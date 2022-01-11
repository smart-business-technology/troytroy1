# -*- coding: utf-8 -*-
{
    'name': "Attendance Report",

    'summary': """
        Print Attendance Report for Employees""",

    'description': """
        This app helps you to print the attendances(Present and Absent Days) in PDF, based on Employees Calendar Resources.
    """,

    'author': "Prabakaran R",
    'website': "https://www.linkedin.com/in/prabakaran-r",
    'category': 'Employees',
    'version': '12.0.1',
    'depends': ['base', 'hr_attendance'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/report_views.xml',
    ],
    "application": True,
    "installable": True,
}
