
PlanIt — Backend (Django + DRF)


> Backend de **PlanIt**, plataforma social para crear, descubrir y vivir planes y eventos en tiempo real.

- 🧱 **Stack:** Django 5 · Django REST Framework · CORS · SQLite (dev)
- 🧰 **Estructura modular:** apps bajo `apps/` (`apps.users`, `apps.core`)
- 👤 **Usuario custom** desde el inicio (`AUTH_USER_MODEL=users.User`)

## 🚀 Requisitos

- **Python** 3.12 recomendado (3.11 OK)  
- **pip / venv**  
- **Git**  
- (Opcional prod) **PostgreSQL**

> En Windows activá el venv con:  
> `.\.venv\Scripts\Activate.ps1`  
> En macOS/Linux: `source .venv/bin/activate`

---

## ⚙️ Puesta en marcha (dev)

## 1) **Crear/activar entorno virtual**

> python -m venv .venv
## Windows
> .\.venv\Scripts\Activate.ps1
# macOS / Linux
> source .venv/bin/activate

## 2) Instalar dependencias

> python -m pip install --upgrade pip
> pip install django djangorestframework django-cors-headers django-environ Pillow

## 3) **Migrar, crear admin y levantar**

> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver  # http://127.0.0.1:8000/


## 4) Estructura del proyecto

```text
PROYECTO/
├─ .venv/                # entorno virtual (no versionar)
├─ apps/                 # apps del dominio (modular)
│  ├─ core/              # eventos, asistencia, historias, etc.
│  │  ├─ admin.py
│  │  ├─ apps.py         # name = "apps.core"
│  │  ├─ models.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ migrations/
│  └─ users/             # usuario custom y vistas básicas
│     ├─ admin.py
│     ├─ apps.py         # name = "apps.users"
│     ├─ models.py       # class User(AbstractUser)
│     ├─ urls.py
│     └─ views.py
├─ config/               # paquete del proyecto
│  ├─ settings.py        # SQLite, CORS, DRF, apps instaladas
│  ├─ urls.py            # incluye urls de apps
│  ├─ asgi.py / wsgi.py
│  └─ __init__.py
├─ templates/            # plantillas globales
├─ static/               # estáticos de trabajo (css/js/img)
├─ media/                # archivos subidos por usuarios
├─ info/                 # docs/notas del proyecto
├─ db.sqlite3            # BD de desarrollo
└─ manage.py
```

## 5) **Endpoints de prueba**

> Admin: http://127.0.0.1:8000/admin

> Healthcheck: GET /health → {"status":"ok"}

> Users / me: GET /api/users/me/

> Responde { "anonymous": true } si no hay sesión

## 6) **.gitignore**
```
 .venv/
 __pycache__/
*.pyc
db.sqlite3
.env
media/
staticfiles/
```
## Organizacion del proyecto

**No se trabaja directo sobre main ni sobre dev.**

**Se debe crear una rama feature por cada desarrollo.**

> Main → producción. Solo entra vía PR desde release/*.

> Dev --> integración diaria. Se auto-despliega a ambiente de desarrollo. Acá convergen todas las features

> Feature/* → trabajo por historia/tarea.

 La convencion de los nombres de estas van a ser:

    feature/* → trabajo por historia/tarea. 
    feature/registro_usuarios
