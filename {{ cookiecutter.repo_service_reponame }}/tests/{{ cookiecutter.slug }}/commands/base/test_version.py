def test_version(runner):
    from {{ cookiecutter.slug }}.commands.base.version import version
    from {{ cookiecutter.slug }} import get_version_str

    result = runner.invoke(version)
    assert result.exit_code == 0
    assert result.output    == "%s\n" % get_version_str()