# -*- coding: utf-8 -*-

{
    'name': "L'Agence Automated",
    'summary': """Adds automatic action to calc 'Available' in location.""",
    'description': """
        Adjust new 'Available' field 
        - Increment on validation of receipt record
        - Decrement on validation of delivery order
        - Avail can have max of 50, min of 0
        
        Task ID: 3091187""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'stock'
    ],
    'data': [
    ],
}