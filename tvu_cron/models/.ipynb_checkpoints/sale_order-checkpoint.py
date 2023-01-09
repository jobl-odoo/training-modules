# -*- coding: utf-8 -*-

from datetime import date, timedelta

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    @api.depends('validity_date', 'state')
    def _cancel_expired_quotations(self):
        today = date.today()
        for record in self:
            if (record.state == 'draft') and (record.validity_date < today):
                record.action_cancel()