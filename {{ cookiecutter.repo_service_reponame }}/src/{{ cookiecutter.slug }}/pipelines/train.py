from {{ cookiecutter.slug }}.data.get_data import get_data_dir

def build_model():
    pass
    # do something ...

def train(data_dir = None, artifacts_dir = None, *args, **kwargs):
    data_dir = get_data_dir(data_dir)
    model    = build_model()
    # do something ...