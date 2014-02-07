# This file is part of sale_payment_web module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .sale_payment import *


def register():
    Pool.register(
        Sale,
        SalePaymentWeb,
        module='sale_payment_web', type_='model')
