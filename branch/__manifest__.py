{
    'name': 'Branch1',
    'version': '14.0.1.0',
    'category': 'Sales',
    'summary': 'Multiple Branch/Unit Operation on Sales,Purchases,Accounting/Invoicing,HR '
               'Accounting Reports for single company',
    'author': 'ahmed khalil',
    'company': 'Appsmatic',
    'website': 'http://www.appsmatic.net',

    'description': "",
    'depends': ['base','hr'],
    'data': [
        'security/branch_security.xml',
        'security/ir.model.access.csv',
        'views/branch_view.xml',
        'views/hr_employee.xml',

    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
