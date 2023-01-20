# -*- coding: utf-8 -*-

{
    'name': 'Mindesa Scheduled RFQ Confirm',
    'summary': """Confirms all RFQs each night made to central store""",
    'description': """
        Scheduled Action to auto-confirm RFQs made to central store
        - Adds method to purchase.order model
        - Adds scheduled action to call method
        
        Task ID: 3091209""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'purchase',
        'stock',
        'contacts',
    ],
    'data': [
    ],
}