# -*- coding: utf-8 -*-

{
    'name': 'PG Barcode',
    'summary': """Add Product Group to Barcode""",
    'description': """
        Adjusts barcode based on new Product Group field
        - first 2 digits of Product Group added to barcode
        - barcode from 6 digit sequence beginning with 900000
        - XX.barcode
        
        Task ID: 3091248""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'stock_barcode'
    ],
    'data': [
        'views/product_template_views_inherit.xml',
        'data/product_template_sequence.xml',
    ],
}