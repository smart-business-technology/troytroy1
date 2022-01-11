# -*- coding: utf-8 -*-
import base64
from io import BytesIO
from odoo import fields, models,_
from odoo.tools.misc import xlwt
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang
from odoo.exceptions import ValidationError


class Expense(models.Model):
    _name = 'expense.expense'
    _rec_name = 'name'
    _description = 'New Description'
    purchase_id = fields.Many2one(comodel_name="purchase.order", string="", required=False, )
    name = fields.Char("Name")
    amount = fields.Float(string="Amount",  required=False, )

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    account_debit_id = fields.Many2one('account.account', string="Account Debit")
    account_credit_id = fields.Many2one('account.account', string="Account Credit")
    journal_entry_id = fields.Many2one('account.move',string="Journal Entry",readonly="1", copy=False)
    journal_id = fields.Many2one('account.journal', string='Journal', required=True,domain=[('type', 'in', ('bank', 'cash'))])
    def Create_Journal(self):
        sum=0
        for rec in self.expense_expense_ids:
            sum+=rec.amount
        if self.expense_expense_ids and self.account_credit_id and self.account_debit_id and self.journal_id :
            new_account_move = self.env['account.move'].create({
                'journal_id': self.journal_id.id,
                'date': fields.Datetime.now(),
                'move_type': 'entry',
                'line_ids': [
                    (0, 0, {
                        # 'partner_id': self.partner_id.id,
                        'account_id': self.account_debit_id.id,
                        'debit': sum,
                        'credit': 0,
                        'date': fields.Datetime.now(),
                    }),
                    (0, 0, {
                        # 'partner_id': self.partner_id.id if self.partner_id else False,
                        'account_id': self.account_credit_id.id,
                        'debit': 0,
                        'credit': sum,
                        'date': fields.Datetime.now(),
                    })
                ],
            })
            print(new_account_move)
            self.journal_entry_id = new_account_move.id
        else:
            raise ValidationError(_("Please fill  the records"))

    expense_expense_ids = fields.One2many(comodel_name="expense.expense", inverse_name="purchase_id", string="", required=False, )

    def export_purchase_order_in_excel(self):
        active_ids = self.env.context.get('active_ids')
        order_ids = self.env['purchase.order'].search([('id', 'in', active_ids)])

        workbook = xlwt.Workbook(encoding="UTF-8")
        filename = 'Pedido_compra' + '.xls'
        for order_id in order_ids:
            currency_id = order_id.currency_id
            worksheet = workbook.add_sheet(order_id.name)
            worksheet.col(0).width = 4500
            worksheet.col(1).width = 7000
            worksheet.col(2).width = 5500
            worksheet.col(3).width = 4500
            worksheet.col(4).width = 4500
            worksheet.col(5).width = 4500
            worksheet.row(2).height = 400

            bold = xlwt.easyxf("font: bold 1;")
            align_right = xlwt.easyxf("align: horiz right;")
            style = xlwt.easyxf('font: bold 1,height 240;')
            if order_id.state == 'draft':
                worksheet.write(2, 2, 'Request for Quotation', style)
            else:
                worksheet.write(2, 2, 'Purchase Order', style)
            worksheet.write(2, 3, order_id.name)

            worksheet.write(4, 0, 'Vendor:', bold)
            partner = order_id.partner_id
            row = 4
            worksheet.write(row, 1, partner.name)
            if partner.street:
                row += 1
                worksheet.write(row, 1, partner.street)
            if partner.street2:
                row += 1
                worksheet.write(row, 1, partner.street2)
            if partner.city or partner.state_id or partner.zip:
                address = ''
                if partner.city:
                    address = partner.city + ' '
                if partner.state_id:
                    address = address + partner.state_id.name + ' '
                if partner.zip:
                    address = address + partner.zip
                row += 1
                worksheet.write(row, 1, address)
            if partner.country_id:
                row += 1
                worksheet.write(row, 1, partner.country_id.name)
                worksheet.write(4, 4, 'Order Date:', bold)
            worksheet.write_merge(4, 4, 5, 6, order_id.date_order.strftime(DEFAULT_SERVER_DATETIME_FORMAT))
            worksheet.write(5, 4, 'Your Order Reference', bold)
            if order_id.partner_ref:
                worksheet.write(5, 5, order_id.partner_ref)
            row += 3
            worksheet.write(row, 0, 'Code', bold)
            worksheet.write(row, 1, 'Product', bold)
            worksheet.write(row, 2, 'Description', bold)
            worksheet.write(row, 3, 'Date Req.', bold)
            worksheet.write(row, 4, 'Qty', bold)
            worksheet.write(row, 5, 'Rec. Qty', bold)
            worksheet.write(row, 6, 'Unit Price', bold)
            worksheet.write(row, 7, 'Taxes', bold)
            worksheet.write(row, 8, 'Net Price', bold)
            for line in order_id.order_line:
                row += 1
                worksheet.write(row, 0, line.product_id.default_code)
                worksheet.write(row, 1, line.product_id.name)
                worksheet.write(row, 2, line.name)
                worksheet.write(row, 3, line.date_planned.strftime(DEFAULT_SERVER_DATETIME_FORMAT))
                worksheet.write(row, 4, line.product_qty)
                worksheet.write(row, 5, line.qty_received)
                worksheet.write(row, 6, line.price_unit)
                worksheet.write(row, 7, ', '.join(map(lambda x: x.name, line.taxes_id)))
                worksheet.write(row, 8, formatLang(self.env, line.price_subtotal, currency_obj=currency_id), align_right)
            row += 2
            worksheet.write(row, 7, 'Total Without Taxes', bold)
            worksheet.write(row, 8, formatLang(self.env, order_id.amount_untaxed, currency_obj=currency_id), align_right)
            row += 1
            worksheet.write(row, 7, 'Taxes', bold)
            worksheet.write(row, 8, formatLang(self.env, order_id.amount_tax, currency_obj=currency_id), align_right)
            row += 1
            worksheet.write(row, 7, 'Total', bold)
            worksheet.write(row, 8, formatLang(self.env, order_id.amount_total, currency_obj=currency_id), align_right)

            row += 2
            worksheet.write(row, 0, order_id.notes)
        fp = BytesIO()
        workbook.save(fp)

        po_excel_report_id = self.env['purchase.order.excel.report'].create(
            {'excel_file': base64.encodestring(fp.getvalue()), 'file_name': filename})
        fp.close()

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/binary/download_po_excel_report/%s' % (po_excel_report_id.id),
            'target': 'new',
        }


class PurchseOrderExcelReport(models.TransientModel):
    _name = "purchase.order.excel.report"
    _description = "Purchase Order Excel Report"

    excel_file = fields.Binary('Download Report :- ')
    file_name = fields.Char('Text File', size=64)
