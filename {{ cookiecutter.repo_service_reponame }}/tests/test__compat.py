# imports - module imports
from {{ cookiecutter.slug }}._compat import PYTHON_VERSION, _is_python_version, iteritems

def test__is_python_version():
    def _assert_version(major, minor):
        if PYTHON_VERSION.major == major and PYTHON_VERSION.minor == minor:
            assert _is_python_version(major = major, minor = minor)

    _assert_version(2, 7)
    _assert_version(3, 4)
    _assert_version(3, 5)
    _assert_version(3, 6)
    _assert_version(3, 7)

    assert _is_python_version(
        major = PYTHON_VERSION.major,
        minor = PYTHON_VERSION.minor,
        patch = PYTHON_VERSION.micro
    )

def test_iteritems():
    dict_ = dict(foo = "bar")
    
    assert isinstance(iteritems(dict_), collections.Iterable)

    for k, v in iteritems(dict_):
        assert dict_[k] == v