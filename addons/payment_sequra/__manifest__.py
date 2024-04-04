# -*- coding: utf-8 -*-
{
    'name': "payment_sequra",

    'summary': "Allow payments with Sequra payment methods,

    'description': """
Allow payments with Sequra payment methods.
    """,

    'author': "seQura",
    'website': "https://sequra.es",

    'category': 'Payments',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['payment'],

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

