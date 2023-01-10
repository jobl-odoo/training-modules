# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = 'project.task'
    
    photographer_id = fields.Many2one(comodel_name='res.partner',
                                      string='Photographer')
    
    
    @api.onchange('photographer_id')
    def _onchange_photographer(self):
        """"Updates photographer field in associated sale order."""

        for record in self:
            record.sale_order_id.write({'photographer_id': record.photographer_id.id})