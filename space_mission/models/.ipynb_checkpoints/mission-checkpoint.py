# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

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
    fuel_required_in_t = fields.Integer(string='Fuel Required in Tons')
    num_engines = fields.Integer(string='Number of Engines')
    safety_features = fields.Selection(string='Safety Features',
                                       selection=[('low', 'Low'),
                                                  ('medium', 'Medium'),
                                                  ('high', 'High')])
    
    mission_duration = fields.Integer(string='Mission Length in Days',
                                      compute='_compute_mission_duration',
                                      store=True)
    
    @api.depends('launch_date', 'return_date')
    def _compute_mission_duration(self):
        for record in self:
            if not (record.launch_date and record.return_date):
                record.mission_duration = 0
            else:
                duration = record.return_date - record.launch_date
                record.mission_duration = duration.days