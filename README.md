# Portfolio — guía de uso

Sitio estático, sin dependencias ni compilación. Se edita abriendo los `.html` en cualquier editor de texto.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | Portada, rejilla de proyectos, sobre mí y contacto |
| `proyecto-sal-de-garraf.html` | Plantilla de caso. Duplícala una vez por proyecto |
| `styles.css` | Todos los estilos. Los colores están arriba del todo, en `:root` |
| `404.html` | Página de error |
| `img/` | Créala tú y mete ahí tus imágenes |

## Lo primero que hay que cambiar

1. `Marta Ferrer` → tu nombre (aparece en `<title>`, `<h1>`, el pie y las etiquetas `og:`).
2. `MF` → tus iniciales, en la barra superior de cada página.
3. `hola@ejemplo.com` → tu correo real.
4. Los `href="#"` de Instagram, LinkedIn y Behance.
5. `https://ejemplo.com` → tu dominio, en `canonical` y `og:image`.

## Añadir un proyecto

1. Duplica `proyecto-sal-de-garraf.html` y renómbralo, por ejemplo `proyecto-nocturna.html`. Sin acentos, sin espacios, en minúsculas.
2. Cambia título, ficha y textos.
3. Sustituye cada `<div class="hueco">…</div>` por una imagen real:
   ```html
   <img src="img/nocturna-cartel.webp" alt="Cartel del festival en marquesina"
        width="1600" height="1067" loading="lazy">
   ```
   Poner `width` y `height` evita que la página dé saltos mientras carga.
4. En `index.html`, copia un bloque `<article class="proyecto">`, cámbiale el enlace, el título y la portada, y añádelo también al índice de la portada.

Tamaños de la rejilla, por si quieres recolocar: `proyecto--ancho`, `proyecto--medio`, `proyecto--medio-b`, `proyecto--corto`, `proyecto--alto`.

## Publicar en GitHub Pages

1. Crea un repositorio **público** llamado `tuusuario.github.io` (con tu usuario exacto).
2. Sube estos archivos a la raíz del repositorio, no dentro de una carpeta.
3. Settings → Pages → Source: `Deploy from a branch`, rama `main`, carpeta `/ (root)`.
4. En dos o tres minutos estará en `https://tuusuario.github.io`.

Añade un archivo vacío llamado `.nojekyll` en la raíz: evita que GitHub intente procesar el sitio con Jekyll y descarte carpetas que empiecen por guion bajo.

## Dominio propio

1. Compra el dominio (Namecheap, Porkbun, Gandi, DonDominio…). Mira el precio de **renovación**, no el de primer año.
2. En el DNS del registrador crea:
   - Cuatro registros **A** para el dominio raíz apuntando a `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
   - Un registro **CNAME** para `www` apuntando a `tuusuario.github.io`.
3. En Settings → Pages → Custom domain, escribe tu dominio. GitHub creará un archivo `CNAME` en el repositorio: no lo borres.
4. Espera a que aparezca el certificado y marca **Enforce HTTPS**.

La propagación puede tardar de minutos a 24 horas. Hasta entonces es normal ver errores de certificado.
