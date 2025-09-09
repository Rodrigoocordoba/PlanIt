# Create README.md content and save it to /mnt/data/README.md

readme = r'''# PlanIt — Backend (Django + DRF)

> Backend de **PlanIt**, plataforma social para crear, descubrir y vivir planes y eventos en tiempo real.

- 🧱 **Stack:** Django 5 · Django REST Framework · CORS · SQLite (dev)
- 🧰 **Estructura modular:** apps bajo `apps/` (`apps.users`, `apps.core`)
- 👤 **Usuario custom** desde el inicio (`AUTH_USER_MODEL=users.User`)

---

## 🧭 Tabla de contenidos

- [🚀 Requisitos](#-requisitos)  
- [⚙️ Puesta en marcha (dev)](#️-puesta-en-marcha-dev)  
- [🔐 Variables de entorno (`.env`)](#-variables-de-entorno-env)  
- [🗂️ Estructura del proyecto](#️-estructura-del-proyecto)  
- [📡 Endpoints de prueba](#-endpoints-de-prueba)  
- [🧰 Comandos útiles](#-comandos-útiles)  
- [🧭 Flujo de trabajo (equipo)](#-flujo-de-trabajo-equipo)  
- [📝 .gitignore sugerido](#-gitignore-sugerido)  
- [➕ Crear una nueva app](#-crear-una-nueva-app)  
- [🗄️ Migrar a PostgreSQL (más adelante)](#️-migrar-a-postgresql-más-adelante)  
- [🩺 Troubleshooting](#-troubleshooting)

---

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

1) **Crear/activar entorno virtual**
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
