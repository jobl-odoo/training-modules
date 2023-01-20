# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    
    def _confirm_rfqs_to_central(self):
        """Called by Scheduler every night at 00:00
            Confirms all RFQs made to central store."""
        
        print("MADE IT TO METHOD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for record in self.search([('state', 'in', ['draft', 'sent']), ('user_id', '=', 1), ('partner_id', '=', 1)]):
            print("AAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH", record)
            record.button_confirm()