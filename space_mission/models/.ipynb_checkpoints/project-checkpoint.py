# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    
    _inherit = 'project.project'
    
    mission_id = fields.Many2one(comodel_name='space_mission.mission',
                                 string='Related Mission',
                                 ondelete='set null')
    crew_member_ids = fields.Many2many(string='Crew Members',
                                       related='mission_id.crew_member_ids')