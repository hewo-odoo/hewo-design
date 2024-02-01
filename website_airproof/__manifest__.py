{
    'name': 'custom-rene',
    'version': '16.0.0',
    'description': '',
    'summary': '',
    'author': 'Odoo PS',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Website/Theme',
    'depends': [
        'website', 'website_sale'
    ],
    'data': [
        'data/presets.xml',
        'data/images.xml',
        'data/menu.xml',
        'data/shapes.xml',
        'data/pages/aboutus.xml',
        'data/pages/contactus.xml',
        'data/pages/home.xml',
        'views/website_templates.xml',
        'views/snippets/options.xml'
    ],
    'demo': [
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        'web._assets_primary_variables': [
            'website_airproof/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss')
        ],
        'web.assets_frontend': [
            'website_airproof/static/src/scss/font.scss'
        ],
    },
}