# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class res_branch(models.Model):
    _name = 'res.branch'

    name = fields.Char('Name', required=True)
    address = fields.Text('Address', size=252)
    telephone_no = fields.Char("Telephone No")
    # company_id = fields.Many2one('res.company', string='Company', required=True,readonly=True, index=True,
    #                              default=lambda self: self.env.user.company_id,
    #                              help="Company")

class res_users(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one('res.branch', 'Branch')
