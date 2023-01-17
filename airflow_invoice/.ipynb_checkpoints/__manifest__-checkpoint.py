# -*- coding: utf-8 -*-

{
    'name': 'Air Flow Invoice',
    'summary': """Custom invoicing/pdf for Air Flow""",
    'description': """
        Adjust invoice form/pdf report based on custom specifications
        - Add 'Billing Address' header
        - Re-name 'Description' -> 'Customer PO'
        - Add 'Ship Date' field
        - Add 'Shipping Method' field
        - Add 'Project Manager' field
        - Add 'Project Name' field
        - Add 'email' and 'phone' to Sales Channel model and display
        - Remove Source Document
        - Remove 'Unit Price' column
        - Remove 'Taxes' column
        - Adjust 'Tax Description' based on conditions
        
        Task ID: 3091182""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'sale'
    ],
    'data': [
        'views/sale_order_views_inherit.xml',
    ],
}