# llm_client.py
import os
from openai import OpenAI


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm_client = OpenAI(api_key=OPENAI_API_KEY)
