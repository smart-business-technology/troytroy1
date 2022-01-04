# -*- coding: utf-8 -*-

from odoo import models, fields, api


class invoice_fields(models.Model):
    _inherit = 'account.move'


    driver_name = fields.Char("Driver Name")
    anfas_cost = fields.Float(string="التكلفه", required=False, )

    # carpenter_name = fields.Char("Carpenter Name")
    carpenter_name = fields.Many2one(comodel_name="res.partner", string="Carpenter Name", required=False, )
    total_real_cost = fields.Float(string="Total Real price", required=False,)

    # driver_name = fields.Char(string="اسم السائق", required=False, )
    car_number = fields.Integer(string="رقم السياره", required=False, )
    customer_phone = fields.Integer(string="رقم هاتف الزبون", required=False, )
    customer_adress = fields.Char(string="عنوان الزبون", required=False, )
    delevery_date = fields.One2many(comodel_name="dilvevery.date", inverse_name="account_id", string="", required=False, )


class AccountMoveLineInherit(models.Model):

    _inherit = 'account.move.line'
    real_price_unit = fields.Float('Real Unit Price', required=True, digits='Product Price', default=0.0)

class delivaryDate(models.Model):
    _inherit = 'dilvevery.date'
    account_id = fields.Many2one(comodel_name="account.move", string="sale", required=False, )
