# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'
    
    property_partner_id = fields.Many2one(comodel_name='res.partner',
                                       string='Property Partner')