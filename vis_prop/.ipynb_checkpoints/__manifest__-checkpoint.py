# -*- coding: utf-8 -*-

{
    'name': 'Visual Props',
    'summary': """Update photographer across modules""",
    'description': """
        When a Photographer is updated on an order/task,
        update the field across all connected orders
        - SO
        - Task
        
        Task ID: 3091245""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['sale_project'],
    'data': [
        'views/sale_order_views_inherit.xml',
        'views/project_task_views_inherit.xml',
    ],
}