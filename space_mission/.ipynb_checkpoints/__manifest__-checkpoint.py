# -*- coding: utf-8 -*-

{
    'name': 'Space Mission',
    'summary': 'Logistics app to manage space mission',
    'description': """
        Space Mission app:
        - Organizes logistics
        - Includes Spaceship and Space Crew
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Logistics',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/space_mission_demo.xml',
    ],
}