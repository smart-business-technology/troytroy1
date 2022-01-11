# -*- coding: utf-8 -*-
# from odoo import http


# class ChiliTraining(http.Controller):
#     @http.route('/chili_training/chili_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chili_training/chili_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chili_training.listing', {
#             'root': '/chili_training/chili_training',
#             'objects': http.request.env['chili_training.chili_training'].search([]),
#         })

#     @http.route('/chili_training/chili_training/objects/<model("chili_training.chili_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chili_training.object', {
#             'object': obj
#         })
