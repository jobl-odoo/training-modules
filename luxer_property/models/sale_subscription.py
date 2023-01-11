# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'
    
    property_partner_id = fields.Many2one(comodel_name='res.partner',
                                       string='Property Partner')