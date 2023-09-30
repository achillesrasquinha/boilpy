from __future__ import absolute_import

import os.path as osp, upyog as upy

from {{ cookiecutter.slug }}.__attr__ import __name__ as NAME

PATH = dict()

PATH["BASE"]  = upy.pardir(__file__, 1)
PATH["DATA"]  = osp.join(PATH["BASE"], "data")
PATH["CACHE"] = upy.get_config_path(NAME)