{
    'name': 'Sakaya Theme',
    'category': 'Website/Theme',
    'version': '15.0.1.0.0',
    'author': 'Odoo PS',
    'depends': ['website_sale','website_sale_wishlist'],
    'license': 'OEEL-1',
    'data': [
        # Options
        'data/presets.xml',
        # Menu
        'data/menu.xml',
        # Images
        'data/images.xml',
        # Pages
        'data/pages/home.xml',
        'data/pages/aboutus.xml',
        'data/pages/termsconditions.xml',
        'data/pages/privacy.xml',
        'data/pages/shipping.xml',
        'data/pages/faq.xml',
        # Frontend
        'views/website_templates.xml',
        'views/website_sale_templates.xml'
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_sakaya/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            # SCSS
            'website_sakaya/static/src/scss/theme.scss',
        ],
         'web._assets_frontend_helpers': [
             ('prepend', 'website_sakaya/static/src/scss/bootstrap_overridden.scss'),
         ],
    },
    'cloc_exclude': [
        'static/src/scss/bootstrap_overridden.scss',
        'static/src/scss/primary_variables.scss',
        'views/website_templates.xml',
        'data/**/*',
    ],
}
