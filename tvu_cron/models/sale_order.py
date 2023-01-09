# -*- coding: utf-8 -*-

from datetime import date

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    def _cancel_expired_quotations(self):
        today = date.today()
        for record in self.search([('state', '=', 'draft'), ('validity_date', '!=', False), ('validity_date', '<', today)]):
            record.action_cancel()