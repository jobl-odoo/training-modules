# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesTeam(models.Model):
    _inherit = 'crm.team'
    
    
    email = fields.Char(string='Email')
    
    phone = fields.Char(string='Phone')