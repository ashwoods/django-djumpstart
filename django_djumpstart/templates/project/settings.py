# Django settings for project.
# The settings here are project related and should not be deployment specific.
# A host_settings.py settings file will automatically be created where
# deployment specific changes should be made.

import os
from socket import gethostname

# Environment variables 


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = PROJECT_PATH.split(os.sep)[-1]


TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, "templates"),)
ADMIN_MEDIA_PREFIX = "/media/admin/"
ROOT_URLCONF = "%s.urls" % PROJECT_DIR
SITE_ID = 1


# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
# LANGUAGE_CODE = 'de-at'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
     'django.template.loaders.eggs.load_template_source',
)

# List of middelwares
MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',       
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

# List of context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
#    "grappelli.context_processors.admin_template_path",
)

INSTALLED_APPS = ( 
#    'grappelli',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    
    #!-- must have apps
    'south',
    'debug_toolbar',
    'django_extensions',
    'explain_commands',
    #!-- core apps
    'apps.tests',
)


#TINYMCE
#TINYMCE_JS_URL = '/site_media/scripts/tiny_mce_src.js'
#TINYMCE_JS_ROOT = '/site_media/scripts/'
#TINYMCE_DEFAULT_CONFIG = {
#      'theme': "advanced",
#      'cleanup_on_startup': True,
#      'custom_undo_redo_levels': 10,
#  }
#TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = False
#TINYMCE_FILEBROWSER = True


#DEBUG_TOOLBAR

DEBUG_TOOLBAR_CONFIG = {
         'INTERCEPT_REDIRECTS': False,
         #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
         }


INTERNAL_IPS = ('127.0.0.1',)

#!--- Default config ----#
# You might want to overide these
# If you want to override these, do it in your host config file in conf/

MEDIA_URL = "http://127.0.0.1/%s/" % (PROJECT_DIR) 
MEDIA_ROOT = '%s/media/' % (PROJECT_DIR)
ADMIN_MEDIA_PREFIX = "/media/admin/"
DEBUG=True
TEMPLATE_DEBUG = DEBUG

ADMINS = (     
    # ('Django guru', 'mail@example.com'),
    )

MANAGERS = ADMINS
#SECRET_KEY = 'Generate a new key!!!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqllite',
        'PASSWORD':'',
        'USER':'',
        }
    }


#!--- Load/Create deployment/host based config file ---#
CONFIG_PATH = os.path.join(PROJECT_PATH,"conf","host_settings")
HOST_SETTINGS_MODULE = "%s_%s" % (PROJECT_DIR, 
    gethostname().replace("-", "_").replace(".", "_").lower())
HOST_SETTINGS_PATH = os.path.join(CONFIG_PATH,  
    "%s.py" % HOST_SETTINGS_MODULE)


if not os.path.exists(HOST_SETTINGS_PATH):
    print "Host file does not exist, trying to create one under conf/host_settings. Will use default settings for now."
    try:
        f = open(HOST_SETTINGS_PATH, "w")
        f.close()
    except IOError:
        print "Error: Couldn't create host_settings module: %s under conf/. Check folder permissions." % HOST_SETTINGS_PATH
try:
    exec  "from conf.host_settings.%s import *" % (HOST_SETTINGS_MODULE)
except ImportError:
    print "Error: Could not import %s.conf.host_settings.%s. Using defaultsettings." % (PROJECT_DIR, HOST_SETTINGS_MODULE)


    






