import os.path as osp

from {{ cookiecutter.slug }}.util.git    import get_revision
from {{ cookiecutter.slug }}.util.system import pardir, read

__name__                    = "{{ cookiecutter.name.lower().replace(' ', '-') }}"
__version__                 = read(osp.join(pardir(__file__), "VERSION"))
__build__                   = get_revision(pardir(__file__, 2), short = True, raise_err = False)
__author__                  = "{{ cookiecutter.author  }}"
__email__                   = "{{ cookiecutter.email   }}"
__description__             = "{{ cookiecutter.description }}"
__keywords__                = {% if cookiecutter.keywords %}{{ cookiecutter.keywords.split(" ") }}{% else %}[]{% endif %}
__url__                     = "{{ cookiecutter.url     }}"
__license__                 = "{{ cookiecutter.license }}"