def test_imports():
    from {{ cookiecutter.slug }} import (
        __name__    as _,
        __version__ as _,
        __author__  as _,
        main        as _
    )