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
    'depends': ['project', 'website'],
    'data': [
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
        'views/project_views_inherit.xml',
        'wizard/project_wizard_view.xml',
        'views/space_mission_web_templates.xml',
    ],
    'demo': [
        'demo/space_mission_demo.xml',
    ],
}