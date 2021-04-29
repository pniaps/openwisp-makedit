# openwisp-makedit

openwisp-makedit is a python packate to install with openwisp2 with custom modifications

## ow-makedit app

The app `ow-makedit` must be added to ``INSTALLED_APPS`` before `openwisp_users.accounts`, `openwisp_notifications` and `openwisp_utils.admin_theme` to be able to override templates.

Then you have to add the following variable to ``settings.py``

    OPENWISP_ADMIN_THEME_LINKS = [
        {'type': 'text/css', 'href': '/static/makedit.css', 'rel': 'stylesheet', 'media': 'all'},
        {'type': 'image/x-icon', 'href': '/static/makedit.ico', 'rel': 'icon'}
    ]


