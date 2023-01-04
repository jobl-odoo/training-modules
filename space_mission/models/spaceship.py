# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Spaceship(models.Model):
    
    _name = 'space_mission.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Title', required=True)
    height_in_m = fields.Integer(string='Height in Meters')
    diameter_in_m = fields.Integer(string='Diameter in Meters')
    payload_to_leo_in_t = fields.Integer(string='Payload to LEO in Tons')
    fuel_type = fields.Selection(
        string='Fuel Type',
        selection=[('liquid', 'Liquid'),
                   ('solid', 'Solid')])
    ship_type = fields.Selection(
        string='Ship Type',
        selection=[('small', 'Small'),
                   ('medium', 'Medium'),
                   ('large', 'Large')],)
    num_passengers = fields.Integer(string='Number of Passengers')
    active = fields.Boolean(string='Active', default=True)
    
    @api.constrains('height_in_m', 'diameter_in_m')
    def _check_dimensions(self):
        for record in self:
            if record.diameter_in_m > record.height_in_m:
                raise UserError('Height must be greater than diameter.')