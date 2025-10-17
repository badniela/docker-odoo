from odoo import models, fields

class HrLeaveReason(models.Model):
    _name = 'hr.leave.reason'
    _description = 'Motivo de Ausencia'

    name = fields.Char(string='Motivo', required=True, help='Motivo de ausencia')
    description = fields.Text(string='Descripción', required=False, help='Descripción del motivo de ausencia')

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    reason_id = fields.Many2one('hr.leave.reason', string='Motivo de Ausencia', help='Motivo de la ausencia')

