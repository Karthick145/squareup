#!/usr/bin/env python3
# coding: utf-8

from square.client import Client
import squareup.constants as CONST


class Transport(object):
    def __init__(self):
        self.client = Client(environment=CONST.ENVIRONMENT,
                             access_token=CONST.ACCESS_TOKEN)
