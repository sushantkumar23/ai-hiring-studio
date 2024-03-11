# resume_parser.py
import json

from models import Resume
from tools import resume_tools
from config import MODEL_NAME


class ResumeParser:
    """
    ResumeParser is a class that is used to parse the resume using the LLM Function call

    Methods:
    - parse: This method takes the resume text as input and returns a Resume object
    """

    def __init__(self, llm_client):
        self.llm_client = llm_client

    def parse(self, text):
        response = self.llm_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "Parse the resume that has been provided"
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            tools=resume_tools
        )
        parsed_dict =  json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        resume = Resume(**parsed_dict)
        return resume