# -*- coding: utf-8 -*-
# from odoo import http


# class KttCalendarEvent(http.Controller):
#     @http.route('/ktt_calendar_event/ktt_calendar_event', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ktt_calendar_event/ktt_calendar_event/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ktt_calendar_event.listing', {
#             'root': '/ktt_calendar_event/ktt_calendar_event',
#             'objects': http.request.env['ktt_calendar_event.ktt_calendar_event'].search([]),
#         })

#     @http.route('/ktt_calendar_event/ktt_calendar_event/objects/<model("ktt_calendar_event.ktt_calendar_event"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ktt_calendar_event.object', {
#             'object': obj
#         })

