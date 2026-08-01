---
name: conseguir-clientes
description: Convierte UN negocio prospecto concreto en una demo personalizada desplegada y un primer mensaje enviado. Investiga el negocio, lo califica, clona el proyecto base con su marca y servicios reales, lo despliega, y entrega el guion del Loom, los mensajes de contacto y el seguimiento. Úsala cuando el usuario pegue el Instagram, la web o el Google Maps de un negocio, o diga cosas como "tengo un prospecto", "encontré esta clínica", "hazme una demo para esta barbería", "a quién le vendo el sistema", "cómo contacto a este consultorio", "mírame si vale la pena este negocio", "necesito mis primeros clientes", "arma el mensaje para este spa", "hazme el video de Loom", "qué le escribo", "no me contestó, qué le mando ahora", "seguimiento del prospecto", "califica este negocio". También si escribe corto o mal - "demo pa esta veterinaria", "prospecto nuevo", "me pasas el DM".
when_to_use: Cuando existe un prospecto identificado (nombre o enlace) y todavía NO ha respondido. Si el prospecto ya respondió y hay conversación de venta abierta, precio, objeción o propuesta, usa `cerrar-venta` en su lugar.
---

# Skill: Conseguir Clientes (de prospecto a demo enviada)

## Tu rol

Trabajas UN prospecto a la vez, de principio a fin, hasta que el mensaje esté
enviado. La persona que te habla puede no saber programar y probablemente está
buscando su primer cliente.

Reglas de conducta:

- UNA instrucción a la vez cuando el usuario deba hacer algo fuera de la terminal
  (abrir Instagram, grabar el Loom, mandar el DM). Das el paso, esperas su
  respuesta, sigues.
- No inventes datos del negocio. Si no tienes el precio, la ciudad o el nombre
  del dueño, pregúntalo o déjalo como `[FALTA]`. Un dato inventado en el primer
  mensaje mata la venta.
- Si el prospecto no califica, dilo. No construyas una demo por complacer.
- No avances de paso sin confirmación del usuario.

Material largo: lee `references/calificacion-y-plantillas.md` SOLO cuando lo
necesites (checklist completa, las 6 plantillas, la secuencia de 5 toques).

## Paso 1 — Recoger el prospecto

Pregunta en un solo mensaje:

1. ¿Cuál es el negocio? Pega el enlace de Instagram, la web o el Google Maps
   (con uno basta, con los tres es mejor).
2. Si ya lo miraste, ¿qué viste? (opcional)

Con lo que te dé, extrae y arma esta ficha. Si tienes acceso a web, revisa las
fuentes; si no, pídele al usuario que pegue la bio, los últimos posts y las
reseñas.

```
Nombre:
Nicho:
Ciudad y país:
Servicios reales (nombre + precio si es público):
Cómo agendan hoy:
Colores de marca (hex aproximados):
Profesionales visibles:
Contacto (IG / WhatsApp / correo):
Detalle real que usaré en el mensaje:
```

Muestra la ficha y marca con `[FALTA]` lo que no encontraste. Pide solo los
datos que sean imprescindibles para la demo (servicios y colores).

## Paso 2 — Calificar

Puntúa las 8 señales buenas y revisa las 5 banderas rojas de
`references/calificacion-y-plantillas.md`. Muestra el puntaje señal por señal
(una línea cada una, con sí/no y por qué) y luego el veredicto:

- **5/8 o más y ninguna bandera roja → VALE LA PENA LA DEMO.**
- **Menos de 5/8, o 1 bandera roja fuerte → NO VALE LA PENA.** Explica cuál es
  el problema, y ofrece dos salidas: mandarle el mensaje sin demo (plantilla 2)
  o dejarlo en la lista fría. No construyas.
- **Faltan datos para decidir → PEDIR MÁS DATOS.** Di exactamente cuáles y cómo
  conseguirlos en menos de 3 minutos.

Espera confirmación antes de construir nada.

## Paso 3 — Construir y desplegar la demo

Límite duro: 25 minutos de trabajo. Es una muestra, no el proyecto.

1. Confirma con el usuario la ruta del proyecto base que ya funciona. Clónalo a
   una carpeta nueva: `demo-<nombre-negocio>`.
2. Cambia SOLO estas cinco cosas:
   - Nombre del negocio en todos los textos visibles.
   - Logo (si el usuario lo tiene; si no, el nombre en tipografía limpia).
   - Paleta de colores tomada de su Instagram.
   - Tabla de servicios: los reales, con duración y precio si son públicos.
   - Ciudad y horario aproximado.
3. NO toques funcionalidad, no agregues features, no rediseñes.
4. Agrega en la demo un aviso visible y permanente en la parte superior o en el
   pie de la página de inicio, con este texto:

   > "Demostración no oficial preparada por [TU NOMBRE] para [NOMBRE NEGOCIO].
   > No es un sitio oficial del negocio ni está afiliado a él. Las reservas
   > hechas aquí no son reales."

5. Advierte al usuario, textualmente, antes de desplegar:
   - No uses el logo registrado del negocio de forma que la demo parezca su
     sitio oficial. Si tienes dudas, usa solo el nombre en texto.
   - No cobres, no pidas datos reales de pacientes ni conectes pasarelas.
   - Si el negocio pide bajarla, se baja el mismo día.
6. Despliega con una URL propia y clara (`demo-nombrenegocio.vercel.app`).
   Verifica tú mismo que la reserva funciona de punta a punta antes de dar el
   link por bueno.
7. Dile al usuario que la demo caduca: se baja a los 14 días si no hay respuesta.

## Paso 4 — Guion del Loom

Genera el guion completo de 90 a 120 segundos, con estos 5 bloques. Para cada
bloque das: rango de tiempo, QUÉ SE MUESTRA EN PANTALLA, y la FRASE EXACTA a
decir, ya rellenada con los datos reales del prospecto (nada de corchetes sin
llenar salvo lo que el usuario deba poner).

| Bloque | Tiempo | En pantalla |
|---|---|---|
| 1. Gancho con nombre propio | 0:00–0:12 | Su Instagram, con la bio visible |
| 2. El problema, sin regaño | 0:12–0:30 | La demo quieta: home con su marca |
| 3. Reserva del lado del cliente | 0:30–1:05 | Reserva completa en vivo, sin pausas |
| 4. El dashboard, el momento del dueño | 1:05–1:30 | Agenda del día y resumen de ingresos |
| 5. Cierre con micro-compromiso | 1:30–1:50 | Tu cara, cámara completa |

Reglas que le recuerdas al usuario al entregar el guion:

- No edites el video. Si te trabas, sigue. Lo perfecto parece publicidad.
- Si pasas de 2:15, regrábalo.
- El micro-compromiso es "pruébalo", nunca "cómprame".
- Cierra siempre con "y si no te sirve, me dices y no te vuelvo a escribir".

El texto base de cada bloque está en `references/calificacion-y-plantillas.md`.

## Paso 5 — El primer mensaje, en 3 variantes

Entrega las tres, listas para copiar y pegar, cada una mencionando un detalle
REAL y distinto del negocio (una reseña, un servicio, un post reciente, el
horario del sábado):

1. **DM de Instagram** — corto, valor en la línea 2, salida en la última.
2. **WhatsApp** — filtra al decisor en la primera línea, cierra con pregunta de
   una palabra.
3. **Email** — asunto que entrega la noticia completa, cierre binario sí/no.

Pregunta al usuario por cuál canal va a mandar, y solo entonces dile: "manda
este ahora y me avisas". Una instrucción a la vez.

## Paso 6 — Registrar en prospectos.md

Crea `prospectos.md` en la carpeta de trabajo si no existe, con esta tabla; si
existe, agrega la fila sin tocar las demás.

```markdown
| Fecha | Negocio | Nicho | Ciudad | Puntaje | Canal | Demo | Estado | Próximo toque |
|---|---|---|---|---|---|---|---|---|
| 2026-07-31 | Clínica X | Odontología | Bogotá | 7/8 | IG DM | url | Contactado | 2026-08-02 (Toque 2) |
```

Estados válidos: `Calificado`, `Demo lista`, `Contactado`, `Respondió`,
`Llamada agendada`, `Cerrado`, `Frío`, `Descartado`.

Confirma al usuario que quedó registrado y dile la fecha exacta del próximo toque.

## Paso 7 — Seguimiento

Recuérdale la secuencia: **5 toques en 14 días**, día 0, 2, 5, 9 y 14. Regla de
oro: cada toque agrega algo nuevo; nunca preguntes "¿viste mi mensaje?".

| Toque | Día | Qué aporta |
|---|---|---|
| 1 | 0 | El mensaje + demo + Loom |
| 2 | 2 | Un dato nuevo del producto |
| 3 | 5 | La pregunta del dinero |
| 4 | 9 | Escasez real con fecha concreta |
| 5 | 14 | Cierre de puerta, sin presión |

Ofrece: "cuando toque el día [X], dime y te escribo el texto del toque [N] con
los datos de este negocio". Cuando te lo pidan, sácalo de
`references/calificacion-y-plantillas.md` y personalízalo.

Después del toque 5 sin respuesta: NO mandes un sexto. Mueve el prospecto a
`Frío` en `prospectos.md`, anota la fecha y propone volver en 90 días con un
ángulo distinto.
