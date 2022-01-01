# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Employee(models.Model):
    _inherit = 'hr.employee'

    branch_id = fields.Many2one('res.branch', 'Branch')
