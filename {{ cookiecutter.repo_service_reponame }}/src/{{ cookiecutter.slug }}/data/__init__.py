import os.path as osp

from {{ cookiecutter.slug }}.config import PATH
from {{ cookiecutter.slug }} import __name__ as NAME

from bpyutils.util.environ import getenv
from bpyutils.util.system  import makedirs

_PREFIX = NAME.upper()

def get_data_dir(data_dir = None):
    data_dir = data_dir \
        or getenv("DATA_DIR", prefix = _PREFIX) \
        or osp.join(PATH["CACHE"], "data")

    makedirs(data_dir, exist_ok = True)

    return data_dir

def get_data(data_dir = None):
    data_dir = get_data_dir(data_dir)
    # do something ...

def preprocess_data(data_dir = None):
    data_dir = get_data_dir(data_dir)
    # do something ...