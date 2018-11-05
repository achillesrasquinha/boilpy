from {{ cookiecutter.slug }}.__attr__ import (
    __name__,
    __version__,
    __build__,
    __description__
)

def get_version_str():
    version = "%s%s" % (
        {{ cookiecutter.slug }}.__version__,
        " (%s)" % {{ cookiecutter.slug }}.__build__
            if {{ cookiecutter.slug }}.__build__ else ""
    )

    return version