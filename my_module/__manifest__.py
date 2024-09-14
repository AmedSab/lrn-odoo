# -*- coding: utf-8 -*-
{
    'name': "my_module",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "test",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale',
                'account', 'mail',
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/base_menu.xml',
        'views/my_model_view.xml',
        'views/my_second_model_view.xml',
        'views/sale_order_view.xml',
        'reports/my_model_report.xml',
    ],
    'assets': {
        'web.assets_backend': ['my_module\static\src\css\my_model.css']
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}



