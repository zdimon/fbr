# -*- coding: utf-8 -*-
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fbr',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': 'rjvgfhnbz77',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },

   

}
