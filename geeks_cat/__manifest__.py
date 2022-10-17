# Copyright 2022 Oriol Piera
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Geeks Cat',
    'description': """
        Geeks.cat customizations""",
    'version': '13.0.0.0.6',
    'license': 'AGPL-3',
    'author': 'Oriol Piera',
    'website': 'https://oriolpiera.github.io/',
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner.xml',
        'wizard/wizard_assign_number_to_member_views.xml',
        'data/geeks_cat_data.xml',
    ],
    'demo': [
        'demo/res_partner.xml',
    ],
}
