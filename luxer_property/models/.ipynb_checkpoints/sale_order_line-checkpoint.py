# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
    
    
#     @api.onchange('product_id')
#     def product_id_change(self):
#         if self.product_id.property_partner_id:
#             self.product_id.partner_shipping_id = self.product_id.property_partner_id
        
#         return super()