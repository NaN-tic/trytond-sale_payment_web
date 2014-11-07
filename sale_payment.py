# This file is part sale_payment_web module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from datetime import datetime

__all__ = [
    'Sale',
    'SalePaymentWeb',
    ]
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'
    paid_in_web = fields.Boolean('Paid in web')


class SalePaymentWeb(ModelSQL, ModelView):
    'Sale Payment Web'
    __name__ = 'sale.payment.web'
    sale = fields.Many2One('sale.sale', 'Sale', required=True, readonly=True)
    date = fields.DateTime('Date', required=True, readonly=True)
    description = fields.Char('Description', readonly=True)
    state = fields.Selection([
        ('done', 'Done'),
        ('pending', 'Pending'),
        ('error', 'Error'),
        ('cancel', 'Cancel'),
    ], 'State', required=True, readonly=True)

    @staticmethod
    def default_date():
        return datetime.now()

    @staticmethod
    def default_state():
        return 'pending'

    def create_sale_payment_web(self, sale, date=None, description=None):
        vlist = [{
                'sale': sale,
                'date': date or datetime.now(),
                'description': description or '',
                }]
        return self.create(vlist)
