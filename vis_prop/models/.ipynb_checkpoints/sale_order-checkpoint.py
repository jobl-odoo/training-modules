# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    photographer_id = fields.Many2one(comodel_name='res.partner',
                                      string='Photographer')
    
    @api.onchange('photographer_id')
    def _onchange_photographer(self):
        
        for record in self:
            for task in record.tasks_ids:
                task.write({'photographer_id': record.photographer_id})