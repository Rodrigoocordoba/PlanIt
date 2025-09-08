# config/settings.py
from pathlib import Path
import os

# Opcional: usar django-environ si está instalado (recomendado)
try:
    import environ
    env = environ.Env(
        DEBUG=(bool, True),
    )
    # Lee variables desde .env si existe
    ENV_FILE = os.path.join(Path(__file__).resolve().parent.parent, ".env")
    if os.path.exists(ENV_FILE):
        environ.Env.read_env(ENV_FILE)
except ImportError:
    env = None

# ----------------------------------
# BASE
# ----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = (
    env("SECRET_KEY") if env and env("SECRET_KEY", default=None)
    else "dev-secret-key-no-uso-en-produccion"
)

DEBUG = env("DEBUG", default=True) if env else True

ALLOWED_HOSTS = (
    env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])
    if env else ["127.0.0.1", "localhost"]
)

# Si necesitás CSRF en ambientes remotos, podés setear:
# CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# ----------------------------------
# APPS
# ----------------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceros
    "rest_framework",
    "corsheaders",

    # Nuestras apps (con prefijo 'apps.')
    "apps.users",
    "apps.core",
]

# ----------------------------------
# MIDDLEWARE
# ----------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ----------------------------------
# URLS / WSGI / ASGI
# ----------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# ----------------------------------
# TEMPLATES
# ----------------------------------
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

# ----------------------------------
# BASE DE DATOS (SQLite por defecto)
# ----------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ----------------------------------
# AUTH / I18N
# ----------------------------------
AUTH_USER_MODEL = "users.User"  # label de la app 'users'
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# ----------------------------------
# STATIC / MEDIA
# ----------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]       # assets de desarrollo
STATIC_ROOT = BASE_DIR / "staticfiles"         # destino collectstatic (prod)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------------
# DRF / CORS
# ----------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    # Podés cambiar más adelante a JWT si querés.
}

CORS_ALLOW_ALL_ORIGINS = True
# Si preferís lista blanca:
# CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
