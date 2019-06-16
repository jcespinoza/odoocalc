# -*- coding: utf-8 -*-
{
    'name': "odoocalc",

    'summary': """
        An awesome calculator to make Jimmy happy""",

    'description': """
        This thing hallows you to calculate everything you can think of,
        including the amount of time required to find the infinity stones.
    """,

    'author': "Juan Carlos Espinoza",
    'website': "https://www.jcespinoza.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Scientific',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}