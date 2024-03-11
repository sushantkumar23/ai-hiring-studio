from pydantic import BaseModel
from typing import List, Optional


class JobDescription(BaseModel):
    job_title: str
    location: str
    industry: str
    education_degree: str
    technical_skills: List[str]


class Resume(BaseModel):
    candidate_name: str
    email: Optional[str]
    phone: Optional[str]
    location: str
    industry: List[str]
    education_degree: List[str]
    skills: List[str]
