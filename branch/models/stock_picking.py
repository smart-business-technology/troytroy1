from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare

class stock_picking(models.Model):
    _inherit='stock.picking'

    branch_id = fields.Many2one('res.branch','Branch')

class stock_move(models.Model):
    _inherit = 'stock.move'

    branch_id = fields.Many2one('res.branch','Branch')
