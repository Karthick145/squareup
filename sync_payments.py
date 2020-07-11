#!/usr/bin/env python3
# coding: utf-8

import argparse
from squareup.services.payments import Payments


def main():
    parser = argparse.ArgumentParser(description='Syncing payments')

    parser.add_argument('--method', '-m', action='store', default='list_payments', required=True,
                    help='sync method. One of (get_payment, list_payments)')
    parser.add_argument('--payment-id', '-id', action='store', default=None,
                    help='Unique id of transaction')
    parser.add_argument('--begin-time', '-begin-time', action='store', default=None,
                    help='Timestamp for the beginning of the reporting period, in RFC 3339 format.'
                         'Inclusive. Default: The current time minus one year.')
    parser.add_argument('--end-time', '-end-time', action='store', default=None,
                    help='Timestamp for the end of the requested reporting period, in RFC 3339 format.\n'
                         'Default: The current time.')
    parser.add_argument('--sort-order', '-sort-order', action='store', default=None,
                    help='The order in which results are listed.\n'
                         '  ASC - oldest to newest\n'
                         '  DESC - newest to oldest (default).')
    parser.add_argument('--cursor', '-cursor', action='store', default=None,
                    help='A pagination cursor returned by a previous call to this endpoint')
    parser.add_argument('--location-id', '-location-id', action='store', default=None,
                    help='Limit results to the location supplied.')
    parser.add_argument('--total', '-total', action='store', default=None,
                    help='The exact amount in the total_money for a Payment.')
    parser.add_argument('--last-4', '-last-4', action='store', default=None,
                    help='The last 4 digits of Payment card.')
    parser.add_argument('--card-brand', '-card-brand', action='store', default=None,
                    help='The brand of Payment card. For example, VISA')

    args = parser.parse_args()
    if args.method == 'get_payment' and args.payment_id is None:
        raise ValueError("Payment id is required for method %s" %(args.method))

    svc_obj = Payments()
    svc_obj.sync(**dict(args._get_kwargs()))


if __name__ == "__main__":
    main()
