# -*- coding: utf-8 -*-

{
    'name': 'POS Required Fields',
    'summary': """Set VAT and Phone to be required fields in POS""",
    'description': """
        When creating a new client, set the additional following fields
        to be required
        - VAT (Tax ID)
        - Phone
        
        Task ID: 3091247""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'point_of_sale'
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_required/static/src/js/ClientDetailsEdit.js',
        ]
    }
}