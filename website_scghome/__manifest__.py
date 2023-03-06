{
    'name': 'SCG home Theme',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'author': 'Odoo PS',
    'depends': ['website_sale', 'website_blog'],
    'license': 'OEEL-1',
    'data': [
        # Options
        'data/presets.xml',
        # Menu
        'data/menu.xml',
        # Images
        'data/images.xml',
        # Blog
        'data/website_blog.xml',
        # Pages
        'data/pages/home.xml',
        'data/pages/contactus.xml',
        'data/pages/service_solutions.xml',
        'data/pages/maintenance.xml',
        # Frontend
        'views/website_template.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_scghome/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website_scghome/static/src/scss/bootstrap_overridden.scss'),
        ],
    },
}
