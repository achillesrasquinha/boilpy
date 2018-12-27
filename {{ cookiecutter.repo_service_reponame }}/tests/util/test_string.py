def test_strip():
    from {{ cookiecutter.slug }}.util.string import strip
    
    assert strip("\nfoobar")       == "foobar"
    assert strip("foobar\n")       == "foobar"
    
    assert strip("\nfoobar\n")     == "foobar"
    assert strip("\r\nfoobar\r\n") == "foobar"