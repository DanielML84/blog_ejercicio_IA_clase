# Blog de robótica

Blog en español para leer y publicar artículos sobre robótica. Está construido con Django y ofrece una experiencia editorial adaptable, accesible y centrada en la lectura.

## Funcionalidades

- Portada con los artículos publicados más recientes, sus imágenes, fechas y extractos.
- Página individual de cada artículo, con autoría y contenido en Markdown organizado en párrafos y subtítulos.
- Sección «Sobre mí», editable por la persona responsable del sitio.
- Navegación sencilla entre la portada, los artículos y «Sobre mí».
- Gestión de artículos y presentación del autor mediante Django Admin.
- Contenido de ejemplo reemplazable y páginas públicas que solo muestran artículos publicados.
- Diseño adaptable y accesible, con renderizado del lado del servidor.
- Página 404 propia para artículos inexistentes o no publicados.

No se contemplan cuentas públicas, comentarios, suscripciones, buscador ni funciones sociales.

## Rutas previstas

| Ruta | Descripción |
| --- | --- |
| `/` | Portada y artículos recientes |
| `/sobre-mi/` | Presentación del autor |
| `/articulos/<slug>/` | Lectura de un artículo |
| `/admin/` | Panel de administración restringido |

## Tecnología

- Django para el backend y el renderizado de páginas.
- Plantillas HTML semánticas y CSS adaptable.
- Pillow para imágenes, Markdown para el contenido de los artículos y nh3 para sanear el HTML generado.
- SQLite durante el desarrollo inicial.

La base de datos de producción y el entorno de despliegue quedan por definir.

## Ejecución local

Todos los comandos se ejecutan en PowerShell desde la raíz del proyecto.

### Requisitos

- Python 3 instalado (comando `py`).
- Git.

### Instalación (solo la primera vez)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src\manage.py migrate
python src\manage.py createsuperuser
```

- `py -m venv .venv` crea el entorno virtual en la carpeta `.venv`.
- `Activate.ps1` activa el entorno; aparece `(.venv)` al principio de la línea.
- `pip install` instala Django y las demás dependencias.
- `migrate` crea las tablas en la base de datos `db.sqlite3`.
- `createsuperuser` crea el usuario administrador (ver apartado siguiente).

### Arrancar el blog (cada vez)

```powershell
.\.venv\Scripts\Activate.ps1
python src\manage.py runserver
```

- Blog: `http://127.0.0.1:8000/`
- Administración: `http://127.0.0.1:8000/admin/`

El servidor funciona mientras la terminal siga abierta. Para pararlo: `Ctrl + C`.

### Si PowerShell no deja activar el entorno virtual

Si aparece el error *"running scripts is disabled on this system"*, ejecuta antes:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Solo afecta a la terminal abierta y no requiere permisos de administrador. Hay que repetirlo cada vez que se abre una terminal nueva.

### Usuario administrador y contraseña

No hay registro público: el administrador se crea en local desde la terminal, con el entorno virtual activado.

Crear un administrador:

```powershell
python src\manage.py createsuperuser
```

Pide nombre de usuario, email (opcional) y contraseña dos veces. Al escribir la contraseña no se muestra nada en pantalla.

Ver qué administradores existen:

```powershell
python src\manage.py shell -c "from django.contrib.auth.models import User; print(list(User.objects.filter(is_superuser=True).values_list('username', flat=True)))"
```

Cambiar o asignar la contraseña de un administrador existente:

```powershell
python src\manage.py changepassword <nombre_de_usuario>
```

### Estado de publicación de los artículos

Cada artículo tiene un campo **Publicado** (verdadero/falso), que en el panel de administración aparece como una casilla:

- Marcada (verdadero): el artículo aparece en la portada y su página es accesible.
- Desmarcada (falso): el artículo queda como borrador y no se muestra al público.

### Ejecutar los tests

```powershell
python src\manage.py test articles
```

Las imágenes subidas se guardan en `media/` y la base SQLite en `db.sqlite3`; ambos quedan excluidos de Git.## Documentación

- [Briefing](briefing.md): objetivo, público y alcance inicial.
- [PRD](PRD.md): requisitos funcionales, técnicos y criterios de éxito.
- [Visión del producto](spec/vision.md): propósito, usuarios y experiencia deseada.
- [Alcance](spec/scope.md): funciones incluidas y excluidas en la primera versión.
- [Criterios de aceptación](spec/acceptance_criteria.md): condiciones verificables para aceptar la entrega.

## Estructura del proyecto

- `src/config/`: configuración y rutas principales.
- `src/articles/`: modelos, vistas, administración, migraciones y pruebas.
- `src/templates/`: plantillas HTML del sitio.
- `src/static/`: estilos e imagen de portada.
- `db.sqlite3` y `media/`: datos locales fuera de `src/`.
- `spec/`: visión, alcance y criterios de aceptación.