# -*- coding: utf-8 -*-
from odoo import http

# class Siimsa(http.Controller):
#     @http.route('/siimsa/siimsa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siimsa/siimsa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siimsa.listing', {
#             'root': '/siimsa/siimsa',
#             'objects': http.request.env['siimsa.siimsa'].search([]),
#         })

#     @http.route('/siimsa/siimsa/objects/<model("siimsa.siimsa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siimsa.object', {
#             'object': obj
#         })