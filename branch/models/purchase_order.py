# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools.float_utils import float_is_zero, float_compare
from odoo.exceptions import UserError

class purchase_order(models.Model):
    _inherit = 'purchase.order'
    branch_id = fields.Many2one('res.branch', 'Branch')


    @api.model
    def _get_purchase_default_branch(self):
        user_obj = self.env['res.users']
        branch_id = user_obj.browse(self.env.user.id).branch_id.id
        return branch_id
