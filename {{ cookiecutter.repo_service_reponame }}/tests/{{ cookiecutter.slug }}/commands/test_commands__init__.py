import os.path as osp

# imports - compatibility imports
from {{ cookiecutter.slug }}.commands    import _command as command
from upyog.util._dict  import merge_dict
from upyog.util.string import strip_ansi

# imports - test imports
import pytest

# imports - test imports
from testutils import mock_input, PATH