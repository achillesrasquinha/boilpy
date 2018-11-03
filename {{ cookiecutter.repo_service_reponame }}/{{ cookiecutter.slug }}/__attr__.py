from {{ cookiecutter.slug }}.util.git    import get_revision
from {{ cookiecutter.slug }}.util.system import pardir

__name__                    = "{{ cookiecutter.name.lower().replace(' ', '-') }}"
__version__                 = "{{ cookiecutter.version }}"
__build__                   = get_revision(pardir(__file__, 2), raise_err = False)
__author__                  = "{{ cookiecutter.author  }}"
__email__                   = "{{ cookiecutter.email   }}"
__description__             = "{{ cookiecutter.description }}"
__keywords__                = "{{ cookiecutter.keywords.split(" ") }}"
__url__                     = "{{ cookiecutter.url     }}"
__license__                 = "{{ cookiecutter.license }}"