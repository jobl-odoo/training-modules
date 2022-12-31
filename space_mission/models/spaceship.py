# -*- coding: utf-8 -*-

from odoo import models, fields, api


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