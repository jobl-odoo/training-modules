# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = 'project.task'
    
    photographer_id = fields.Many2one(comodel_name='res.partner',
                                      string='Photographer')