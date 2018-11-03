import sys

from   {{ cookiecutter.slug }}.commands import main

if __name__ == "__main__":
    code = main()
    sys.exit(code)
