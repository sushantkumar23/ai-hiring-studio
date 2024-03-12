from fastapi import FastAPI

from llm_client import llm_client
from runner import Runner


app = FastAPI(
    title="AI Hiring Studio API",
    description="API for AI Hiring Studio",
    version="0.1.0"
)

@app.get("/", tags=["Health"])
async def root():
    return {"message": "Hello World"}


@app.post("/match", tags=["Matching"])
async def calculate_similarity_score(job_description_text: str, resume_text: str = None):
    """
    Calculate the match score between the job description and the resume
    """
    runner = Runner(llm_client=llm_client)
    matched_attributes = runner.calculate_match_score(job_description_text, resume_text)
    return {"matched_attributes": matched_attributes}
