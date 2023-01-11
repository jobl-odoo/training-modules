# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'
    
    property_partner_id = fields.Many2one(comodel_name='res.partner',
                                       string='Property Partner')
    
    
    @api.onchange('property_partner_id')
    def change_delivery_address_to_pp(self):
        """If Property Partner is set, update delivery address to match."""
        
        if self.property_partner_id:
            self.partner_shipping_id = self.property_partner_id
        elif self.partner_id:
            self.partner_shipping_id = self.partner_id