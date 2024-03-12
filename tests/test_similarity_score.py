# test_similarity_score.py
import pytest

from llm_client import llm_client
from similarity_score import SimilarityScore
from samples import sample_job_description_text, sample_resume_text


@pytest.fixture
def similarity_score():
    return SimilarityScore(llm_client=llm_client)


def test_similarity_score(similarity_score):
    # Check if the similarity_score has an attribute called llm_client
    assert similarity_score.llm_client is not None

    # Check if the similarity_score has a method called calculate
    assert hasattr(similarity_score, "calculate")


def test_similarity_score_calculate_method(similarity_score: SimilarityScore):
    # Check if the calculate method returns a MatchedAttributes object
    matched_attributes = similarity_score.calculate_score(sample_job_description_text, sample_resume_text)

    assert matched_attributes is not None
    assert matched_attributes.score is not None
