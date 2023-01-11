# -*- coding: utf-8 -*-

{
    'name': 'Luxer Property',
    'summary': """Copy Property Partner field to invoice""",
    'description': """
        Adds 'property_partner' (res.partner) field to a Subscription.
        - when creating an invoice, if filled in,
        copies field data to 'delivery address' on invoice
        
        Task ID: 3091243""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['sale_subscription'],
    'data': [
        'views/product_template_views_inherit.xml',
    ],
}