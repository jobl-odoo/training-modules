# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    product_group = fields.Selection(string='Product Group',
                                     selection=[('1234', '1234'),
                                                ('2345', '2345'),
                                                ('3456', '3456')],
                                     required=True,
                                     default='1234')
    
    
    @api.onchange('product_group')
    def add_pg_to_barcode(self):
        """Prefixes first 2 digits of product group to barcode:
            Product Code = '1234' => Barcode = '12.XXXXXX'
            Barcodes generated from sequence beginning with 900000."""
        
        for record in self:
            if record.barcode:
                original_barcode = record.barcode.split('.')[-1]
            else:
                original_barcode = self.env['ir.sequence'].next_by_code('pg_barcode.barcode')
            if record.product_group:
                record.write({'barcode': f'{record.product_group[:2]}.{original_barcode}'})