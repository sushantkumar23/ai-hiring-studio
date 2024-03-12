# main.py

from llm_client import llm_client
from job_description_parser import JobDescriptionParser
from resume_parser import ResumeParser
from matching_engine import MatchingEngine

class Runner:

    def __init__(self, llm_client):
        self.job_description_parser = JobDescriptionParser(llm_client=llm_client)
        self.resume_parser = ResumeParser(llm_client=llm_client)
        self.matching_engine = MatchingEngine(llm_client=llm_client)
        

    def calculate_match_score(self, job_description_text, resume_text):
        job_description = self.job_description_parser.parse(job_description_text)
        resume = self.resume_parser.parse(resume_text)
        matched_attributes = self.matching_engine.match(job_description, resume)
        return matched_attributes


sample_job_description_text = """
Job Title: Software Engineer
Location: San Francisco, CA
Industry/Domain: Technology
Education Degree: Bachelor's in Computer Science or related field
Technical Skills: Python, Java, SQL, Git, Agile methodologies
"""

sample_resume_text = """
Name: Jane Doe
Location: San Francisco, CA
Education: Bachelor's in Computer Science, University of California, Berkeley
Experience: Software Engineer at TechCorp, proficient in Python, Java, SQL, Git, and experienced in Agile methodologies.
"""

if __name__ == "__main__":
    runner = Runner(llm_client=llm_client)
    matched_attributes = runner.calculate_match_score(sample_job_description_text, sample_resume_text)
    print(f"Match Summary: {matched_attributes.comments}")
    print(f"Match Score: {matched_attributes.score}")
