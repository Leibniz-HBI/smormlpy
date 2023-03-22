"""Test suite for package-level items."""
import re

from {{ cookiecutter.project_slug }} import __version__


def test_version():
    """Should be the current version number."""
    assert __version__ == "1.0.0"


def test_version_type():
    """Should be a string."""
    assert isinstance(__version__, str)


def test_version_number_is_semver():
    """Should be a semver."""
    assert re.match(r"\d+\.\d+\.\d+-{0,1}\w*", __version__) is not None
