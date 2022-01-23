# -*- coding: utf-8 -*-
# from odoo import http


# class IqProductSearchView(http.Controller):
#     @http.route('/iq_product_search_view/iq_product_search_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iq_product_search_view/iq_product_search_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iq_product_search_view.listing', {
#             'root': '/iq_product_search_view/iq_product_search_view',
#             'objects': http.request.env['iq_product_search_view.iq_product_search_view'].search([]),
#         })

#     @http.route('/iq_product_search_view/iq_product_search_view/objects/<model("iq_product_search_view.iq_product_search_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iq_product_search_view.object', {
#             'object': obj
#         })
