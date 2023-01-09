# -*- coding: utf-8 -*-

{
 
    'name': 'TVU Cron',
    'summary': """Auto-cancel expired quotations""",
    'description': """
        Every night at midnight, cancels all quotations
        - if expiration date is before current day
        - skips any non-set expiration dates""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/sale_order_views_inherit.xml',
    ],
}