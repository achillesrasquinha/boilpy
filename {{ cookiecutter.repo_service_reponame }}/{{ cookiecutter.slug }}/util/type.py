def sequencify(value, type_ = list):
    if not isinstance(value, (list, tuple)):
        value = type_([value])
    return value

def merge_dict(a, b):
    c = a.copy()
    c.update(b)

    return c