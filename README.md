# Portfolio — guía de uso

Sitio estático, sin dependencias ni compilación. Se edita abriendo los `.html` en cualquier editor.

## Estructura de la página principal

1. **Portada** a pantalla completa: vídeo de fondo, eslogan arriba a la izquierda, enlace a trabajo arriba a la derecha, nombre gigante recortado por el borde inferior.
2. **Mosaico** a dos columnas: cada pieza muestra solo la imagen con el cliente superpuesto. Al pasar el ratón la imagen desaparece y queda el texto. El eslogan ocupa una celda de la segunda columna.
3. **Declaración**: la frase de posicionamiento a tamaño grande y un párrafo de contexto.
4. **Desfile**: dos columnas de imágenes sin texto que se desplazan en sentidos opuestos con el scroll.
5. **Índice completo** sobre negro: todos los proyectos en lista. Al pasar el ratón aparece la miniatura a la izquierda y el año y la disciplina a los lados. Es CSS puro, sin JavaScript.
6. **Pie**: correo, redes y ubicación.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | Toda la página principal, incluidas las portadas SVG |
| `proyecto-sal-de-garraf.html` | Plantilla de caso. Duplícala por proyecto |
| `styles.css` | Todos los estilos. Los colores están en `:root`, arriba del todo |
| `404.html` | Página de error |
| `img/` | Créala tú y mete ahí tus imágenes y vídeos |

## Lo primero que hay que cambiar

1. `celia muntaner` → tu nombre (portada, índice, cabeceras y `<title>`).
2. `hola@ejemplo.com` y los `href="#"` de redes.
3. `https://ejemplo.com` en `canonical` y `og:image`.
4. Los seis proyectos de prueba.

## El vídeo de portada

En `index.html`, dentro de `<header class="portada">`, hay un `<div class="portada__media">` con un SVG de relleno. Sustitúyelo entero por:

```html
<video class="portada__media" autoplay muted loop playsinline
       preload="metadata" poster="img/portada.webp">
  <source src="img/portada.webm" type="video/webm">
  <source src="img/portada.mp4"  type="video/mp4">
</video>
```

Reglas para que no destroce la carga:

- Bucle de 6 a 12 segundos, **sin audio**, recortado a 1280 px de ancho.
- Objetivo: **menos de 2 MB**. Con ffmpeg: `ffmpeg -i original.mov -vf scale=1280:-2 -an -c:v libx264 -crf 30 -preset slow portada.mp4`
- El `poster` es obligatorio: es lo que se ve mientras carga y en móviles con ahorro de datos.
- `autoplay` solo funciona si el vídeo está `muted`. No lo quites.

Si el vídeo pasa de 5 MB, no lo subas al repositorio: mételo en Vimeo y usa una imagen fija en la portada.

## Añadir un proyecto

1. **Portada SVG**: en `index.html` hay un bloque `<svg width="0" height="0">` con ocho `<symbol>`. Añade el tuyo con un `id` nuevo, o borra el bloque entero cuando tengas fotos reales y usa `<img>` dentro de `.pieza__marco`.
2. **Mosaico**: copia una `<figure class="pieza">` entera. Contiene el `.pieza__marco` (la imagen) y el `.pieza__reverso` (el texto que la sustituye al pasar el ratón).
3. **Índice**: copia un `<li>` de `.lista` con su año, nombre, disciplina y miniatura.
4. **Caso**: duplica `proyecto-sal-de-garraf.html`, renómbralo sin acentos ni espacios y actualiza los enlaces.

El mosaico tiene ocho celdas: seis piezas, el eslogan y la frase de cierre. Si añades o quitas piezas, procura mantener un número par para que las filas cuadren.

## El desfile de dos columnas

Es la sección `<section class="desfile">`. Cada columna lleva cuatro imágenes y un atributo `data-desfile` que indica su sentido: `sube` o `baja`. El script del final de `index.html` calcula cuánto ha avanzado la sección por la ventana y desplaza cada columna en sentido contrario.

Para cambiar la intensidad, ajusta la altura de `.desfile` en el CSS: cuanto más baja sea respecto a las imágenes, más recorrido tienen las columnas. Para añadir o quitar imágenes basta con meter o borrar `<figure>` dentro de cada columna; el script recalcula solo.

Si el visitante tiene activado el ahorro de movimiento en su sistema, el efecto se desactiva y las columnas se ven completas, una debajo de otra.

## Imágenes

- Exporta a **WebP**, lado largo máximo 2000 px.
- Pon siempre `width`, `height` y `loading="lazy"`.
- Objetivo: menos de 2 MB por página. Compruébalo en PageSpeed Insights.

## Publicar en GitHub Pages

1. Repositorio **público** llamado `tuusuario.github.io`.
2. Sube los archivos a la raíz, no dentro de una carpeta.
3. Settings → Pages → Source: `Deploy from a branch`, rama `main`, carpeta `/ (root)`.
4. Añade un archivo vacío `.nojekyll` en la raíz.

## Dominio propio

1. En el DNS del registrador: cuatro registros **A** para el dominio raíz apuntando a `185.199.108.153`, `185.199.109.153`, `185.199.110.153` y `185.199.111.153`, y un **CNAME** de `www` a `tuusuario.github.io`.
2. Settings → Pages → Custom domain. GitHub creará un archivo `CNAME`: no lo borres.
3. Espera al certificado y marca **Enforce HTTPS**.
