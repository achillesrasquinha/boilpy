class {{ cookiecutter.slug.capitalize() }}Error(Exception):
    pass

class DependencyNotFoundError(ImportError):
    pass