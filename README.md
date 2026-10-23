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

Desde la raíz del proyecto, en PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src\manage.py migrate
python src\manage.py createsuperuser
python src\manage.py runserver
```

Abre `http://127.0.0.1:8000/` para visitar el blog y `http://127.0.0.1:8000/admin/` para gestionar el contenido. El usuario editorial se crea localmente con `createsuperuser`; no hay registro público.

Las imágenes subidas se guardan en `media/` y la base SQLite en `db.sqlite3`; ambos quedan excluidos de Git.

## Documentación

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