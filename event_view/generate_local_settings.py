from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = """SECRET_KEY = \'{0}\'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'Host': '',
        'PORT': '',
    }
}
""".format(secret_key)
print(text)
