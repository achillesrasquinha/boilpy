# imports - module imports
from {{ cookiecutter.slug }}       import cli
from {{ cookiecutter.slug }}.table import _sanitize_string, Table

def test__sanitize_string():
    assert _sanitize_string(cli.format("foobar", cli.GREEN)) == "foobar"
    assert _sanitize_string(cli.format("foobar", cli.BOLD))  == "foobar"

def test_table():
    table  = Table()
    assert table.empty
    
    dummy  = ["foo", "bar"]

    table.insert(dummy)
    assert not table.empty
    
    string = table.render()
    assert string.count("\n") == 1

    table.header = dummy
    string = table.render()
    assert string.count("\n") == 2

    table.insert(dummy)
    string = table.render()
    assert string.count("\n") == 3