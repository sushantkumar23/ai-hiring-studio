# matching_engine.py
import json

from models import JobDescription, Resume
from tools import matching_engine_tools
from config import MODEL_NAME


class MatchingEngine:
    """
    MatchingEngine is a class that is used to match the job description with the resume using cosine similarity

    Methods:
    - match: This method takes the job description and resume as input and returns the matched attributes
    """
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def match(self, job_description: JobDescription, resume: Resume):

        user_message = "The job description is as follows: " + json.dumps(job_description.__dict__) + " and the resume is as follows: " + json.dumps(resume.__dict__)
        print(user_message)
        response = self.llm_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "Match the job description with the resume based on the attributes such as location, industry, education degree, and skills. Provide details about the matched attributes and an overall similarity score out of 100."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            tools=matching_engine_tools
        )
        matching_comments_and_score =  json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        return matching_comments_and_score
