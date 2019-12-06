# coding:utf-8

"""
DCRM - Darwin Cydia Repository Manager
Copyright (C) 2017  WU Zheng <i.82@me.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
from dotenv import load_dotenv
load_dotenv()

# SITE ID & BASE DIR
"""
!!! DO NOT CHANGE THIS SECTION IF YOU DO NOT KNOW WHAT IT MEANS !!!
"""
SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# THEME
THEME         = os.environ.get('DCRM_THEME', 'DefaultStyle')


# FEATURES
ENABLE_REDIS  = int(os.environ.get('DCRM_ENABLE_REDIS', True)) == 1
ENABLE_CACHE  = int(os.environ.get('DCRM_ENABLE_CACHE', True)) == 1
ENABLE_API    = int(os.environ.get('DCRM_ENABLE_API', False))  == 1


# SECURITY
# WARNING: keep the secret key secret!
# WARNING: don't run with debug turned on in production!
SECRET_KEY    = os.environ.get('DCRM_SECRET_KEY', 'vR*dKs4pp9MGx*V-j8hbB7wF*u6N98XLaXyJtPxHBr_.2-448a')
DEBUG         = int(os.environ.get('DCRM_DEBUG', True))       == 1        
SECURE_SSL    = int(os.environ.get('DCRM_SECURE_SSL', False)) == 1
ALLOWED_HOSTS = [
    os.environ.get('DCRM_HOST', 'apt.82flex.com'),
    '127.0.0.1',
    'localhost'
]
print("[DCRM] Host: " + ALLOWED_HOSTS[0])


# INTERNATIONAL
USE_I18N      = int(os.environ.get('DCRM_USE_I18N', True)) == 1
USE_L10N      = int(os.environ.get('DCRM_USE_L10N', True)) == 1
USE_TZ        = int(os.environ.get('DCRM_USE_TZ', True))   == 1
LANGUAGE_CODE = os.environ.get('DCRM_LANGUAGE_CODE', 'en')
TIME_ZONE     = os.environ.get('DCRM_TIME_ZONE', 'Asia/Shanghai')


# DATABASE
# You cannot use SQLite3 due to the lack of advanced database supports.
# !!! change the 'NAME' here if you have multiple DCRM installed !!!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DCRM_MYSQL_NAME', 'DCRM'),  # mysql database name here, should match `docker-compose.yml`
        'USER': os.environ.get('DCRM_MYSQL_USER', 'dcrm'),  # mysql user name here, should match `docker-compose.yml`
        'PASSWORD': os.environ.get('DCRM_MYSQL_PASSWORD', 'dcrm_user_password'),  # mysql user password here, should match `docker-compose.yml`
        'HOST': os.environ.get('DCRM_MYSQL_HOST', '127.0.0.1'),  # if you don't use docker, set it to 127.0.0.1
        'PORT': os.environ.get('DCRM_MYSQL_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# REDIS (TASK QUEUE)
if ENABLE_REDIS is True:
    # Redis
    # !!! change the 'DB' number here if you have multiple DCRM installed !!!
    RQ_QUEUES = {
        'default': {
            'HOST': os.environ.get('DCRM_REDIS_HOST', '127.0.0.1'),  # if you don't use docker, set it to 127.0.0.1
            'PORT': int(os.environ.get('DCRM_REDIS_PORT', 6379)),
            'DB': 0,
            'PASSWORD': '',
            'DEFAULT_TIMEOUT': 360,
        },
        'high': {
            'HOST': os.environ.get('DCRM_REDIS_HOST', '127.0.0.1'),  # if you don't use docker, set it to 127.0.0.1
            'PORT': int(os.environ.get('DCRM_REDIS_PORT', 6379)),
            'DB': 0,
            'PASSWORD': '',
            'DEFAULT_TIMEOUT': 360,
        },
    }
    print("[DCRM] Redis Queue: Enabled")
else:
    print("[DCRM] Redis Queue: Disabled")


# MEMCACHED (PAGE CACHING)
CACHE_TIME = 0
if ENABLE_CACHE is True:
    # Cache
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': os.environ.get('DCRM_MEMCACHED_HOST', '127.0.0.1') + ':' + os.environ.get('DCRM_MEMCACHED_PORT', '11211'),
        }
    }
    CACHE_TIME = int(os.environ.get('DCRM_CACHE_TIME', 7200))
    if DEBUG:
        CACHE_TIME = 0
    print("[DCRM] Page Caching: Enabled, %s seconds." % str(CACHE_TIME))
else:
    print("[DCRM] Page Caching: Disabled")


# NGINX
"""
!!! DO NOT CHANGE THIS SECTION IF YOU USE DOCKER !!!
"""
# !!! remember to configure Nginx to make an alias from STATIC_URL to STATIC_ROOT !!!
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []
"""
!!! DO NOT CHANGE THIS SECTION IF YOU USE DOCKER !!!
"""
# !!! remember to configure Nginx to make an alias from MEDIA_URL to MEDIA_ROOT !!!
MEDIA_URL = '/resources/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'resources')





"""
!!! DO NOT EDIT ANYTHING BELOW !!!
!!! DO NOT EDIT ANYTHING BELOW !!!
!!! DO NOT EDIT ANYTHING BELOW !!!
"""
"""
!!! 如果你不知道下面各项配置的作用，请勿修改以下任何内容 !!!
!!! 如果你不知道下面各项配置的作用，请勿修改以下任何内容 !!!
!!! 如果你不知道下面各项配置的作用，请勿修改以下任何内容 !!!
"""

INSTALLED_APPS = [
    'WEIPDCRM',
    'WEIPDCRM.apps.SuitConfig',
    'WEIPDCRM.styles.' + THEME,
    'preferences',
    "suit_redactor",
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fluent_comments',
    'threadedcomments',
    'crispy_forms',
    'django_comments',
    'sortedm2m',
    'photologue',
]

if ENABLE_REDIS is True:
    INSTALLED_APPS.append('scheduler')
    INSTALLED_APPS.append('django_rq')

if ENABLE_API is True:
    INSTALLED_APPS.append('rest_framework')
    INSTALLED_APPS.append('django_filters')

COMMENTS_APP = 'fluent_comments'
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('url', 'title')
CRISPY_TEMPLATE_PACK = 'bootstrap3'
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

MIDDLEWARE_CLASSES = [
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DCRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "preferences.context_processors.preferences_cp",
                "WEIPDCRM.context_processors.admin_context"
            ],
        },
    },
]

WSGI_APPLICATION = 'DCRM.wsgi.application'

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
]

LANGUAGES = (
    ('en',      u'English'),
    ('ar',      u'العربية'),
    ('zh_Hans', u'中文简体'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
    os.path.join(BASE_DIR, "fluent_comments/locale"),
    os.path.join(BASE_DIR, "WEIPDCRM/locale"),
    os.path.join(BASE_DIR, "WEIPDCRM/styles/DefaultStyle/locale"),
)
TEMP_ROOT = os.path.join(BASE_DIR, 'temp')

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

