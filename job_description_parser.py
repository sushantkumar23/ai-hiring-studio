# job_description_parser.py
import json

from models import JobDescription
from tools import job_description_tools
from config import MODEL_NAME


class JobDescriptionParser:
    """
    JobDescriptionParser is a class that is used to parse the job description using the LLM Function call
    
    Methods:
    - parse: This method takes the job description text as input and returns a JobDescription object
    """
    
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def parse(self, text):
        response = self.llm_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "Parse the job description that has been provided this will used for matching the job with the right candidate"
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            tools=job_description_tools
        )
        parsed_dict =  json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        job_description = JobDescription(**parsed_dict)
        return job_description