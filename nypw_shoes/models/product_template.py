# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    pairs_per_case = fields.Integer(string='Pairs per Case')
    
    price_per_pair = fields.Monetary(string='Price per Pair')
    
    
    @api.onchange('pairs_per_case', 'price_per_pair')
    def _calc_sales_price(self):
        """Calculate Sales Price based on new fields."""
        
        for record in self:
            if record.pairs_per_case and record.price_per_pair:
                record.list_price = record.pairs_per_case * record.price_per_pair