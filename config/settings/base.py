"""
Title: Freshdesk CRM Platform.
Description: Freshdesk is smart ERP solution to manage your business. you can keep track of your inventory customers, products, orders, invoices, and more.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty

"""
import os
import re
from pathlib import Path

import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
def gettext_noop(s):
    return s


# Cloudinary configration
# cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'),
#                   api_secret=os.getenv('API_SECRET'))


BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']


DJANGO_COMMON_APPS = [
    # 'admin_volt.apps.AdminVoltConfig', # Modern Admin UI 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'import_export',
    'django_user_agents',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_filters',
    'crispy_forms',
    'simple_history',
    'django_countries',
    'rest_framework',
    'phonenumber_field',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'defender',
    'zxcvbn_password',
    'ckeditor',
    'ckeditor_uploader',
]

LOCAL_APPS = [
    'core.apps.CoreConfig',
    'stock.apps.StockConfig',
    'expense.apps.ExpenseConfig',
    'sales.apps.SalesConfig',
    'report.apps.ReportConfig',
    'service.apps.ServiceConfig',
    'returns.apps.ReturnsConfig',
    'damage.apps.DamageConfig',
    'settings.apps.SettingsConfig',
    'profiles.apps.ProfilesConfig',
    'products.apps.ProductsConfig',
    'accounts.apps.AccountsConfig',
    'purchase.apps.PurchaseConfig',
    'suppliers.apps.SuppliersConfig',
    'customers.apps.CustomersConfig',
    'authenticator.apps.AuthenticatorConfig',
    'analytics.apps.AnalyticsConfig',
]

INSTALLED_APPS = DJANGO_COMMON_APPS + LOCAL_APPS + THIRD_PARTY_APPS


SITE_ID = 1

# Thousand separator symbol
THOUSAND_SEPARATOR = ','
PHONENUMBER_DEFAULT_REGION = 'BD'
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
##################
# REST FRAMEWORK #
##################

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         # 'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.AllowAny',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#     'rest_framework.authentication.TokenAuthentication',
#     'rest_framework.authentication.SessionAuthentication',
#     ],
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# }

REST_FRAMEWORK = {
    # 'SEARCH_PARAM': 'search'
    'SEARCH_PARAM': 'q'
}

# Setting the throttling policy

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '2/day',
    #     'user': '5/hour',
    #     'sale': '3/min',
    # }
}

##############
# MIDDLEWARE #
##############

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Third party middleware📌
    'defender.middleware.FailedLoginMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Third party middleware📌
    'corsheaders.middleware.CorsMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    # Custom middleware📌
    # 'core.middleware.activity.UserActivityMiddleware',
    # 'core.middleware.visitors.UserStatisticsMiddleware',
    'core.middleware.requests.RequestMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom context processors📌
                # Each context processor must return a dictionary
                'expense.context_processors.get_total_expsense',
                'expense.context_processors.get_total_expsense_by_month',
                'expense.context_processors.get_total_expsense_by_year',
                # customers
                'customers.context_processors.customer_created_at_january',
                'customers.context_processors.customer_created_at_february',
                'customers.context_processors.customer_created_at_march',
                'customers.context_processors.customer_created_at_april',
                'customers.context_processors.customer_created_at_may',
                'customers.context_processors.customer_created_at_june',
                'customers.context_processors.customer_created_at_july',
                'customers.context_processors.customer_created_at_august',
                'customers.context_processors.customer_created_at_september',
                'customers.context_processors.customer_created_at_october',
                'customers.context_processors.customer_created_at_november',
                'customers.context_processors.customer_created_at_december',

                # 'sales.context_processors.march_sales',
            ],
        },
    },
]


# Mail configrations
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

############
# SESSIONS #
############

# Cookie name. This can be whatever you want.
# SESSION_COOKIE_NAME = 'DUMMY_SESSION'

# Age of cookie, in seconds 52 weeks
SESSION_COOKIE_AGE = 31449600

# Whether to save the session data on every request.
SESSION_SAVE_EVERY_REQUEST = False

# Whether a user's session cookie expires when the web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


##################
# AUTHENTICATION #
##################

AUTH_USER_MODEL = 'authenticator.User'

LOGIN_REDIRECT_URL = '/dashboard'

LOGIN_URL = '/auth/sign-in/'

LOGOUT_REDIRECT_URL = '/'

# The number of seconds a password reset link is valid for (default: 3 days).
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'zxcvbn_password.ZXCVBNValidator',
        'OPTIONS': {
            'min_score': 3,
            'user_attributes': ('email', 'organization_name', 'owner_name')
        }
    }
]

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*/.png$'),
    re.compile(r'^/favicon.ico$'),
    re.compile(r'^/robots.txt$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'^/sitemap\.xml$'),
    re.compile(r'^/sitemap-index\.xml$'),
    re.compile(r'^/static/'),
    re.compile(r'^/media/'),
    re.compile(r'^/api/')
]


# Celery Configurations
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

'''
sqlite3
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/freshdesh-db.sqlite3',
    },

}

# The list of routers that will be used to determine which database to use when performing a database query.
# DATABASE_ROUTERS = ['database.routers.db_routers.ExpenseRouter']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'Freshdesk-CRM-Platform/cache/',
    }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
CRISPY_TEMPLATE_PACK = "bootstrap4"


# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
