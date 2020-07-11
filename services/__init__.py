#!/usr/bin/env python3
# coding: utf-8

import os
import json


def get_dump_dir(service):
    return os.path.join(os.getenv('DATA_DUMPS'), service, 'dump.json')


def update_dump(service, data):
    dump_dir = get_dump_dir(service)
    with open(dump_dir, 'w') as f:
        json.dump(data, f, indent=4)


def get_dump(service):
    dump_dir = get_dump_dir(service)
    with open(dump_dir) as f:
        data = json.load(f)
    return data
