# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    project_manager = field.Many2one(comodel_name='res.partner',
                                     related='account.move',
                                     string='Project Manager')
    
    project_name = field.Char(related='account.move',
                              string='Project Name')