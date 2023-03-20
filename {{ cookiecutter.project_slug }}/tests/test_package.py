"""Test suite for package-level items."""

from {{ cookiecutter.project_slug }} import __version__


def test_version():
    """Should be the current version number."""
    assert __version__ == "0.3.3"


def test_version_type():
    """Should be a string."""
    assert isinstance(__version__, str)


def test_version_number_is_semver():
    """Should be a semver."""
    assert all([int(x) for x in __version__.split(".")])
