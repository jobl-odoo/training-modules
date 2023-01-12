# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    product_group = fields.Selection(string='Product Group',
                                     selection=[('1234', '1234'),
                                                ('2345', '2345'),
                                                ('3456', '3456')])