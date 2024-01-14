# -*- coding: utf-8 -*-
{
    'name': "KTT Project",
    'summary': """
        KTT Project module.
    """,
    'description': """""",
    'author': "KTT Teams",
    'website': "https://kkt.io.vn",
    "license": "LGPL-3",
    'category': 'KTT/KTT',
    'version': '0.1',

    # DEPENDS MODULES
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # ============================================================================================================
        # DATA
        # ============================================================================================================
        # SECURITY SETTING - GROUP - PROFILE

        # ============================================================================================================
        # WIZARD
        # ============================================================================================================
        # VIEWS
        'views/project_task_views.xml',
        'views/project_project_views.xml',
        # ============================================================================================================
        # REPORT
        # ============================================================================================================
        # MENU - ACTION
        # ============================================================================================================
        # FUNCTION USE TO UPDATE DATA LIKE POST OBJECT
        # ============================================================================================================
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
}