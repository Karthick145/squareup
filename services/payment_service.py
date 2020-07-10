#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from squareup.transport import Transport


class PaymentService(object):
    def __init__(self):
        self._transport = Transport()
        self.payments = self._transport.client.payments

    def get_payment_by_id(self, id):
        r = self.payments.get_payment(id)
        return r.body

    def list_payments(self, begin_time=None, end_time=None, sort_order=None,
                      cursor=None, location_id=None, total=None, last_4=None, card_brand=None):
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


if __name__ == '__main__':
    ps = PaymentService()
    print(ps.get_payment_by_id('l2Yv0D21NgOENfUzc7CFlPQXHlcZY'))