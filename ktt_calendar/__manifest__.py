# -*- coding: utf-8 -*-
{
    'name': "KTT Calendar",
    'summary': """
        KTT Calendar module.
    """,
    'description': """""",
    'author': "KTT Teams",
    'website': "https://kkt.io.vn",
    "license": "LGPL-3",
    'category': 'KTT/KTT',
    'version': '0.1',

    # DEPENDS MODULES
    'depends': ['base', 'calendar', 'ktt_project'],

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
        'views/calendar_event_views.xml',
        'views/project_task_views.xml',
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
    'assets': {
        'web.assets_backend': [
            'ktt_calendar/static/src/style.css',
        ]
    }
}
