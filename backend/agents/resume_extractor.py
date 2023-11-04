from .json_agent import JsonAgent

RESUME_EXTRACTOR_PROMPT = """
    Given a resume you need to parse that resume and extract information from it. You need to extract name, email, github, work experience, projects and skills from it. You are to output the answer in the Json form. If any of the key is not available then have null for that key. Don't guess it yourself. 
    One example output is:
    {"name": "Albert Einstien", "email":"27albert86@gmail.com", "github":"https://github.com/alber29", "work experience": null, "projects":["hello-world","nft-gen"], "skills": ["blockchain","c++"]}
    You can list all other organisation name then the name of the person in work experience
    """
    
class ResumeExtractor(JsonAgent):
    def __init__(self):
        super().__init__(
            name="resume_extractor",
            system_message = RESUME_EXTRACTOR_PROMPT)
        
    def extract_info(self):
        return self.get_last_message_as_json()