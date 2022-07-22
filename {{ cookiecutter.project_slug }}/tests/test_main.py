""" Test suite for {{ cookiecutter.project_slug }}.main
"""

import pytest

from {{ cookiecutter.project_slug }}.main import cli_implementation

@pytest.mark.parametrize("name,expectation",[("World", "Hello World!")])
def test_cli(name: str, expectation: str) -> None:
    """ Asserts whether greetings are correct.
    """
    assert cli_implementation(name) == expectation
