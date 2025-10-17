from odoo.tests.common import TransactionCase
from odoo.tests import tagged, Form
import logging

_logger = logging.getLogger(__name__)

@tagged('hr_leave_reason', 'hr', 'hr_holidays')
class TestHrLeaveReason(TransactionCase):

    def setup(self):
        super().setUp()
    
    def test_01_create_reason_and_leave(self):
        reason = self.env['hr.leave.reason'].create({'name': 'Enfermedad'})
        employee = self.env.ref('hr.employee_admin')
        holiday_status = self.env.ref('hr_holidays.holiday_status_cl')

        # Crear asignación de días
        allocation = self.env['hr.leave.allocation'].create({
            'name': 'Asignación de prueba',
            'employee_id': employee.id,
            'holiday_status_id': holiday_status.id,
            'allocation_type': 'regular',
            'number_of_days': 5,
        })
        allocation.action_validate()  # Validar la asignación

        # Crear la solicitud de ausencia
        leave = self.env['hr.leave'].create({
            'name': 'Ausencia por gripe',
            'employee_id': employee.id,
            'holiday_status_id': holiday_status.id,
            'reason_id': reason.id,
            'request_date_from': '2025-10-20',
            'request_date_to': '2025-10-21',
        })

        self.assertEqual(leave.reason_id.name, 'Enfermedad')
        _logger.info("Test de creación de motivo y ausencia completado con éxito.")