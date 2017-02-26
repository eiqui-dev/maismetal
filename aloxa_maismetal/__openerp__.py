# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Solucións Aloxa S.L. <info@aloxa.eu>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
{
    'name': "mais_metal",

    'summary': """
        Opciones por defecto para maismetal""",

    'description': """
        Opciones por defecto para maismetal
    """,

    'author': "Solucions Aloxa S.L.",
    'website': "http://www.aloxa.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'eiqui.com',
    "icon": "/aloxa_maismetal/static/src/img/icon.png",    
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale',
                'purchase',
                'project',
                'stock',
                'hr',
                'hr_timesheet',
                'hr_timesheet_sheet',
                'sale_stock',
                'account_analytic_analysis',
                'report_qweb_element_page_visibility',
               ],

    # always loaded
    'data': [
        'views.xml',
        'data/data.xml',
        'data/res.groups.csv',
        'data/menus.xml',
        'views/maismetal_report_invoice.xml',
        'views/maismetal_report_saleorder.xml',
        'views/maismetal_report_picking_document.xml',
        'views/maismetal_report_picking.xml',
        'views/maismetal_report_saleorder_document.xml',
        'views/maismetal_report_invoice_document.xml',
        'views/maismetal_external_layout.xml',
        'views/maismetal_external_layout_footer.xml',
        'views/maismetal_external_layout_header.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}