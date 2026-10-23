# Alcance: Blog de robótica

## Objetivo

Definir la primera versión de un blog en español sobre robótica que permita a los visitantes leer publicaciones y conocer al autor, y que permita a una persona editora mantener el contenido desde el panel administrativo de Django.

## Incluido en la primera versión

### Experiencia pública

- **Portada (`/`):** muestra el nombre del blog y los artículos publicados más recientes, ordenados del más nuevo al más antiguo. Cada entrada incluye título, imagen, fecha, extracto y enlace al artículo. Si no hay publicaciones, presenta un mensaje informativo.
- **Detalle de artículo (`/articulos/<slug>/`):** muestra título, imagen, fecha de publicación, autoría y contenido estructurado con párrafos y subtítulos. Las rutas de artículos inexistentes responden con HTTP 404 original (y a ser posible, graciosa).
- **Sobre mí (`/sobre-mi/`):** presenta al autor mediante un texto breve, editable por la persona responsable del sitio.
- **Navegación:** ofrece enlaces claros entre la portada y «Sobre mí», y permite volver a la portada desde un artículo. La navegación básica funciona sin JavaScript.
- **Diseño y accesibilidad:** interfaz adaptable a móviles y ordenadores, centrada en la lectura, con HTML semántico, jerarquía coherente de encabezados, enlaces descriptivos y uso con teclado.

### Gestión editorial

- Panel administrativo estándar de Django, accesible únicamente a usuarios autorizados.
- Alta, edición y retirada de artículos, y edición de la presentación del autor.
- Artículos con título, slug, contenido, autoría, fecha de publicación y estado de publicación.
- Solo los artículos publicados aparecen en las páginas públicas; los borradores quedan disponibles para la persona editora autenticada desde el panel.
- Contenido de ejemplo relacionado con robótica que pueda sustituirse o eliminarse.
- No existe registro público ni gestión de cuentas para visitantes.

### Base técnica de la primera versión

- Renderizado del lado del servidor con Django, modelos y migraciones.
- Plantillas HTML semánticas y CSS adaptable.
- SQLite para el desarrollo inicial.

## Fuera del alcance

- Registro, perfiles o cuentas para visitantes.
- Comentarios, reacciones, funciones sociales o interacción entre lectores.
- Suscripciones, boletines o notificaciones.
- Búsqueda de artículos.
- Flujos editoriales avanzados, como revisión, programación de publicaciones o múltiples roles.
- Aplicación móvil, API pública o experiencia dependiente de JavaScript para la navegación esencial.
- Definición del dominio, identidad visual definitiva o configuración de despliegue en producción.
- Decisión de la base de datos de producción, que dependerá del entorno de publicación.

## Restricciones y supuestos

- El idioma inicial es el español y el tema editorial es la robótica.
- La primera versión contempla una persona editora y una única presentación principal del autor.
- La prioridad es consultar y mantener contenido; no se incluyen funciones de participación de lectores.
- Las páginas deben favorecer la lectura prolongada, evitar desplazamiento horizontal innecesario y no depender de JavaScript para las tareas básicas.
- La seguridad del panel y de las operaciones editoriales debe seguir las prácticas recomendadas por Django; la publicación en producción requiere definir y revisar la configuración del entorno.

## Criterio de finalización del alcance

La primera versión está dentro del alcance cuando un visitante puede recorrer la portada, abrir y leer artículos publicados, consultar «Sobre mí» y volver a la portada; cuando las rutas inválidas muestran una respuesta 404; y cuando la persona editora puede mantener artículos y presentación desde Django Admin sin modificar plantillas.
