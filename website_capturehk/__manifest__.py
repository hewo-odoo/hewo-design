{
    'name': 'capturehk Theme',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website_sale','website_blog','website_mass_mailing'],
    'license': 'OEEL-1',
    'data': [
        # Options
        'data/presets.xml',
        # Menu
        'data/menu.xml',
        # Images
        'data/images.xml',
        # Pages
        'data/pages/contactus.xml',
        'data/pages/home.xml',
        'data/pages/products.xml',
        'data/pages/photo-album.xml',
        'data/pages/photographs.xml',
        'data/pages/videotape.xml',
        'data/pages/digital-media.xml',
        'data/pages/google-photos.xml',
        'data/pages/usb.xml',
        'data/pages/our-story.xml',
        'data/pages/privacy.xml',
        'data/pages/security.xml',
        'data/pages/customer-care.xml',
        'data/pages/faq.xml',
        'data/pages/how-it-works.xml',
        'data/pages/online-prepayment.xml',
        'data/pages/onsite-payment.xml',
        'data/pages/buy-now.xml',
        'data/pages/terms.xml',
        'data/pages/privacy-policy.xml',
        # 'data/pages/website_blog.xml',
        #Frontend
        'views/website_template.xml',
        # Header
        # 'views/header.xml',
        # Footer
        # 'views/footer.xml',
    ],
    "demo": [
        "demo/website_blog_demo.xml",
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_capturehk/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            # SCSS
            'website_capturehk/static/src/scss/theme.scss',
        ],
    },
}
