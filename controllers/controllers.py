# -*- coding: utf-8 -*-
from odoo import http

# class Odoocalc(http.Controller):
#     @http.route('/odoocalc/odoocalc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoocalc/odoocalc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoocalc.listing', {
#             'root': '/odoocalc/odoocalc',
#             'objects': http.request.env['odoocalc.odoocalc'].search([]),
#         })

#     @http.route('/odoocalc/odoocalc/objects/<model("odoocalc.odoocalc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoocalc.object', {
#             'object': obj
#         })