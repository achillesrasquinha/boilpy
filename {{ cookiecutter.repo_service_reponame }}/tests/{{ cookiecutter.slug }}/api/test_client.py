from {{ cookiecutter.slug }}.api.client import Client

def test_client():
    client = Client()