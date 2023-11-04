from .agents.conversation_initializer import ConversationInitializer
from .agents.candidate import Candidate
from .agents.hr_manager import HRManager
from .agents.interviewer import Interviewer
from .agents.interview_evaluator import InterviewEvaluator
from .agents.project_evaluator import ProjectEvaluator
from .utils import get_repo_description,get_resume_from_url,extract_github_urls, check_for_inclusion_from_resume, extract_info_from_resume

def get_question_from_jd(jd):
    hr_manager = HRManager()
    user_proxy = ConversationInitializer()
    user_proxy.initiate_chat(
        hr_manager,
        message=jd
    )
    return hr_manager.get_questions()

def get_candidate_rating(questions, resume_url):
    final_score = {}
    chat = ""
    for question in questions:
        res = get_question_rating(question, resume_url)
        score = res["score"]
        conversation = res["conversation"]
        chat += f"{conversation} \n"
        for k,v in score.items():
            if v is not None and k!="":
                final_score.setdefault(k,[])
                final_score[k].append(v)
    rating = {k:sum(v)/len(v) for k,v in final_score.items() if k!="reason"}
    return rating,chat
    
def get_question_rating(que,resume_url):
    resume = get_resume_from_url(resume_url)
    interview_minute = get_interview_minute(que,resume)
    ans_score = get_interview_score(interview_minute)
    github_urls = extract_github_urls(interview_minute)
    resume_info = extract_info_from_resume(resume_url)
    if github_urls:
        score = {"complexity": 0, "uniqueness": 0, "reason": "", "reference":""}
        for url in github_urls:
            try:
                project_rating = get_project_rating(get_repo_description(url))
                if score["complexity"] + score["uniqueness"] < project_rating["complexity"] + project_rating["uniqueness"]:
                    score = project_rating
                    score["reference"] = url
            except:
                pass
    elif check_for_inclusion_from_resume(interview_minute,resume_info):
        score = {
            "complexity": 10, 
            "uniqueness": 10, 
            "reason": "Candidate refered their work experience", 
            "reference": "work"
        }
    else:
        score = {
            "complexity": 4, 
            "uniqueness": 4, 
            "reason": "Candidate didn't refer anything", 
            "reference": "none"
        }
    weightage = (score["complexity"] + score["uniqueness"])/20
    
    hr_score = f"Evaluator: {ans_score}, weightage: {score}, final score = "
    ans_score["technical_skill"] *= weightage
    ans_score["relevance"] *= weightage
    hr_score += f"{ans_score}"
    return {"conversation": f"{interview_minute}\n{hr_score}", "score": ans_score}

def get_project_rating(project_desc):
    project_desc += "\nGiven the description rate the project in the specified form"
    
    project_evaluator = ProjectEvaluator()
    user_proxy = ConversationInitializer()
    user_proxy.initiate_chat(
        project_evaluator,
        message=project_desc
    )
    return project_evaluator.get_rating()

def get_interview_minute(question, resume):
    interviewer = Interviewer()
    candidate = Candidate(resume=resume)
    interviewer.initiate_chat(
        candidate,
        message=question
    )
    
    get_role = lambda conv: 'Interviewer' if conv['role'] == 'assistant' else 'Candidate'
    
    interview_minute = "\n".join([
        f"{get_role(conversation)}: {conversation['content']} " for conversation in interviewer.chat_messages[candidate]
    ])
    
    return interview_minute

def get_interview_score(interview_minute):
    evaluator = InterviewEvaluator()
    user_proxy = ConversationInitializer()
    user_proxy.initiate_chat(
        evaluator,
        message=interview_minute
    )
    return evaluator.get_rating()
