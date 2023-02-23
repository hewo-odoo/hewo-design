{
    'name': 'SCG home Theme',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website_sale','website_blog'],
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
        'data/pages/contactus.xml',
        'data/pages/service_solutions.xml',
        'data/pages/maintenance.xml',
        #Frontend
        'views/website_template.xml',
        'views/website_blog.xml',
    ],
    # "demo": [
    #     "demo/website_blog_demo.xml",
    # ],
    'assets': {
        'web._assets_primary_variables': [
            'website_scghome/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            # SCSS
            #'website_scghome/static/src/scss/theme.scss',
        ],
    },
}
