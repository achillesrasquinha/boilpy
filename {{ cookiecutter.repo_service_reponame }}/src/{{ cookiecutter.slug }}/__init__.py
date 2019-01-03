{% if cookiecutter.compat != "none" %}
from __future__ import absolute_import
{% endif %}

from {{ cookiecutter.slug }}.__attr__ import (
    __name__,
    __version__,
{% if cookiecutter.cli == "click" %}
    __build__,
{% endif %}
{% if cookiecutter.cli != "none" %}
    __description__,
{% endif %}
    __author__
)

{% if cookiecutter.config == "y" %}
from {{ cookiecutter.slug }}.cache import Cache
cache = Cache()
cache.create()
{% endif %}

{% if cookiecutter.cli != "none" %}
def get_version_str():
    version = "%s%s" % (__version__, " (%s)" % __build__ if __build__ else "")
    return version
{% endif %}