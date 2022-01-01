# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceFields(http.Controller):
#     @http.route('/invoice_fields/invoice_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_fields/invoice_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_fields.listing', {
#             'root': '/invoice_fields/invoice_fields',
#             'objects': http.request.env['invoice_fields.invoice_fields'].search([]),
#         })

#     @http.route('/invoice_fields/invoice_fields/objects/<model("invoice_fields.invoice_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_fields.object', {
#             'object': obj
#         })
