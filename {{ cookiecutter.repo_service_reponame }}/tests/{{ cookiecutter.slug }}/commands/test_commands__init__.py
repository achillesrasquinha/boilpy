import os.path as osp

# imports - compatibility imports
from {{ cookiecutter.slug }}.commands    import _command as command
from {{ cookiecutter.slug }}.util._dict  import merge_dict
from {{ cookiecutter.slug }}.util.string import strip_ansi

# imports - test imports
import pytest

# imports - test imports
from testutils import mock_input, PATH