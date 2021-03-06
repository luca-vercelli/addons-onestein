# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Cost Spread',
    'summary': 'Cost spreading over a custom period',
    'version': '10.0.1.0.0',
    'author': 'Onestein',
    'license': 'AGPL-3',
    'website': 'http://www.onestein.eu',
    'images': [],
    'category': 'Accounting',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice_line.xml',
        'views/account_invoice.xml',
        'views/account_config_settings.xml',
        'data/spread_cron.xml',
    ],
    'installable': True,
}
