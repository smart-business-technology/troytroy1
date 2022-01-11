from odoo import models, fields, api
class HrDepartureWizardemployee(models.TransientModel):
    _inherit = 'hr.departure.wizard'

    departure_reason = fields.Selection([
        ('fired', 'Fired'),
        ('resigned', 'Resigned'),
        ('retired', 'Retired'),
        ('termination', 'Termination'),
        ('leave_work', 'Leave Work'),
        ('open_vacation', 'Open Vacation')

    ], string="Departure Reason", default="fired")