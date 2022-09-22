{
    'name': 'Helena Theme',
    'summary': '',
    'description': '',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website'],
    'license': 'OEEL-1',
    'data': [
        # Options
        'data/presets.xml',
        # Menu
         'data/menu.xml',
        # Images
        'data/images.xml',
        'data/shapes.xml',
        # Pages
        'data/pages/aboutus.xml',
        'data/pages/contactus.xml',
        'data/pages/home.xml',
        # Snippets
        'views/snippets/options.xml',
        # Frontend
        #'views/website_templates.xml',
        # Backend

        # Header
        'views/header.xml',

        # Footer
        'views/footer.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_helena/static/src/scss/primary_variables.scss',
        ],
        # 'web._assets_frontend_helpers': [
        #     ('prepend', 'website_helena/static/src/scss/bootstrap_overridden.scss'),
        # ],
        'web.assets_frontend': [
            # SCSS
            #'website_helena/static/src/scss/helpers.scss',
            'website_helena/static/src/scss/theme.scss',
        ],
    },
}
