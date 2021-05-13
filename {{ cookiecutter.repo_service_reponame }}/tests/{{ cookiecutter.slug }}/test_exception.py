{% set capitalized = cookiecutter.slug.capitalize() %}

# imports - standard imports
import subprocess as sp

# imports - module imports
from {{ cookiecutter.slug }}.util.system import popen
from {{ cookiecutter.slug }}.exception   import (
    {{ capitalized }}Error,
    PopenError
)

# imports - test imports
import pytest

def test_{{ cookiecutter.slug }}_error():
    with pytest.raises({{ capitalized }}Error):
        raise {{ capitalized }}Error

def test_popen_error():
    with pytest.raises(PopenError):
        popen('python -c "raise TypeError"')

    assert isinstance(
        PopenError(0, "echo foobar"),
        ({{ capitalized }}Error, sp.CalledProcessError)
    )
    assert isinstance({{ capitalized }}Error(), Exception)