from odoo import models, fields


class AwardType(models.Model):
    _name = "employee.punish.type"
    _description = "Employee punish Type"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")


class Award(models.Model):
    _name = "employee.punish"
    _description = "Employee punish"

    name = fields.Char(string="Name")
    employee_id = fields.Many2one("hr.employee", string="Employee")
    date = fields.Date(string="Date")
    ttype = fields.Many2one('employee.punish.type', string="نوع العقوبه")
    amount = fields.Float(string="Amount")
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company',
                                 default=lambda self: self.employee_id.company_id)
    currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')
class punishtype(models.Model):
    _name = "employee.punish.type"
    name = fields.Char(string="Name")
