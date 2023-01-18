# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    project_manager_id = fields.Many2one(comodel_name='res.partner',
                                     string='Project Manager')
    
    project_name = fields.Char(string='Project Name')