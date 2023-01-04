# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    
    _name = 'space_mission.mission'
    _description = 'Mission Info'
    
    spaceship_id = fields.Many2one(comodel_name='space_mission.spaceship',
                                 string='Spaceship',
                                 ondelete='cascade',
                                 required=True)
    name = fields.Char(string='Title',
                       related='spaceship_id.name')
    crew_member_ids = fields.Many2many(comodel_name='res.partner',
                                    string='Crew Members')
    launch_date = fields.Date(string='Launch Date')
    return_date = fields.Date(string='Return Date')
                                 
                                 