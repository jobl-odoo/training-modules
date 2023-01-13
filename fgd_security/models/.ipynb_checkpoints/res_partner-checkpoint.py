# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    
    _inherit = 'res.partner'
    _description = 'FGD res.partner'