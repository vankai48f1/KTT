# -*- coding: utf-8 -*-
# from odoo import http


# class KttProject(http.Controller):
#     @http.route('/ktt_project/ktt_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ktt_project/ktt_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ktt_project.listing', {
#             'root': '/ktt_project/ktt_project',
#             'objects': http.request.env['ktt_project.ktt_project'].search([]),
#         })

#     @http.route('/ktt_project/ktt_project/objects/<model("ktt_project.ktt_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ktt_project.object', {
#             'object': obj
#         })

