"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from python_template import main


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner):
    """It exits with a status code of zero."""
    result = runner.invoke(main.main)
    assert result.exit_code == 0