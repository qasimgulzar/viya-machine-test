import functools

import yaml


@functools.cache
def load_raw_queries():
    with open('raw-sql-statements.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)
