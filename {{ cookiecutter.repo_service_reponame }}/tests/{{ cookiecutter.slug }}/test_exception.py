{% set capitalized = cookiecutter.slug.capitalize() %}

# imports - module imports
from {{ cookiecutter.slug }}.exception import (
    {{ capitalized }}Error
)

# imports - test imports
import pytest

def test_{{ cookiecutter.slug }}_error():
    with pytest.raises({{ capitalized }}Error):
        raise {{ capitalized }}Error