# -*- coding: utf-8 -*-

from odoo import models, fields, api


class invoice_fields(models.Model):
    _inherit = 'account.move'


    driver_name = fields.Char("Driver Name")
    anfas_cost = fields.Float(string="التكلفه", required=False, )

    # carpenter_name = fields.Char("Carpenter Name")
    carpenter_name = fields.Many2one(comodel_name="res.partner", string="Carpenter Name", required=False, )
    total_real_cost = fields.Float(string="Total Real price", required=False,
                                   )
class AccountMoveLineInherit(models.Model):

    _inherit = 'account.move.line'
    real_price_unit = fields.Float('Real Unit Price', required=True, digits='Product Price', default=0.0)
