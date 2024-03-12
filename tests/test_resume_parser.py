# test_resume_parser.py
import pytest

from llm_client import llm_client
from resume_parser import ResumeParser
from samples import sample_resume_text


@pytest.fixture
def resume_parser():
    return ResumeParser(llm_client=llm_client)

def test_resume_parser(resume_parser):
    # Check if the resume_parser has an attribute called llm_client
    assert resume_parser.llm_client is not None

    # Check if the resume_parser has a method called parse
    assert hasattr(resume_parser, "parse")


def test_resume_parser_parse_method(resume_parser):
    # Check if the parse method returns a Resume object
    resume = resume_parser.parse(sample_resume_text)
    assert resume is not None
    assert resume.name == "Jane Doe"
    assert resume.location == "San Francisco, CA"
    assert "computer science" in resume.education.lower()
    assert "software engineer" in resume.experience.lower()
