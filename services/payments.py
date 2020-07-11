#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function
import json
from squareup.services import get_dump, update_dump
from squareup.transport import Transport


class Payments(object):
    def __init__(self):
        self._service = "payments"
        self._transport = Transport()
        self.payments = self._transport.client.payments

    def get_payment(self, payment_id, **kwargs):
        """ get_payment(payment_id: str) -> dict
        """
        r = self.payments.get_payment(payment_id)
        content = r.body['payment']
        return content

    def list_payments(self, begin_time=None, end_time=None, sort_order=None,
                      cursor=None, location_id=None, total=None, last_4=None, card_brand=None, **kwargs):
        payments = []
        while True:
            params = {
                'begin_time': begin_time, 'end_time': end_time,
                'sort_order': sort_order, 'cursor': cursor,
                'location_id': location_id, 'total': total,
                'last_4': last_4, 'card_brand': card_brand
            }
            r = self.payments.list_payments(**params)
            payments.extend(r.body['payments'])
            if r.cursor:
                cursor = r.cursor
                continue
            break
        return payments

    def sync(self, **kwargs):
        svc_obj = Payments()
        invoke_method = getattr(svc_obj, kwargs['method'])
        payments = invoke_method(**kwargs)
        payments = payments if isinstance(payments, list) else [payments]
        dump = get_dump(self._service)
        for payment in payments:
            payment_id = payment['id']
            dump.update({payment_id: payment})
        update_dump(self._service, dump)
