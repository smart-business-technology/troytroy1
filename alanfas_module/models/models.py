# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError, ValidationError

class delivaryDate(models.Model):
    _name = 'dilvevery.date'
    delevery_date = fields.Date(string="تاريخ التسليم", required=False, )
    product_id_1 = fields.Many2one('product.product', "Product")
    qty = fields.Integer('Qty')
    sale_id = fields.Many2one(comodel_name="sale.order", string="sale", required=False, )
    po_id = fields.Many2one(comodel_name="purchase.order", string="PO", required=False, )

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    anfas_cost = fields.Float(string="التكلفه",  required=False, )
    delevery_date = fields.One2many(comodel_name="dilvevery.date", inverse_name="sale_id", string="", required=False, )
    driver_name = fields.Char(string="اسم السائق", required=False, )
    car_number = fields.Integer(string="رقم السياره", required=False, )
    customer_phone = fields.Integer(string="رقم هاتف الزبون", required=False, )
    customer_adress = fields.Integer(string="عنوان الزبون", required=False, )

    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

        invoice_vals = {
            'ref': self.client_order_ref or '',
            'move_type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'delevery_date': self.delevery_date,
            'anfas_cost': self.anfas_cost,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
            'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'payment_reference': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
        }
        return invoice_vals

    @api.onchange('anfas_cost' )
    def onchange_anfas_cost(self):
        if self.amount_total != 0:
            cost1 = self.anfas_cost/self.amount_total
            for rec in self.order_line:
                if cost1 != 0 :
                    rec.price_unit = rec.price_unit * cost1 +rec.price_unit
                # else:
                #     rec.price_unit = rec.product_id.lst_price



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    real_price_unit = fields.Float('Real Unit Price', required=True, digits='Product Price', default=0.0)

    @api.onchange('product_id')
    def onchange_method(self):
        self.price_unit = self.product_id.lst_price
        self.real_price_unit = self.product_id.lst_price
class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"
    anfas_cost = fields.Float(string="التكلفه", required=False,)
    total_real_cost = fields.Float(string="Total Real price", required=False, compute="_compute_total_real_cost")

    delevery_date = fields.One2many(comodel_name="dilvevery.date", inverse_name="po_id", string="", required=False, )

    def _compute_total_real_cost(self):
        for rec in self :
            sum = 0
            for i in rec.order_line :
                sum+=(i.real_price_unit*i.product_qty)
            rec.total_real_cost = sum


    def _prepare_invoice(self):
        """Prepare the dict of values to create the new invoice for a purchase order.
        """
        self.ensure_one()
        move_type = self._context.get('default_move_type', 'in_invoice')
        journal = self.env['account.move'].with_context(default_move_type=move_type)._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting purchase journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

        partner_invoice_id = self.partner_id.address_get(['invoice'])['invoice']
        invoice_vals = {
            'ref': self.partner_ref or '',
            'move_type': move_type,
            'narration': self.notes,
            'currency_id': self.currency_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'partner_id': partner_invoice_id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(partner_invoice_id)).id,
            'payment_reference': self.partner_ref or '',
            'partner_bank_id': self.partner_id.bank_ids[:1].id,
            'invoice_origin': self.name,
            'anfas_cost': self.anfas_cost,
            'total_real_cost': self.total_real_cost,
            'delevery_date': self.delevery_date,
            'invoice_payment_term_id': self.payment_term_id.id,
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
        }
        return invoice_vals

    @api.onchange('anfas_cost')
    def onchange_anfas_cost(self):
        if self.amount_total != 0:
            cost1 = self.anfas_cost/self.amount_total
            for rec in self.order_line:
                if cost1 != 0 :
                    rec.price_unit = rec.price_unit*cost1 +rec.price_unit
                # else:
                rec.real_price_unit = rec.product_id.standard_price

class SaleOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    real_price_unit = fields.Float('Real Unit Price', required=True, digits='Product Price', default=0.0)

    @api.onchange('product_id')
    def onchange_method(self):
        self.price_unit = self.product_id.lst_price
        self.real_price_unit = self.product_id.standard_price
    def _prepare_account_move_line(self, move=False):
        self.ensure_one()
        res = {
            'display_type': self.display_type,
            'sequence': self.sequence,
            'name': '%s: %s' % (self.order_id.name, self.name),
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom.id,
            'quantity': self.qty_to_invoice,
            'price_unit': self.price_unit,
            'real_price_unit': self.real_price_unit,

            'tax_ids': [(6, 0, self.taxes_id.ids)],
            'analytic_account_id': self.account_analytic_id.id,
            'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
            'purchase_line_id': self.id,
        }
        if not move:
            return res

        if self.currency_id == move.company_id.currency_id:
            currency = False
        else:
            currency = move.currency_id

        res.update({
            'move_id': move.id,
            'currency_id': currency and currency.id or False,
            'date_maturity': move.invoice_date_due,
            'partner_id': move.partner_id.id,
        })
        return res



class AccountMoveInherit(models.Model):

    _inherit = 'account.move'

    driver_name = fields.Char(string="اسم السائق", required=False, )
    car_number = fields.Integer(string="رقم السياره", required=False, )
    customer_phone = fields.Integer(string="رقم هاتف الزبون", required=False, )
    customer_adress = fields.Char(string="عنوان الزبون", required=False, )


