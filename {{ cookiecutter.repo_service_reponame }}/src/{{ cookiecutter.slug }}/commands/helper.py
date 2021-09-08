# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import sys, os, os.path as osp
import re
import json

# imports - module imports
from {{ cookiecutter.slug }}.commands.util 	import cli_format
from {{ cookiecutter.slug }}.table      	import Table
from {{ cookiecutter.slug }}.tree			import Node as TreeNode
from bpyutils.util.string    import pluralize, strip
from bpyutils.util.system   	import read, write, popen, which
from bpyutils.util.array		import squash
from {{ cookiecutter.slug }} 		      	import (cli, semver,
	log, parallel
)
from {{ cookiecutter.slug }}.exception		import PopenError

logger = log.get_logger()