{% if cookiecutter.compat != "none" %}
from __future__ import absolute_import
{% endif %}

from {{ cookiecutter.slug }}.__attr__ import (
    __name__,
    __version__,
    __build__,
    __description__,
    __author__
)

def get_version_str():
    version = "%s%s" % (__version__, " (%s)" % __build__ if __build__ else "")
    return version