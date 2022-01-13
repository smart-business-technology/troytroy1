# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Transport(models.Model):
    _name = "hr.transport"
    _description = "transport"

    name = fields.Char(string="المسمي الوظيفي")
    date = fields.Date(string="Date")
    employee_id = fields.Many2one("hr.employee", string="Employee")


class Training(models.Model):
    _name = "hr.training"
    _description = "Training"

    name = fields.Char(string="Name")
    from_date = fields.Date(string="From Date")
    course_subject = fields.Char(string="Course Subject")
    to_date = fields.Date(string="To Date")
    status = fields.Selection([('start', 'To Start'),
                               ('running', 'Running'),
                               ('hold', 'Hold'),
                               ('cancel', 'Cancel'),
                               ('Done', 'Done')], default='start',
                              string="Status")
    employee_ids = fields.One2many('employee.training','hr_training_id', string="Employee")
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company',
                                 default=lambda self: self.env.user.company_id)



class EmployeeTraining(models.Model):
    _name = "employee.training"
    _description = "Employee Training"

    name = fields.Char(string=" Course Name")
    employee_id = fields.Many2one("hr.employee", string="Employee")
    hr_training_id = fields.Many2one("hr.training", string="Training Program")
    result = fields.Char(string='Result')
    from_date = fields.Date(string="From Date")
    course_subject = fields.Char(string="Course Subject", related='hr_training_id.course_subject')
    to_date = fields.Date(string="To Date")
    status = fields.Selection([('start', 'To Start'),
                               ('running', 'Running'),
                               ('hold', 'Hold'),
                               ('cancel', 'Cancel'),
                               ('Done', 'Done')], default='start',
                              string="Status")
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company',
                                 default=lambda self: self.env.user.company_id)


class HREmployee(models.Model):
    _inherit = 'hr.employee'


    punish_ids = fields.One2many("employee.punish", "employee_id", string="العقويات")
    reward_ids = fields.One2many("employee.reward", "employee_id", string="العقويات")
    training_ids = fields.One2many("employee.training", "employee_id", string="Training")
    zmm_ids = fields.One2many("hr.zmm", "employee_id", string="Training")
    transport_ids = fields.One2many("hr.transport", "employee_id", string="التنقلات")

    latee = fields.Float(string="التاخير",  required=False, )
    early_leave = fields.Float(string="الرحيل المبكر ",  required=False, )
    days_latee = fields.Float(string="ايام الغياب",  required=False, )
    pre_job = fields.Char(string="Previous Job ", required=False, )



class HrZmm(models.Model):
    _name = 'hr.zmm'
    name = fields.Char("الاسم")
    note = fields.Char("الملاحظات")
    date = fields.Date(string="تاريخ الاستلام", required=False, )
    amount = fields.Float(string=" القيمه",  required=False, )
    employee_id = fields.Many2one("hr.employee", string="Employee")
