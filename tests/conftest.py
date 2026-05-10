import sys
import os
import pytest

# Add the project root to sys.path so that absolute imports from the root work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.api_client import APIClinet


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client(base_url):
    return APIClinet(base_url)