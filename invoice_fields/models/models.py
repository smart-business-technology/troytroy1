# -*- coding: utf-8 -*-

from odoo import models, fields, api


class invoice_fields(models.Model):
    _inherit = 'account.move'


    driver_name = fields.Char("Driver Name")
    # carpenter_name = fields.Char("Carpenter Name")
    carpenter_name = fields.Many2one(comodel_name="res.partner", string="Carpenter Name", required=False, )
