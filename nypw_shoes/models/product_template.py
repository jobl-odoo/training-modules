# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    pairs_per_case = fields.Integer(string='Pairs per Case')
    
    price_per_pair = fields.Monetary(string='Price per Pair')