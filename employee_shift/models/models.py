# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NewModddule(models.Model):

    _inherit = 'resource.calendar.attendance'

    @api.onchange('hour_from', 'hour_to')
    def _onchange_hours(self):

        # avoid negative or after midnight
        for rec in self :
            if rec.hour_to<rec.hour_from or rec.hour_to>24.00 :
                if rec.hour_to>=3.0:
                    rec.hour_to=3.00

        # self.hour_from = min(self.hour_from, 23.99)
        # self.hour_from = max(self.hour_from, 0.0)
        # self.hour_to = min(self.hour_to, 23.99)
        # self.hour_to = max(self.hour_to, 0.0)
        #
        # # avoid wrong order
        # self.hour_to = max(self.hour_to, self.hour_from)
class NewModdduele(models.Model):

    _inherit = 'resource.calendar'
    
    def _calculate_hours_per_week(self):
        self.ensure_one()
        attendances = self.attendance_ids.filtered(lambda r: not r.date_from and not r.date_to)
        hour_count = 0.0
        for attendance in attendances:
            hour_count += attendance.hour_to - attendance.hour_from

        return abs(hour_count)

    @api.onchange('attendance_ids', 'two_weeks_calendar')
    def _onchange_hours_per_day(self):
        attendances = self._get_global_attendances()
        self.hours_per_day = abs(self._compute_hours_per_day(attendances))

    def _check_overlap(self, attendance_ids):
        """ attendance_ids correspond to attendance of a week,
            will check for each day of week that there are no superimpose. """
        result = []
        for attendance in attendance_ids.filtered(lambda att: not att.date_from and not att.date_to):
            # 0.000001 is added to each start hour to avoid to detect two contiguous intervals as superimposing.
            # Indeed Intervals function will join 2 intervals with the start and stop hour corresponding.
            result.append((int(attendance.dayofweek) * 24 + attendance.hour_from + 0.000001, int(attendance.dayofweek) * 24 + attendance.hour_to, attendance))
        #
        # if len(Intervals(result)) != len(result):
        #     raise ValidationError(_("Attendances can't overlap."))

