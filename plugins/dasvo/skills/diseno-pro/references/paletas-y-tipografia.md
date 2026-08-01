# Paletas y tipografía

Todo lo que necesitas para que un sistema de reservas se vea hecho por alguien que sabe. Los colores de aquí están calculados, no escogidos a ojo: cada valor de contraste que ves fue medido con la fórmula de luminancia relativa de WCAG y verificado contra los valores publicados por WebAIM.

---

## 1. Cómo se arma una paleta que no se ve amateur

### La regla: un color de marca, todo lo demás neutro

Una interfaz profesional casi siempre usa **un solo color con carácter** y lo rodea de grises. Ese color aparece en poquísimos sitios: el botón principal, el día seleccionado del calendario, el enlace activo, el borde de la tarjeta escogida. Nada más.

El resto de la pantalla —textos, fondos, bordes, separadores— es neutro. Cuando el 95% de lo que ves es neutro, ese 5% de color grita. Y eso es exactamente lo que quieres: que el ojo del cliente caiga solo en el botón de "Reservar".

### Por qué dos o tres colores fuertes te delatan

Cuando pones azul en el encabezado, verde en el botón de confirmar y naranja en las alertas, el usuario ya no sabe qué es importante. Todo compite. Y hay un problema peor: **si todo es importante, nada lo es**. El botón que quieres que aprieten pierde contra el banner morado de arriba.

Además, combinar colores es difícil: que dos colores saturados se lleven bien es suerte o años de oficio, mientras que un color con grises derivados de él siempre funciona. Y se nota el origen — las paletas amateur son colores sueltos de un generador, sin familia común.

Excepción legítima: los colores semánticos. Verde para éxito, ámbar para advertencia, rojo para error. Esos no son "colores de marca", son señales, y aparecen solo cuando hay algo que señalar.

### Cómo derivar tonos en vez de escoger colores sueltos

El error clásico es abrir un selector de color y sacar diez colores distintos. El método correcto es empezar con **un tono (hue)** y moverte solo en saturación y luminosidad.

Piensa en HSL (matiz, saturación, luminosidad):

1. Fijas el matiz. Ejemplo: 202 grados, un azul.
2. **El color de marca** es ese matiz con saturación alta (70-80%) y luminosidad media-baja (30-40%). La luminosidad la bajas hasta que el texto blanco encima pase 4.5:1.
3. **El hover** es el mismo matiz, 7-8 puntos menos de luminosidad.
4. **El tinte de selección** es el mismo matiz, saturación moderada, luminosidad 95-96%. Casi blanco, pero se nota que es de la familia.
5. **Los neutros** son el mismo matiz (o uno muy cercano) con saturación bajísima: 10-15%. Eso es lo que hace que tus grises no se vean sucios: no son grises puros, son grises teñidos del color de la marca. La diferencia es invisible por separado y evidente en conjunto.

Con ese método cada color que agregas ya está en armonía porque comparte matiz con todos los demás. No hay nada que "combinar".

### Los mínimos de contraste que sí existen

Antes de las paletas, la parte que la gente inventa. Los criterios reales de WCAG 2.1:

| Criterio | Nivel | Qué exige |
|---|---|---|
| 1.4.3 Contraste (mínimo) | **AA** | 4.5:1 para texto normal |
| 1.4.3 Contraste (mínimo) | **AA** | 3:1 para texto grande (24px, o 19px si está en negrilla) |
| 1.4.11 Contraste no textual | **AA** | 3:1 para componentes de interfaz y objetos gráficos informativos |
| 1.4.6 Contraste (mejorado) | AAA | 7:1 texto normal, 4.5:1 texto grande |
| 2.5.5 Tamaño del objetivo | **AAA** | objetivos táctiles de 44x44 px CSS |

Tres precisiones que la gente se salta:

- **Los 44x44 px son AAA en WCAG 2.1**, no AA. Es una buena práctica que deberías seguir siempre en móvil, pero no la presentes como "obligatorio por AA". (En WCAG 2.2 sí entró un criterio AA de tamaño de objetivo, el 2.5.8, y su mínimo son 24x24 px, no 44.)
- **El texto deshabilitado está exento** del 1.4.3. Un botón inactivo puede tener poco contraste sin incumplir. Aun así, que se pueda leer.
- **Los logotipos también están exentos.** No rompas el logo del cliente para "cumplir".

Y una regla que no es de contraste pero se confunde con esto: el criterio **1.4.1 (Uso del color, AA)** dice que el color no puede ser el único medio para transmitir información. Un día del calendario marcado solo con color de fondo no cumple; necesita además texto, un ícono o `aria-*`.

### Cómo se mide (y contra qué)

El contraste siempre es entre **dos colores concretos**, no entre un color y "el fondo en general". Si tu texto gris vive sobre blanco en unas pantallas y sobre el gris muy claro de una tarjeta en otras, tienes que medirlo contra el **más oscuro de los dos fondos**. Ese es el que manda.

Por eso en las tablas de abajo cada texto lleva dos valores: contra `#FFFFFF` y contra `--fondo-claro` (la superficie más oscura donde puede aparecer). Todas las paletas están construidas para que **el peor de los dos casos** siga pasando AA.

---

## 2. Diez paletas listas, por nicho

**Cómo leer las tablas.** Cada paleta tiene el mismo esqueleto de once tokens. La columna de contraste dice el valor medido y contra qué se midió:

- `blanco encima` → texto blanco sobre ese color (botón primario). Mínimo 4.5:1.
- `vs #FFF` → ese color como texto sobre fondo blanco. Mínimo 4.5:1.
- `vs claro` → ese color sobre `--fondo-claro`, el peor caso. Mínimo 4.5:1 para texto, 3:1 para bordes.
- Los tokens de fondo no llevan contraste porque son superficies, no contenido.

Los tres colores semánticos son **los mismos en las diez paletas** y están al final de esta sección. Eso es a propósito: el rojo de error no debe cambiar de un proyecto a otro.

---

### 1. Consultorio odontológico

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#13699A` | 5.97 blanco encima · 5.97 vs #FFF |
| `--marca-oscuro` | `#0B537C` | 8.26 blanco encima |
| `--marca-claro` | `#EDF5FA` | superficie de selección |
| `--texto-fuerte` | `#192329` | 15.98 vs #FFF · 14.17 vs claro |
| `--texto-cuerpo` | `#3E4A54` | 9.08 vs #FFF · 8.05 vs claro |
| `--texto-suave` | `#5D707E` | 5.14 vs #FFF · 4.56 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F7F9FB` | — |
| `--fondo-claro` | `#EDF2F5` | — |
| `--borde` | `#7A8E9C` | 3.40 vs #FFF · 3.01 vs claro |
| `--borde-suave` | `#E1E8EC` | decorativo, no informativo |

Por qué este azul: es el color que ya está en el consultorio (la bata, el instrumental, la luz). Se ve limpio sin parecer hospital, y no compite con las fotos de antes y después, que son casi siempre blancas y rosadas.

---

### 2. Barbería

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#2C3F59` | 10.70 blanco encima · 10.70 vs #FFF |
| `--marca-oscuro` | `#1C2D42` | 13.97 blanco encima |
| `--marca-claro` | `#F0F3F7` | superficie de selección |
| `--texto-fuerte` | `#1A2028` | 16.39 vs #FFF · 14.35 vs claro |
| `--texto-cuerpo` | `#404851` | 9.28 vs #FFF · 8.12 vs claro |
| `--texto-suave` | `#636E7E` | 5.17 vs #FFF · 4.53 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F7F8FA` | — |
| `--fondo-claro` | `#EDF0F5` | — |
| `--borde` | `#7E8A9A` | 3.51 vs #FFF · 3.07 vs claro |
| `--borde-suave` | `#E2E6EC` | decorativo, no informativo |

Por qué este azul casi negro: las fotos de cortes son de piel, pelo y madera, y cualquier color saturado se pelea con ellas. Este tono se comporta casi como negro, deja que las fotos manden, y el botón se ve sólido incluso en una pantalla barata con los colores lavados.

---

### 3. Spa

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#2B6E4F` | 6.09 blanco encima · 6.09 vs #FFF |
| `--marca-oscuro` | `#1D563B` | 8.58 blanco encima |
| `--marca-claro` | `#EEF9F4` | superficie de selección |
| `--texto-fuerte` | `#1A2822` | 15.32 vs #FFF · 13.73 vs claro |
| `--texto-cuerpo` | `#41514A` | 8.40 vs #FFF · 7.53 vs claro |
| `--texto-suave` | `#5D746A` | 5.03 vs #FFF · 4.51 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F7FAF9` | — |
| `--fondo-claro` | `#EDF4F2` | — |
| `--borde` | `#779287` | 3.36 vs #FFF · 3.01 vs claro |
| `--borde-suave` | `#E2EBE8` | decorativo, no informativo |

Por qué este verde: es oscuro, no pastel. El error típico en spa es usar verdes y beiges clarísimos que no dan contraste y dejan la pantalla ilegible con el sol encima.

---

### 4. Clínica estética

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#843351` | 8.16 blanco encima · 8.16 vs #FFF |
| `--marca-oscuro` | `#6D243F` | 10.64 blanco encima |
| `--marca-claro` | `#F9EEF2` | superficie de selección |
| `--texto-fuerte` | `#281A21` | 16.67 vs #FFF · 14.47 vs claro |
| `--texto-cuerpo` | `#514148` | 9.55 vs #FFF · 8.29 vs claro |
| `--texto-suave` | `#7F6672` | 5.19 vs #FFF · 4.51 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#FAF7F9` | — |
| `--fondo-claro` | `#F4EDF1` | — |
| `--borde` | `#9B828E` | 3.51 vs #FFF · 3.05 vs claro |
| `--borde-suave` | `#EBE2E6` | decorativo, no informativo |

Por qué este vino: el rosa claro es la trampa de este nicho. No da contraste, se ve barato y hace que la clínica parezca un salón de fiestas infantiles.

---

### 5. Veterinaria

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#187C72` | 5.04 blanco encima · 5.04 vs #FFF |
| `--marca-oscuro` | `#0E5F57` | 7.52 blanco encima |
| `--marca-claro` | `#EDFAF9` | superficie de selección |
| `--texto-fuerte` | `#1A2828` | 15.24 vs #FFF · 13.68 vs claro |
| `--texto-cuerpo` | `#415150` | 8.34 vs #FFF · 7.49 vs claro |
| `--texto-suave` | `#5C7372` | 5.06 vs #FFF · 4.54 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F7FAFA` | — |
| `--fondo-claro` | `#EDF4F4` | — |
| `--borde` | `#769190` | 3.37 vs #FFF · 3.03 vs claro |
| `--borde-suave` | `#E2EBEB` | decorativo, no informativo |

Por qué este verde azulado: se lee como salud sin ser el azul de hospital, y funciona bien de fondo para fotos de mascotas, que son de todos los colores imaginables. Un color muy cálido se pelearía con los pelajes naranjas y marrones.

---

### 6. Fisioterapia

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#303EA6` | 8.88 blanco encima · 8.88 vs #FFF |
| `--marca-oscuro` | `#222F8E` | 11.26 blanco encima |
| `--marca-claro` | `#EDEFFA` | superficie de selección |
| `--texto-fuerte` | `#1A1D28` | 16.80 vs #FFF · 14.61 vs claro |
| `--texto-cuerpo` | `#404351` | 9.81 vs #FFF · 8.54 vs claro |
| `--texto-suave` | `#666C82` | 5.21 vs #FFF · 4.53 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F7F8FA` | — |
| `--fondo-claro` | `#EDEFF5` | — |
| `--borde` | `#84899F` | 3.47 vs #FFF · 3.01 vs claro |
| `--borde-suave` | `#E2E4EC` | decorativo, no informativo |

Por qué este índigo: es distinto del azul clínico sin irse al morado. Da sensación de movimiento y precisión, y tiene un contraste altísimo con blanco (8.88:1), que ayuda cuando el paciente entra a reservar desde el celular en la sala de espera con la pantalla al mínimo.

---

### 7. Estudio de tatuajes

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#202327` | 15.78 blanco encima · 15.78 vs #FFF |
| `--marca-oscuro` | `#0E1013` | 19.05 blanco encima |
| `--marca-claro` | `#F2F3F5` | superficie de selección |
| `--texto-fuerte` | `#1C1F26` | 16.49 vs #FFF · 14.45 vs claro |
| `--texto-cuerpo` | `#44474D` | 9.32 vs #FFF · 8.16 vs claro |
| `--texto-suave` | `#686D76` | 5.20 vs #FFF · 4.56 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F7F8FA` | — |
| `--fondo-claro` | `#EEF0F4` | — |
| `--borde` | `#858A93` | 3.47 vs #FFF · 3.04 vs claro |
| `--borde-suave` | `#E3E6EA` | decorativo, no informativo |

Por qué casi negro: el portafolio es la marca. Las piezas son negro, gris y color saturado sobre piel; cualquier color de interfaz que metas ahí se ve como si compitiera con el trabajo del artista.

---

### 8. Salón de uñas

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#8C2C72` | 7.73 blanco encima · 7.73 vs #FFF |
| `--marca-oscuro` | `#731F5C` | 10.10 blanco encima |
| `--marca-claro` | `#F9EEF6` | superficie de selección |
| `--texto-fuerte` | `#281A25` | 16.60 vs #FFF · 14.43 vs claro |
| `--texto-cuerpo` | `#51414D` | 9.49 vs #FFF · 8.25 vs claro |
| `--texto-suave` | `#7E6579` | 5.22 vs #FFF · 4.54 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#FAF7FA` | — |
| `--fondo-claro` | `#F4EDF3` | — |
| `--borde` | `#9B8296` | 3.48 vs #FFF · 3.03 vs claro |
| `--borde-suave` | `#EBE2EA` | decorativo, no informativo |

Por qué este magenta oscuro: el catálogo del salón es una galería de esmaltes de todos los colores. Un magenta claro se confundiría con el producto; oscurecido funciona como marco.

---

### 9. Taller mecánico

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#99460F` | 6.49 blanco encima · 6.49 vs #FFF |
| `--marca-oscuro` | `#7A3608` | 8.90 blanco encima |
| `--marca-claro` | `#FAF2ED` | superficie de selección |
| `--texto-fuerte` | `#28211B` | 15.87 vs #FFF · 14.10 vs claro |
| `--texto-cuerpo` | `#504841` | 8.96 vs #FFF · 7.96 vs claro |
| `--texto-suave` | `#776C62` | 5.11 vs #FFF · 4.55 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#FAF9F7` | — |
| `--fondo-claro` | `#F4F1EE` | — |
| `--borde` | `#95897E` | 3.41 vs #FFF · 3.03 vs claro |
| `--borde-suave` | `#EBE6E2` | decorativo, no informativo |

Por qué este naranja quemado: el naranja brillante típico de taller (`#FF6600` y compañía) no llega ni a 3:1 con blanco encima, así que el botón principal queda ilegible. Bajado a quemado conserva la referencia industrial y llega a 6.49:1.

---

### 10. Consultorio de psicología

| Token | Hex | Contraste medido |
|---|---|---|
| `--marca` | `#466B2E` | 6.17 blanco encima · 6.17 vs #FFF |
| `--marca-oscuro` | `#34541F` | 8.63 blanco encima |
| `--marca-claro` | `#F3F8EF` | superficie de selección |
| `--texto-fuerte` | `#1F281B` | 15.24 vs #FFF · 13.70 vs claro |
| `--texto-cuerpo` | `#465041` | 8.45 vs #FFF · 7.60 vs claro |
| `--texto-suave` | `#65735E` | 5.04 vs #FFF · 4.53 vs claro |
| `--fondo` | `#FFFFFF` | — |
| `--fondo-suave` | `#F8FAF7` | — |
| `--fondo-claro` | `#F0F4EE` | — |
| `--borde` | `#819178` | 3.36 vs #FFF · 3.02 vs claro |
| `--borde-suave` | `#E5EBE2` | decorativo, no informativo |

Por qué este verde musgo: es un color que no llama la atención, y en este nicho eso es la función. La persona que entra a reservar quiere hacerlo rápido y sin espectáculo.

---

### Colores semánticos (iguales en las diez paletas)

| Token | Hex | Fondo del token | Contraste |
|---|---|---|---|
| `--exito` | `#0E8142` | `#E9F9F0` | 4.96 vs #FFF · 4.55 sobre su fondo |
| `--alerta` | `#9D6004` | `#FDF1E0` | 5.11 vs #FFF · 4.58 sobre su fondo |
| `--error` | `#C91D28` | `#FCEBEC` | 5.69 vs #FFF · 4.94 sobre su fondo |

Los fondos claros (`#E9F9F0`, `#FDF1E0`, `#FCEBEC`) son para las cajas de mensaje. El color fuerte va en el texto y en el ícono de esa caja. Nunca uses el color fuerte de fondo con texto blanco encima para mensajes largos: cansa.

Nota sobre el ámbar: es imposible tener un amarillo brillante que pase 4.5:1 sobre blanco. El `#9D6004` parece marrón mostaza suelto y ámbar cuando lo ves como texto de alerta al lado de su fondo. Si necesitas amarillo brillante, úsalo solo como fondo o como banda decorativa, nunca como texto.

---

## 3. Tipografía sin instalar nada

### La pila del sistema

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             Helvetica, Arial, sans-serif;
```

Eso es todo. No descargas nada. Cada aparato agarra la primera fuente de la lista que tenga instalada: San Francisco en iPhone y Mac, Segoe UI en Windows, Roboto en Android. `Helvetica` y `Arial` son la red de seguridad y `sans-serif` el último recurso.

Por qué para estos proyectos es mejor que traer una de Google:

- **Carga instantánea.** La fuente ya está en el aparato. Cero peticiones de red, cero espera.
- **Se ve nativa.** El cliente que entra desde un iPhone ve una pantalla que se parece a las demás apps de su iPhone. Eso se lee como "esto es serio" sin que sepa por qué.
- **No hay parpadeo.** Una fuente web cargada mal produce el salto en el que el texto aparece con una fuente y medio segundo después cambia a otra (FOUT) o directamente no aparece (FOIT). Con la pila del sistema no existe ese estado.
- **Cero costo con mala señal.** Una fuente de Google son entre 15 y 40 KB por peso. Si cargas regular, semibold y bold ya vas por 100 KB antes de mostrar una letra. En 3G en una zona con mala cobertura eso es un segundo o dos de pantalla en blanco, justo cuando la persona está decidiendo si reserva o cierra.

### La escala

Seis tamaños. Ni uno más.

| Nombre | Tamaño | Interlineado | Peso | Uso |
|---|---|---|---|---|
| `title` | 32px | 40px (1.25) | 700 | Título de la pantalla. Uno por página. |
| `h1` | 24px | 32px (1.33) | 700 | Sección grande. |
| `h2` | 20px | 28px (1.4) | 600 | Subsección, nombre de servicio en tarjeta. |
| `h3` | 17px | 24px (1.4) | 600 | Etiqueta de grupo, encabezado de tabla. |
| `cuerpo` | 16px | 24px (1.5) | 400 | Todo el texto normal, campos de formulario, botones. |
| `chica` | 14px | 20px (1.43) | 400 | Ayuda bajo un campo, metadatos, notas. |

Tres reglas que van con la escala:

1. **El cuerpo nunca baja de 16px.** En iOS, un `<input>` con menos de 16px hace que Safari haga zoom automático al enfocarlo. La pantalla salta, el usuario se pierde. Esto solo lo arreglas con 16px.
2. **Nada por debajo de 14px.** Si te dan ganas de poner 12px es porque estás metiendo información que no cabe. Quítala, no la encojas.
3. **Máximo cuatro tamaños por pantalla.** Un título, un subtítulo, cuerpo y chica. Si necesitas cinco, tu pantalla está haciendo dos trabajos y hay que partirla.

Y una regla de jerarquía: **la diferencia entre niveles se hace con peso y espacio antes que con tamaño.** Un `h3` de 17px en peso 600 con 32px de aire encima se lee como un encabezado clarísimo. Subirlo a 22px no lo mejora, solo lo hace ruidoso.

### Si de todas formas quieres cargar una fuente

Tres combinaciones que funcionan, de menos a más riesgo:

| Combinación | Titulares | Cuerpo | Cuándo |
|---|---|---|---|
| Un solo peso variable | Inter (variable) | Inter (variable) | Lo más seguro. Un archivo cubre todos los pesos. |
| Serif + sistema | Fraunces 600 solo en `title` y `h1` | pila del sistema | Spa, estética, psicología. Cargas un peso, no seis. |
| Geométrica neutra | Manrope 700 | Manrope 400 | Fisioterapia, taller, veterinaria. |

El costo: cada peso que cargues son 15-40 KB y una petición extra que compite con las imágenes. En una conexión mala eso se traduce en texto invisible o parpadeante en el peor momento. Si cargas una fuente, **carga como máximo dos pesos**.

Cómo cargarla sin bloquear el renderizado, en Next.js:

```js
// app/layout.js
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',          // muestra la del sistema y cambia al llegar
  variable: '--fuente',
  weight: ['400', '700'],   // solo dos pesos
})

export default function RootLayout({ children }) {
  return (
    <html lang="es" className={inter.variable}>
      <body>{children}</body>
    </html>
  )
}
```

`next/font` descarga la fuente en el build y la sirve desde tu propio dominio, así que evita el viaje a los servidores de Google. `display: 'swap'` garantiza que el texto sea visible desde el primer momento con la fuente del sistema. Y en el CSS declaras siempre el respaldo:

```css
body { font-family: var(--fuente), -apple-system, BlinkMacSystemFont,
                    "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
```

Nunca uses `display: block` ni `optional` sin saber lo que haces: el primero esconde el texto hasta que la fuente llegue, el segundo puede no cargarla nunca.

---

## 4. Bloque de tokens listo para copiar

Este ejemplo usa la paleta de consultorio odontológico. Para cambiar de nicho, reemplaza los nueve hex del bloque de color por los de la tabla que quieras: el resto no se toca.

```css
:root {
  /* ---------- COLOR DE MARCA ---------- */
  --marca:          #13699A;  /* botón primario. Blanco encima: 5.97:1 */
  --marca-oscuro:   #0B537C;  /* hover y activo.  Blanco encima: 8.26:1 */
  --marca-claro:    #EDF5FA;  /* fondo de la opción seleccionada */

  /* ---------- TEXTO ----------
     Los ratios son contra blanco y contra --fondo-claro (el peor caso). */
  --texto-fuerte:   #192329;  /* títulos.   15.98:1 / 14.17:1 */
  --texto-cuerpo:   #3E4A54;  /* párrafos.   9.08:1 /  8.05:1 */
  --texto-suave:    #5D707E;  /* ayudas.     5.14:1 /  4.56:1 */

  /* ---------- SUPERFICIES ---------- */
  --fondo:          #FFFFFF;  /* página */
  --fondo-suave:    #F7F9FB;  /* tarjetas, campos deshabilitados */
  --fondo-claro:    #EDF2F5;  /* zonas agrupadas, cabecera de tabla */

  /* ---------- BORDES ---------- */
  --borde:          #7A8E9C;  /* borde de campo. 3.40:1 / 3.01:1 → cumple 1.4.11 */
  --borde-suave:    #E1E8EC;  /* separadores decorativos, sin exigencia */

  /* ---------- SEMÁNTICOS (iguales en todos los proyectos) ---------- */
  --exito:          #0E8142;  --exito-fondo:  #E9F9F0;  /* 4.55:1 sobre su fondo */
  --alerta:         #9D6004;  --alerta-fondo: #FDF1E0;  /* 4.58:1 sobre su fondo */
  --error:          #C91D28;  --error-fondo:  #FCEBEC;  /* 4.94:1 sobre su fondo */

  /* ---------- TIPOGRAFÍA ---------- */
  --fuente: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
            Helvetica, Arial, sans-serif;

  --t-title:  2rem;      --lh-title:  2.5rem;    /* 32 / 40 · peso 700 */
  --t-h1:     1.5rem;    --lh-h1:     2rem;      /* 24 / 32 · peso 700 */
  --t-h2:     1.25rem;   --lh-h2:     1.75rem;   /* 20 / 28 · peso 600 */
  --t-h3:     1.0625rem; --lh-h3:     1.5rem;    /* 17 / 24 · peso 600 */
  --t-cuerpo: 1rem;      --lh-cuerpo: 1.5rem;    /* 16 / 24 · peso 400 */
  --t-chica:  0.875rem;  --lh-chica:  1.25rem;   /* 14 / 20 · peso 400 */

  /* ---------- ESPACIO (escala de 4) ---------- */
  --e1: 4px;  --e2: 8px;  --e3: 12px; --e4: 16px;
  --e5: 24px; --e6: 32px; --e7: 48px; --e8: 64px;

  /* ---------- FORMA Y SOMBRA ---------- */
  --radio:       8px;
  --radio-chico: 6px;
  --sombra:      0 1px 2px rgba(16, 24, 32, .06),
                 0 2px 8px rgba(16, 24, 32, .06);
  --alto-toque:  44px;   /* objetivo táctil. WCAG 2.1 SC 2.5.5 es AAA */
}

body {
  font-family: var(--fuente);
  font-size: var(--t-cuerpo);
  line-height: var(--lh-cuerpo);
  color: var(--texto-cuerpo);
  background: var(--fondo);
  -webkit-text-size-adjust: 100%;
}

h1, h2, h3 { color: var(--texto-fuerte); margin: 0 0 var(--e3); }
h1 { font-size: var(--t-h1); line-height: var(--lh-h1); font-weight: 700; }
h2 { font-size: var(--t-h2); line-height: var(--lh-h2); font-weight: 600; }
h3 { font-size: var(--t-h3); line-height: var(--lh-h3); font-weight: 600; }

/* Foco visible en todo lo que se pueda enfocar (WCAG 2.4.7, AA) */
:focus-visible {
  outline: 3px solid var(--marca);
  outline-offset: 2px;
  border-radius: var(--radio-chico);
}
```

Si usas Tailwind, mete los mismos valores en `theme.extend.colors` de `tailwind.config.js` y consúmelos como `bg-marca`, `text-cuerpo`, etc. Lo importante no es la herramienta: es que ningún hex suelto aparezca nunca en un componente.

---

## 5. Los ocho errores que más delatan un proyecto amateur

**1. Gris claro para el texto secundario.**
El error: poner `#999999` o `#AAAAAA` porque "se ve más suave". `#999` sobre blanco da 2.85:1 y no cumple AA.
Por qué se nota: en cuanto alguien abre la página con sol encima o desde una pantalla vieja, esos textos desaparecen. Se lee como descuido.
La corrección: usa `--texto-suave` de la paleta y verifica contra el fondo más oscuro donde vaya a aparecer. En todas las paletas de arriba el peor caso queda por encima de 4.5:1.

**2. Texto blanco sobre un color de marca brillante.**
El error: naranja `#FF6600`, amarillo, verde lima o cyan con letra blanca encima. `#FF6600` con blanco da 2.9:1.
Por qué se nota: el botón principal —justo el que quieres que aprieten— es lo peor leído de la pantalla.
La corrección: oscurece el color de marca hasta que el blanco pase 4.5:1, o pon texto oscuro encima en vez de blanco. Nunca dejes el hex del logo tal cual si no pasa.

**3. Más de un color fuerte compitiendo.**
El error: encabezado azul, botón verde, insignia naranja, enlaces morados.
Por qué se nota: no hay jerarquía. El ojo no sabe adónde ir y la pantalla se ve como una plantilla de 2011.
La corrección: un color de marca, neutros para todo lo demás, y los semánticos solo cuando hay algo que señalar.

**4. Grises puros junto a un color saturado.**
El error: `#F5F5F5` y `#666666` al lado de un azul intenso.
Por qué se nota: el gris puro se ve sucio o verdoso al lado de un color saturado, y el conjunto parece armado con piezas de sitios distintos.
La corrección: tiñe los neutros con el mismo matiz de la marca a 10-15% de saturación. Es lo que hacen todas las paletas de arriba.

**5. Demasiados tamaños de letra.**
El error: 13px, 15px, 17px, 18px, 21px, 26px en la misma pantalla, cada uno decidido en el momento.
Por qué se nota: no hay ritmo. Se siente improvisado aunque nadie sepa señalar por qué.
La corrección: seis tamaños en total en todo el proyecto, máximo cuatro por pantalla, y siempre desde los tokens.

**6. Interlineado pegado en párrafos.**
El error: `line-height: 1.2` en texto de cuerpo, o dejarlo en el valor por defecto del navegador.
Por qué se nota: los bloques se ven apretados y cuestan de leer, sobre todo en móvil con líneas cortas.
La corrección: 1.5 en cuerpo, 1.4 en subtítulos, 1.25 en títulos grandes. Cuanto más grande la letra, más apretado puede ir.

**7. Todo en negrilla, o títulos que solo son "más grandes".**
El error: párrafos enteros en 700, o al revés, un `h2` que es cuerpo de 20px sin cambio de peso.
Por qué se nota: la negrilla es un recurso de énfasis; si todo lo tiene, deja de significar algo. Y un encabezado sin peso ni aire no se lee como encabezado.
La corrección: cuerpo en 400, encabezados en 600-700, y la separación entre secciones con espacio (`--e6`), no con más puntos de tamaño.

**8. Quitar el `outline` del foco sin poner nada en su lugar.**
El error: `*:focus { outline: none; }` porque "el borde azul se ve feo".
Por qué se nota: quien navega con teclado —y quien usa lector de pantalla— pierde por completo el rastro de dónde está. En un flujo de reserva con calendario eso es fatal, y además rompe el criterio 2.4.7 (Foco visible, AA).
La corrección: reemplázalo siempre. `:focus-visible { outline: 3px solid var(--marca); outline-offset: 2px; }` se ve bien, solo aparece al navegar con teclado, y cumple.
