# -*- coding: utf-8 -*-
{
    'name': "Purchase Request Transfer",

    'summary': """
        Make Inter company transfer from purchase request """,

    'description': """
        - Make Inter company transfer from purchase request.

    """,

    'author': "Sejal Patel",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'license':'OPL-1',
    'category': 'purchase',
    'version': '13.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase_request', 'Inter-Entreprise_odoo13'],

    # always loaded
    'data': [
        'data/mail_data.xml',
        'views/purchase_request_view.xml',
    ],
    'external_dependencies': {
    },
    
    # "images": ['static/description/background.jpg'],
    'installable': True,
}