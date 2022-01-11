# -*- coding: utf-8 -*-
# from odoo import http


# class AttendaceSheetReport(http.Controller):
#     @http.route('/attendace_sheet_report/attendace_sheet_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/attendace_sheet_report/attendace_sheet_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('attendace_sheet_report.listing', {
#             'root': '/attendace_sheet_report/attendace_sheet_report',
#             'objects': http.request.env['attendace_sheet_report.attendace_sheet_report'].search([]),
#         })

#     @http.route('/attendace_sheet_report/attendace_sheet_report/objects/<model("attendace_sheet_report.attendace_sheet_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attendace_sheet_report.object', {
#             'object': obj
#         })
