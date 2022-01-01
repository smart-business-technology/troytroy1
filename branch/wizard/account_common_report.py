# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class AccountCommonReport(models.TransientModel):
    _inherit = "account.common.report"

    branch_ids = fields.Many2one('res.branch', string='Branch')
                                          
    def _build_contexts(self, data):
        result = {}
        data['form']['branch_ids'] = self.read(['branch_ids'])[0]
        result['branch_ids'] = \
            'branch_ids' in data['form'] \
            and data['form']['branch_ids'] or False
        branch_name_long = ''
        if result['branch_ids'].get('branch_ids'):
                branch_name = self.env['res.branch'].browse(result['branch_ids'].get('branch_ids')[0]).name
                branch_name_long += branch_name  
        result['branch_ids'] = branch_name_long
        result['journal_ids'] = 'journal_ids' in data['form'] and data['form']['journal_ids'] or False
        result['state'] = 'target_move' in data['form'] and data['form']['target_move'] or ''
        result['date_from'] = data['form']['date_from'] or False
        result['date_to'] = data['form']['date_to'] or False
        result['strict_range'] = True if result['date_from'] else False
        return result









