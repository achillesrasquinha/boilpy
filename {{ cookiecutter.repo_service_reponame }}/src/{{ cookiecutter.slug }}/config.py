from {{ cookiecutter.slug }}.__attr__ import __name__ as NAME

from bpyutils.config import get_config_path

PATH = dict()

PATH["CACHE"] = get_config_path(NAME)