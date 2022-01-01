# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class pos_session(models.Model):
    _inherit = 'pos.session'

    branch_id = fields.Many2one('res.branch', 'Branch')

class pos_order(models.Model):
    _inherit = 'pos.order'

    branch_id = fields.Many2one('res.branch', 'Branch')

class pos_config(models.Model):
    _inherit = 'pos.config'
    branch_id = fields.Many2one('res.branch', 'Branch')

