# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    photographer_id = fields.Many2one(comodel_name='res.partner',
                                      string='Photographer')