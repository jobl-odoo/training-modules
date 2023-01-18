# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Location(models.Model):
    _inherit = 'stock.location'
    
    
    available = fields.Integer(string='Available')