PlanIt — Backend (Django + DRF)

Backend de PlanIt construido con Django 5 + Django REST Framework.
Estructura modular bajo apps/, usuario custom desde el inicio y configuración lista para desarrollo.

🚀 Requisitos

Python 3.12 recomendado (3.11 OK)

Pip / venv

Git

(Opcional para prod) PostgreSQL

En Windows, activá el entorno: .\.venv\Scripts\Activate.ps1
En macOS/Linux: source .venv/bin/activate

⚙️ Puesta en marcha (dev)
1) Crear/activar entorno
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

2) Instalar dependencias
python -m pip install --upgrade pip
pip install django djangorestframework django-cors-headers django-environ Pillow

3) Migrar y arrancar
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # crea usuario admin
python manage.py runserver         # http://127.0.0.1:8000/

🔐 Variables de entorno (.env)

Archivo opcional en la raíz del proyecto (ya soportado por settings.py):

DEBUG=True
SECRET_KEY=dev-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
# Para Postgres (cuando migremos a prod)
# DB_NAME=planit
# DB_USER=postgres
# DB_PASS=postgres
# DB_HOST=127.0.0.1
# DB_PORT=5432


En desarrollo usamos SQLite por defecto (no requiere config).
En producción, cambiaremos a Postgres y DEBUG=False.

🗂️ Estructura del proyecto
PROYECTO/
├─ .venv/                # entorno virtual (no versionar)
├─ apps/                 # todas las apps del dominio
│  ├─ core/              # (eventos, asistencia, historias, etc.)
│  │  ├─ admin.py        # modelos en el admin
│  │  ├─ apps.py         # name = "apps.core"
│  │  ├─ models.py       # modelos de dominio
│  │  ├─ urls.py         # rutas de la app
│  │  ├─ views.py        # vistas / DRF views
│  │  └─ migrations/     # migraciones de DB
│  └─ users/             # user custom y perfil
│     ├─ admin.py
│     ├─ apps.py         # name = "apps.users"
│     ├─ models.py       # class User(AbstractUser)…
│     ├─ urls.py
│     └─ views.py
├─ config/               # paquete del proyecto
│  ├─ settings.py        # configuración (SQLite por defecto)
│  ├─ urls.py            # rutas raíz (incluye apps)
│  ├─ asgi.py / wsgi.py  # entrypoints servidor
│  └─ __init__.py
├─ templates/            # plantillas globales
├─ static/               # estáticos de trabajo (css/js/img)
├─ media/                # archivos subidos por usuarios
├─ info/                 # docs/notas del proyecto
├─ db.sqlite3            # DB de desarrollo
└─ manage.py             # CLI de Django


Claves:

AUTH_USER_MODEL = "users.User" (usuario custom ya activo).

apps/ evita choques de nombres y mantiene orden.

staticfiles/ se genera en prod con collectstatic.

📡 Endpoints de prueba

Admin: http://127.0.0.1:8000/admin

Healthcheck: GET /health → {"status":"ok"}

Users / me: GET /api/users/me/
Responde { "anonymous": true } si no hay sesión.

🧭 Flujo de trabajo (equipo)

Ramas: main (estable) + dev (integración) + feature/<nombre>

Commits (sugerido): Conventional Commits
feat:, fix:, chore:, docs:, refactor:, test:

Migraciones:

Al tocar modelos: makemigrations → migrate

Revisar archivos en apps/*/migrations/ antes del commit.

.gitignore sugerido:

.venv/
__pycache__/
*.pyc
db.sqlite3
.env
media/
staticfiles/

➕ Crear una nueva app
python manage.py startapp nombre apps/nombre
# en apps/nombre/apps.py -> name = "apps.nombre"
# en config/settings.py -> INSTALLED_APPS += ["apps.nombre"]


Agregar urls.py en la app y luego include("apps.nombre.urls") en config/urls.py.

🗄️ Cambiar a PostgreSQL (cuando toque)

Instalar driver: pip install psycopg2-binary

En settings.py (o .env) definir DATABASES para Postgres.

migrate y listo.

🧰 Notas útiles / Troubleshooting

ALLOWED_HOSTS con DEBUG=False: agregá dominio/IP en .env.

Poder activar venv en PowerShell:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

No reconoce pip: usar python -m pip … o revisar PATH.

No detecta cambios de modelos: asegurate de que la app esté en INSTALLED_APPS y que el modelo esté importado/definido.

📌 Roadmap inmediato

Modelar Event, Attendance, Story en apps.core y exponer endpoints DRF de lectura.

apps.users: Profile, Follow, endpoints básicos.

Integrar JWT (djangorestframework-simplejwt) para la app móvil.