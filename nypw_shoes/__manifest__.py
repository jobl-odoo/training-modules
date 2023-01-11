# -*- coding: utf-8 -*-

{
    'name': 'NY P&W Shoes',
    'summary': """Calulate sale price based on new fields""",
    'description': """
        Sales Price of product computed based on new fields in product.template
        - adds pair_per_case field
        - adds price_per_pair field
        - computes list_price based on above
        
        Task ID: 3091249""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'views/product_template_views_inherit.xml',
    ],
}