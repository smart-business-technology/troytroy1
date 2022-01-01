# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo.tools.safe_eval import safe_eval
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountJournal(models.Model):
    _inherit = 'account.journal'
    branch_id = fields.Many2one('res.branch', 'Branch')


class ResourceCalendarAttendance1(models.Model):
    _inherit = "resource.calendar.attendance"
    _description = "Work Detail"
    @api.onchange('hour_from', 'hour_to')
    def _onchange_hours(self):
        print('sssssssssssssssss')
        # avoid negative or after midnight
        # self.hour_from = min(self.hour_from, 23.99)
        self.hour_from = max(self.hour_from, 0.0)
        # self.hour_to = min(self.hour_to, 23.99)
        self.hour_to = max(self.hour_to, 0.0)
        # avoid wrong order
        self.hour_to = max(self.hour_to, self.hour_from)




class account_move(models.Model):
    _inherit = 'account.move'
    branch_id = fields.Many2one('res.branch', 'Branch', )


class account_move_line(models.Model):
    _inherit = 'account.move.line'
    branch_id = fields.Many2one('res.branch', 'Branch', )


class AccountPayment(models.Model):
    _inherit = "account.payment"
    branch_id = fields.Many2one('res.branch', string='Branch', )
