from odoo import api, fields, models
from datetime import date, timedelta

class HrPayslipInherit(models.Model):

    _inherit = 'hr.payslip'

    def compute_sheet(self):
        summ=0
        summ1=0
        late_obj = self.env['late.check_in'].search(
            [('employee_id', '=', self.employee_id.id), ('date', '>=', self.date_from), ('date', '<=', self.date_to)])
        if late_obj:
            for recc in late_obj:
                summ += recc.late_minutes
        self.employee_id.latee = summ
        early_leave = self.env["hr.attendance"].search(
            [('employee_id', '=', self.employee_id.id), ('checkout_date', '>=', self.date_from),
             ('checkout_date', '<=', self.date_to)])

        print(early_leave)
        if early_leave:
            for recc in early_leave:
                summ1 += recc.early_check_out
        self.employee_id.early_leave = summ1

        absent = 0
        delta = self.date_to - self.date_from
        flag = False
        for i in range(delta.days + 1):

            day =  self.date_from + timedelta(days=i)

            attendances = self.env["hr.attendance"].search(
                [('employee_id', '=', self.employee_id.id), ('checkin_date', '=', day)])
            work_hours_sum = 0
            less_than7 = False
            if not attendances:
                absent+=1
            for att in attendances:
                if not att.check_out and  att.check_in:
                    absent +=1
                if not att.check_in and att.check_out:
                    absent +=1
                work_hours_sum += att.worked_hours
                if att.check_out:
                    flag = True

            if 8 >= work_hours_sum >= 7:
                less_than7 = True
            if attendances and flag:
                if less_than7:
                    absent += .5
            self.employee_id.days_latee=absent
        for payslip in self.filtered(lambda slip: slip.state in ['draft', 'verify']):
            number = payslip.number or self.env['ir.sequence'].next_by_code('salary.slip')
            # delete old payslip lines
            payslip.line_ids.unlink()
            lines = [(0, 0, line) for line in payslip._get_payslip_lines()]
            payslip.write({'line_ids': lines, 'number': number, 'state': 'verify', 'compute_date': fields.Date.today()})
        return True
