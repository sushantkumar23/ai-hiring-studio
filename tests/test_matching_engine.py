
import pytest

from llm_client import llm_client
from matching_engine import MatchingEngine


def test_matching_engine():
    matching_engine = MatchingEngine(llm_client=llm_client)

    # Check if the matching_engine has an attribute called llm_client
    assert matching_engine.llm_client is not None
