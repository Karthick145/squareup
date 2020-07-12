#!/usr/bin/env python3
# coding: utf-8

import os
import configparser

from squareup import DIR


config_file = os.path.join(DIR, 'config.ini')

config = configparser.ConfigParser()
config.read(config_file)

environment = 'PRODUCTION' if config.get('DEFAULT', 'is_prod') == 'true' else 'SANDBOX'

ENVIRONMENT = config.get(environment, 'environment')
ACCESS_TOKEN = config.get(environment, 'access_token')
CLIENT_SECRET = config.get(environment, 'app_id')
