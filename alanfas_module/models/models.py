# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError, ValidationError


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    anfas_cost = fields.Float(string="التكلفه",  required=False, )

    @api.onchange('anfas_cost' )
    def onchange_anfas_cost(self):
        if self.amount_total != 0:
            cost1 = self.anfas_cost/self.amount_total
            for rec in self.order_line:
                if cost1 != 0 :
                    rec.price_unit = rec.price_unit * cost1 +rec.price_unit
                # else:
                #     rec.price_unit = rec.product_id.lst_price



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    real_price_unit = fields.Float('Real Unit Price', required=True, digits='Product Price', default=0.0)

    @api.onchange('product_id')
    def onchange_method(self):
        self.price_unit = self.product_id.lst_price
        self.real_price_unit = self.product_id.lst_price
class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"
    anfas_cost = fields.Float(string="التكلفه", required=False,)


    @api.onchange('anfas_cost')
    def onchange_anfas_cost(self):
        if self.amount_total != 0:
            cost1 = self.anfas_cost/self.amount_total
            for rec in self.order_line:
                if cost1 != 0 :
                    rec.price_unit = rec.price_unit*cost1 +rec.price_unit
                # else:
                #     rec.price_unit = rec.product_id.standard_price

class SaleOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    real_price_unit = fields.Float('Real Unit Price', required=True, digits='Product Price', default=0.0)

    @api.onchange('product_id')
    def onchange_method(self):
        self.price_unit = self.product_id.lst_price
        self.real_price_unit = self.product_id.standard_price

# class AccountMoveInherit(models.Model):
#
#     _inherit = 'account.move'
#
#     driver_name = fields.Char(string="اسم السائق", required=False, )
#     car_number = fields.Integer(string="رقم السياره", required=False, )
#     customer_phone = fields.Integer(string="رقم هاتف الزبون", required=False, )
#     customer_adress = fields.Char(string="عنوان الزبون", required=False, )
