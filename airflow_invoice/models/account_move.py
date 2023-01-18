# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    
    ship_date = fields.Date(string='Ship Date')
    
    shipping_method = fields.Many2one(comodel_name='delivery.carrier',
                                      string='Shipping Method')
    
    project_manager_id = fields.Many2one(related='invoice_line_ids.sale_line_ids.order_id.project_manager',
                                         string='Project Manager')
    
    project_name_id = fields.Char(related='invoice_line_ids.sale_line_ids.order_id.project_name',
                                      string='Project Name')
    
    sales_team_email = fields.Char(related='team_id.email',
                                   string='Sales Team Email')
    
    sales_team_phone = fields.Char(related='team_id.phone',
                                   string='Sales Team Phone')