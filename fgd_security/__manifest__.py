# -*- coding: utf-8 -*-

{
    'name': 'FGD Security',
    'summary': """Set access rights for specific Sale groups""",
    'description': """
        Adds 2 access right groups, and adjust rights for
        Salesperson and Pricelist when on Contact page
        - Adds 'Sales / Administration (Commission)'
        - Adds 'Sales / All Documents'
        - Admin and Admin (C) access when create/edit contact
        - Own Doc and All Doc access when create only
        
        Task ID: 3091244""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base'
    ],
    'data': [
        'security/fgd_security_security.xml',
        'security/ir.model.access.csv',
    ],
}