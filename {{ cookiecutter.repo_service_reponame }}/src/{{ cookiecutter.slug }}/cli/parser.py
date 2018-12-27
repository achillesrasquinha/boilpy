# imports - standard imports
import argparse

# imports - module imports
import {{ cookiecutter.slug }}

VERSION_STRING = {{ cookiecutter.slug }}.get_version_str()

def get_parser():
    parser = argparse.ArgumentParser(
        description = {{ cookiecutter.slug }}.__description__
    )
    parser.add_argument("-v", "--version",
        action  = "version",
        version = VERSION_STRING
    )

    return parser

def get_parsed_args():
    parser  = get_parser()
    args, _ = parser.parse_known_args()

    return args