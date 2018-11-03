import os.path as osp

def pardir(path, level = 1):
    for _ in range(level):
        path = osp.dirname(path)
    return path