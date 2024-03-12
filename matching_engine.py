# matching_engine.py

from llm_client import llm_client
from job_description_parser import JobDescriptionParser
from resume_parser import ResumeParser
from similarity_score import SimilarityScore
from samples import sample_job_description_text, sample_resume_text


class MatchingEngine:
    """
    MatchingEngine is a class that is used to match the job description with the resume

    Methods:
    - match: This method takes the job description and resume as input and returns the
    matched attributes
    """

    def __init__(self, llm_client):
        self.job_description_parser = JobDescriptionParser(llm_client=llm_client)
        self.resume_parser = ResumeParser(llm_client=llm_client)
        self.similarity_score = SimilarityScore(llm_client=llm_client) 

    def match(self, job_description_text, resume_text):
        job_description = self.job_description_parser.parse(job_description_text)
        resume = self.resume_parser.parse(resume_text)
        matched_attributes = self.similarity_score.calculate_score(job_description, resume)
        return matched_attributes


if __name__ == "__main__":
    matching_engine = MatchingEngine(llm_client=llm_client)
    matched_attributes = matching_engine.match(sample_job_description_text, sample_resume_text)
    print(f"Match Summary: {matched_attributes.comments}")
    print(f"Match Score: {matched_attributes.score}")
