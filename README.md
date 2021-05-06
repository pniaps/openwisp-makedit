# openwisp-makedit

openwisp-makedit is a python packate to install with openwisp2 with custom modifications

## ow-makedit-theme

This app is needed to override default openwisp theme. It's important to add `ow-makedit-theme` to `INSTALLED_APPS` before `openwisp_users.accounts`, `openwisp_notifications` and `openwisp_utils.admin_theme`.

Then you have to add the following variable to ``settings.py``

    OPENWISP_ADMIN_THEME_LINKS = [
        {'type': 'text/css', 'href': '/static/makedit.css', 'rel': 'stylesheet', 'media': 'all'},
        {'type': 'image/x-icon', 'href': '/static/makedit.ico', 'rel': 'icon'}
    ]

## ow-makedit

The app `ow-makedit` must be added to the end of``INSTALLED_APPS``.

This app contains the custom modifications over openwisp.



