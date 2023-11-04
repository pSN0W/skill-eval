from functools import cache
import re
import requests

@cache
def get_repo_description(repo_url):
    def get_raw_url():
        pattern = r'//([^/]+)'
        result = re.sub(pattern, '//raw.githubusercontent.com', repo_url)
        return f"{result.strip('/')}/main/README.md"
    raw_url = get_raw_url()
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    raise Exception("couldn't get data from URL")

@cache
def get_resume_from_url(url):
    def convert_docs_link_to_direct_download(docs_link):
        # Extract the file ID from the given Google Docs link
        match = re.search(r"/d/([^/]+)/", docs_link)
        if match:
            file_id = match.group(1)
            # Construct the direct download link in text format
            direct_download_link = f"https://docs.google.com/document/d/{file_id}/export?format=txt"
            return direct_download_link
        else:
            return None
    
    direct_download_url=convert_docs_link_to_direct_download(url)
    response = requests.get(direct_download_url)
    return response.content.decode('utf-8').replace("\ufeff","").replace("\r","")

def extract_github_urls(text):
    # Define a regular expression to match GitHub URLs
    github_url_pattern = r'https?://github\.com/[\w\-]+/[\w\-]+'

    # Use re.findall to find all matches in the input text
    github_urls = re.findall(github_url_pattern, text)

    return github_urls
def check_for_inclusion_from_resume(interview_minute,resume_info):
    work_experience = " ".join(resume_info["work experience"]) if resume_info["work experience"] else ""
    project_experience = " ".join(resume_info["projects"]) if resume_info["projects"] else ""
    complete_experience = set([word.lower() for word in f"{work_experience} {project_experience}".split(" ") if len(word)>0])
    interview_words = set([word.lower() for word in interview_minute.split(" ") if len(word)>0])
    print(complete_experience)
    print(interview_words)
    print(complete_experience.intersection(interview_words))
    return len(complete_experience.intersection(interview_words)) > 0