# -*- coding: utf-8 -*-
{
    'name': 'Tax Balance',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Añade balance de impuestos y posición fiscal legal',
    'author': 'Juandelsur5, OCA/Reporting-engine',
    'website': 'https://github.com/Juandelsur5/account_tax_balance',
    'depends': [
        'account',
        'date_range',  # Inyección crítica para eliminar el error de "Operación no válida"
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/open_tax_balances_view.xml',
        'views/account_move_view.xml',
        'views/account_tax_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
    'pre_init_hook': 'pre_init_hook',
}
