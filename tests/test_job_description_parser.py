# test_job_description_parser.py
import pytest

from llm_client import llm_client
from job_description_parser import JobDescriptionParser
from samples import sample_job_description_text


@pytest.fixture
def job_description_parser():
    return JobDescriptionParser(llm_client=llm_client)

def test_job_description_parser(job_description_parser):
    job_description_parser = JobDescriptionParser(llm_client=llm_client)

    # Check if the job_description_parser has an attribute called llm_client
    assert job_description_parser.llm_client is not None

    # Check if the job_description_parser has a method called parse
    assert hasattr(job_description_parser, "parse")


def test_job_description_parser_parse_method(job_description_parser):
    # Check if the parse method returns a JobDescription object
    job_description = job_description_parser.parse(sample_job_description_text)
    assert job_description is not None
    assert job_description.job_title == "Software Engineer"
    assert job_description.location == "San Francisco, CA"
    assert "technology" in job_description.industry.lower()
    assert "computer science" in job_description.education_degree.lower()
