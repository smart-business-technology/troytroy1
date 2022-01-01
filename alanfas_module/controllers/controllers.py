# -*- coding: utf-8 -*-
# from odoo import http


# class AlanfasModule(http.Controller):
#     @http.route('/alanfas_module/alanfas_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alanfas_module/alanfas_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alanfas_module.listing', {
#             'root': '/alanfas_module/alanfas_module',
#             'objects': http.request.env['alanfas_module.alanfas_module'].search([]),
#         })

#     @http.route('/alanfas_module/alanfas_module/objects/<model("alanfas_module.alanfas_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alanfas_module.object', {
#             'object': obj
#         })
