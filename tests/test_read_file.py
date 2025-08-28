import pytest
import os
from challenges.read_file import read_file

TEST_CONTENT = 'Reading as intended'

@pytest.fixture
def fixture_file():
    filename = 'fixture_test.py'
    with open(filename, 'w') as file:
        file.write(TEST_CONTENT)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

def test_returned_content(fixture_file):
    result = read_file(fixture_file)
    assert result == TEST_CONTENT

def test_error_handling():
    # Windows gotcha - throws [WinError 6]
    with pytest.raises((TypeError, OSError)):
        read_file(123)
    with pytest.raises((TypeError, OSError)):
        read_file('Double', 'args')
    with pytest.raises((ValueError)):
        read_file(int('string'))