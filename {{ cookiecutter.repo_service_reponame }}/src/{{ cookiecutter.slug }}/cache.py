import os, os.path as osp

import {{ cookiecutter.slug }}
from   {{ cookiecutter.slug }}.util.system import makedirs

class Cache:
    def __init__(self, location = None, dirname = None):
        self.location = location or osp.expanduser("~")
        self.dirname  = dirname  or ".%s" % ({{ cookiecutter.slug }}.__name__)

    def create(self, exist_ok = True):
        path = osp.join(self.location, self.dirname)
        makedirs(path, exist_ok = exist_ok)