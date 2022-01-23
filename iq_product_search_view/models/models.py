# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class iq_product_search_view(models.Model):
#     _name = 'iq_product_search_view.iq_product_search_view'
#     _description = 'iq_product_search_view.iq_product_search_view'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
