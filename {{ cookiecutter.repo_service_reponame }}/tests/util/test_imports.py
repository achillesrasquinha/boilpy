import pytest

def test_import_handler():
    import sys, os
    from   {{ cookiecutter.slug }}.util.imports import import_handler
    import {{ cookiecutter.slug }}
    
    assert import_handler("os")  == os
    assert import_handler("sys") == sys

    assert import_handler("os.path")  == os.path
    assert import_handler("sys.path") == sys.path

    assert import_handler("{{ cookiecutter.slug }}") == {{ cookiecutter.slug }}
    assert import_handler("{{ cookiecutter.slug }}.util.imports.import_handler") == import_handler

    with pytest.raises(ImportError) as e:
        import_handler("foo.bar.baz")