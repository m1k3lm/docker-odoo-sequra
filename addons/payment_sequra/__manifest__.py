# -*- coding: utf-8 -*-
{
    'name': "payment_sequra",

    'summary': "Allow payments with Sequra payment methods",

    'description': """
Allow payments with Sequra payment methods.
    """,

    'author': "seQura",
    'website': "https://sequra.es",

    'category': 'Accounting/Payment Providers',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['payment'],

    # always loaded
    'data': [
        'views/payment_sequra_templates.xml',
        'data/payment_provider_data.xml',
        'views/payment_provider_views.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
}

