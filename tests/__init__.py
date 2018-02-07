def configure():
    from django.conf import settings
    if not settings.configured:

        settings.configure(
            DEBUG_PROPAGATE_EXCEPTIONS=True,
            DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                                   'NAME': ':memory:'}},
            ALLOWED_HOSTS=['*'],
            SITE_ID=1,
            SECRET_KEY='none',
            USE_I18N=True,
            USE_L10N=True,
            STATIC_URL='/static/',
            ROOT_URLCONF='tests.urls',
            MIDDLEWARE_CLASSES=(
                'django.middleware.common.CommonMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
            ),
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.staticfiles',

                'related_select',
                'tests',
            ),
            PASSWORD_HASHERS=(
                'django.contrib.auth.hashers.MD5PasswordHasher',
            ),
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [],
                    'OPTIONS': {
                        'context_processors': [
                            # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                            # list if you haven't customized them:
                            'django.contrib.auth.context_processors.auth',
                            'django.template.context_processors.debug',
                            'django.template.context_processors.i18n',
                            'django.template.context_processors.media',
                            'django.template.context_processors.static',
                            'django.template.context_processors.tz',
                            'django.contrib.messages.context_processors.messages',
                        ],
                        'loaders': [
                            'django.template.loaders.filesystem.Loader',
                            'django.template.loaders.app_directories.Loader'
                        ]
                    },
                },
            ]

        )

        try:
            import django
            django.setup()
        except AttributeError:
            pass
