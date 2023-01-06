# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    
    _name = 'space_mission.project.wizard'
    _description = 'Wizard: Create Project for Mission'
    
    def _default_session(self):
        return self.env['space_mission.mission'].browse(self._context.get('active_id'))
    
    name = fields.Char(required=True, string='Project Name')
    
    mission_id = fields.Many2one(comodel_name='space_mission.mission',
                                 string='Mission',
                                 required=True,
                                 default=_default_session)
    mission_crew_member_ids = fields.Many2many(comodel_name='res.partner',
                                               string='Crew Members on Mission',
                                               related='mission_id.crew_member_ids',
                                               help='These are the crew members for the mission')
    
    
    def create_project(self):
        
        project_id = self.env['project.project'].create({
            'mission_id': self.mission_id.id,
            'name': self.name})