{
    'name': 'Motivos de Ausencia',
    'license': 'LGPL-3',
    'version': '17.0.0.0.1',
    'category': 'Human Resources',
    'summary': 'Clasifica ausencias por motivos personalizables',
    'description': 'Permite agregar motivos de ausencia personalizables al módulo de RRHH y permite reportes agrupados.',
    'author': 'andrea',
    'depends':['hr', 'hr_holidays'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hr_leave_reason_views.xml',
        'views/hr_leave_views.xml',
    ],
    'installable': True,
}
