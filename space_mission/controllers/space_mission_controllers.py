# -*- coding: utf-8 -*-

from odoo import http


class SpaceMission(http.Controller):
    @http.route('/space_mission', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/space_mission/missions', auth='public', website=True)
    def missions(self, **kw):
        missions = http.request.env['space_mission.mission'].search([])
        return http.request.render('space_mission.missions_website', {
            'missions': missions,
        })
    
    @http.route('/space_mission/<model("space_mission.mission"):mission>/', auth='public', website=True)
    def mission(self, mission):
        return http.request.render('space_mission.mission_website', {
            'mission': mission,
        })