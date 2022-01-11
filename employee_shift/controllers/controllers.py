# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeShift(http.Controller):
#     @http.route('/employee_shift/employee_shift/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_shift/employee_shift/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_shift.listing', {
#             'root': '/employee_shift/employee_shift',
#             'objects': http.request.env['employee_shift.employee_shift'].search([]),
#         })

#     @http.route('/employee_shift/employee_shift/objects/<model("employee_shift.employee_shift"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_shift.object', {
#             'object': obj
#         })
