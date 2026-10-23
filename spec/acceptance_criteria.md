# Criterios de aceptación: Blog de robótica

Estos criterios definen las condiciones observables para considerar completa la primera versión. Cuando `scope.md` amplía el PRD, se toman en cuenta las decisiones vigentes del alcance, incluidas las imágenes y el tono propio de la página 404.

## CA-01: Portada y publicaciones recientes

- Dada una persona visitante, cuando accede a `/`, entonces se muestra el nombre del blog y la lista de artículos publicados.
- Cada artículo de la lista muestra título, imagen, fecha de publicación y extracto, y ofrece un enlace descriptivo a su página.
- Los artículos aparecen ordenados del más nuevo al más antiguo.
- Los artículos en borrador no aparecen en la portada ni en ninguna otra página pública.
- Cuando no hay artículos publicados, la portada muestra un mensaje informativo en lugar de una lista vacía sin explicación.

## CA-02: Lectura de artículos

- Cuando una persona abre `/articulos/<slug>/` para un artículo publicado, la página muestra su título, imagen, fecha de publicación, autoría y contenido.
- El contenido conserva los párrafos y subtítulos que se hayan introducido y se presenta con una jerarquía legible.
- La imagen del artículo se muestra sin deformarse y se proporciona texto alternativo cuando sea informativa.
- Si el slug no corresponde a un artículo publicado, la respuesta HTTP es 404 y se presenta una página de error propia, con un mensaje claro y, si es posible, humor negro.
- Desde el detalle de un artículo hay un enlace claro para volver a la portada.

## CA-03: Sección «Sobre mí»

- `/sobre-mi/` muestra una página identificable como «Sobre mí» con la presentación del autor.
- La presentación puede actualizarse desde el panel administrativo sin editar plantillas.
- La navegación principal incluye un enlace «Sobre mí» que funciona desde las páginas públicas.

## CA-04: Navegación

- Las páginas públicas ofrecen navegación clara entre la portada y «Sobre mí».
- Los enlaces describen su destino y pueden activarse mediante teclado.
- La navegación esencial funciona sin JavaScript.

## CA-05: Gestión editorial y acceso

- Una persona editora autenticada puede crear, editar y retirar artículos desde Django Admin.
- En cada artículo se pueden gestionar título, slug, contenido, autoría, fecha, estado de publicación e imagen.
- La persona editora puede crear y actualizar la presentación del autor desde el panel.
- Una persona anónima no puede acceder a las operaciones de edición del panel administrativo.
- No hay registro público ni creación de cuentas para visitantes.
- El contenido de ejemplo está relacionado con robótica y puede sustituirse o eliminarse desde el panel.

## CA-06: Adaptabilidad, legibilidad y accesibilidad

- Las páginas pueden utilizarse en pantallas móviles y de escritorio sin pérdida de contenido ni desplazamiento horizontal innecesario.
- El HTML utiliza estructura semántica y una jerarquía coherente de encabezados.
- El texto, los enlaces y los controles mantienen contraste y legibilidad suficientes para su uso normal.
- Los enlaces y controles interactivos pueden recorrerse y utilizarse con teclado.

## CA-07: Renderizado y robustez

- Las páginas informativas se renderizan en el servidor con Django; JavaScript no es necesario para leer contenido ni navegar por las rutas principales.
- Una solicitud a una ruta de artículo inexistente responde con estado HTTP 404.
- El acceso público solo expone contenido publicado; los borradores quedan restringidos a la persona editora autenticada en el panel.

## Condición de aceptación de la primera versión

La primera versión se acepta cuando se cumplen los criterios CA-01 a CA-07 y una persona puede recorrer el flujo completo desde la portada a un artículo y a «Sobre mí», mientras la persona editora mantiene artículos y presentación sin modificar las plantillas.
