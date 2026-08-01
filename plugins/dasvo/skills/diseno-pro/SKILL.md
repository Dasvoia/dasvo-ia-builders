---
name: diseno-pro
description: "Hace que el sistema se vea de agencia y no de proyecto de fin de semana, y que lo pueda usar cualquiera. Define los tokens de color, tipografía y espaciado antes de tocar componentes, arregla la jerarquía de cada pantalla, verifica el contraste contra WCAG AA con números reales, revisa que funcione con teclado y en celular, y reescribe los textos de la interfaz. Es lo que separa un sistema que se vende por 300 dólares de uno que se vende por 1.000."
when_to_use: "Úsala cuando el sistema ya funcione y toque hacerlo ver bien, o cuando el usuario diga cosas como \"se ve feo\", \"se ve muy simple\", \"parece hecho por un principiante\", \"no se ve profesional\", \"mejora el diseño\", \"hazlo más bonito\", \"que se vea premium\", \"los colores no combinan\", \"se ve mal en el celular\", \"el cliente dijo que no le gustó como se ve\", \"revisa el diseño\", \"critica esta pantalla\", \"esto es accesible\", \"contraste\", \"no se lee bien\", \"el texto es muy claro\", \"qué le pongo a este botón\", \"cómo redacto el error\", \"paleta de colores\", \"tipografía\", \"UI\", \"UX\", \"diseño\". También ANTES de grabar una demo o de entregar, porque lo que se ve es lo que se cobra."
---

# Skill: Diseño profesional de la interfaz

## Tu rol

El sistema ya funciona. Ahora tiene que verse como algo por lo que un dueño de
negocio paga mil dólares sin discutir, y tiene que poder usarlo la señora de 62
años que va al consultorio.

No inventes estilo. Sigue este orden, que es el que usan los equipos de diseño
de verdad: primero los valores, después los componentes, después las pantallas,
y al final el texto.

Reglas de conducta:

- **Nunca cambies varias cosas a la vez y digas "quedó mejor".** Un cambio, una
  razón, y muéstrale al usuario el antes y el después.
- **Todo color, tamaño y espacio sale de un token.** Si te encuentras
  escribiendo un `#hex` o un `px` suelto dentro de un componente, para: ese
  valor va arriba, en el token.
- **El contraste se calcula, no se estima.** Nunca digas "se ve bien" sobre un
  color. Da el número.
- **Lo que no se puede usar con el teclado, está roto.** Aunque se vea bonito.

## Paso 0 — Diagnóstico en 2 segundos

Antes de tocar nada, mira la pantalla como si fuera la primera vez y responde
estas tres, en voz alta, al usuario:

1. ¿Qué es lo primero que te jala el ojo? ¿Es lo que debería ser?
2. ¿Se entiende de qué se trata esto sin leer nada?
3. ¿Cuál es la acción principal y se ve como la acción principal?

Si alguna respuesta es floja, el problema es de jerarquía y no de colores.
Arregla eso primero: cambiar la paleta de una pantalla mal jerarquizada es
pintar una pared torcida.

## Paso 1 — Los tokens, antes que nada

Define esto una sola vez, arriba del CSS, y no vuelvas a escribir un valor
suelto en ningún lado.

```css
:root{
  /* texto: del más fuerte al más suave */
  --tx-fuerte:#0d1a23;
  --tx-cuerpo:#39485a;
  --tx-suave:#566673;

  /* marca: uno principal y sus variantes */
  --marca:#1a5479;
  --marca-viva:#1e5f8a;
  --marca-noche:#0b2c42;

  /* estado */
  --exito:#217a58;
  --alerta:#8a5a12;
  --error:#a1332b;

  /* superficie */
  --sup:#ffffff;
  --sup-2:#f4f8fb;
  --sup-3:#e9f1f6;
  --borde:#d3e0e9;        /* decorativo */
  --borde-ui:#8596a1;     /* 3.05:1 — bordes de campos, obligatorio */

  /* espaciado: escala de 4, sin valores intermedios inventados */
  --e1:4px;  --e2:8px;  --e3:12px; --e4:16px; --e5:24px;
  --e6:32px; --e7:48px; --e8:64px; --e9:96px;

  /* radio */
  --r1:6px; --r2:10px; --r3:16px; --r4:999px;

  /* elevacion */
  --sombra-1:0 1px 2px rgba(13,26,35,.06);
  --sombra-2:0 4px 16px rgba(13,26,35,.09);
}
```

**La escala de espaciado es lo que más se nota y lo que nadie hace.** Un
proyecto amateur tiene `padding: 13px`, `margin: 7px`, `gap: 22px`. Uno
profesional solo usa valores de la escala. Cámbialo y la pantalla se ve
ordenada sin que nadie sepa explicar por qué.

## Paso 2 — Verifica el contraste con números

**Obligatorio. No lo saltes.** Corre esto y pega el resultado en el chat:

```
${CLAUDE_SKILL_DIR}/scripts/contraste.py
```

Si no puedes ejecutarlo, calcula la razón de contraste tú y da el número.

Los mínimos de WCAG 2.1 nivel AA, que es el estándar que se exige:

| Qué | Mínimo |
|---|---|
| Texto normal sobre su fondo | 4.5 : 1 |
| Texto grande (24px o 19px en negrilla) | 3 : 1 |
| Bordes de campos, íconos que informan | 3 : 1 |

**El error más común, con diferencia:** grises tipo `#6b7c8a` o `#888` para
texto secundario. Se ven elegantes en tu monitor y son ilegibles al sol, en un
celular viejo o para alguien de 60 años. Ese gris da 4.3:1 y **falla**.

Cuando encuentres uno que falla, oscurécelo hasta que pase y dilo así:
"el gris de las descripciones daba 4.3:1, lo bajé a #566673 que da 5.9:1".

## Paso 3 — Jerarquía de cada pantalla

Recorre pantalla por pantalla:

1. **Una sola acción principal por pantalla.** Si hay dos botones que compiten,
   uno se vuelve secundario (fondo transparente, borde, o solo texto).
2. **Tamaño de letra: máximo cuatro en toda la pantalla.** Título, subtítulo,
   cuerpo, y letra chica. Más que eso se ve desordenado.
3. **El espacio en blanco separa, las líneas no.** Antes de meter un borde,
   prueba con más espacio. Casi siempre queda mejor.
4. **Agrupa las listas largas.** Una lista de doce cosas seguidas no se lee:
   se escanea y se abandona. Tres grupos de cuatro con su encabezado sí se lee.
   Este es el arreglo que más rinde por minuto invertido.
5. **Lo importante arriba y grande.** En un sistema de reservas: el servicio y
   la fecha mandan; el aviso de privacidad va abajo y en letra chica.

## Paso 4 — Que se pueda usar de verdad

Verifica cada punto y marca [OK] o [FALLA]:

- [ ] Todo lo que se puede clicar mide **44 × 44 píxeles** o más. Los enlaces
      dentro de un párrafo están exentos. Dato exacto para que no lo digas mal
      delante de un cliente: los 44 px son criterio AAA (WCAG 2.1, 2.5.5); el
      mínimo AA de WCAG 2.2 son 24 px. Apunta a 44 de todos modos, porque es lo
      que de verdad se alcanza con el pulgar.
- [ ] Se puede recorrer toda la pantalla con la tecla Tab, en orden lógico.
- [ ] El elemento enfocado **se ve**. Un anillo grueso, no el punteado gris del
      navegador y jamás `outline:none` sin reemplazo.
- [ ] Todos los campos tienen etiqueta visible. El texto de adentro
      (placeholder) **no es una etiqueta**: desaparece al escribir.
- [ ] Los errores dicen qué pasó, por qué y cómo se arregla.
- [ ] Las imágenes que informan tienen texto alternativo; las decorativas van
      con `alt=""`.
- [ ] La página se deja hacer zoom al 200% sin que se rompa.
- [ ] Hay `prefers-reduced-motion` para quien se marea con las animaciones.
- [ ] La información nunca se transmite solo con color (rojo/verde). Siempre
      hay además texto o un ícono.

Si tienes navegador disponible, corre una auditoría automática con axe-core y
reporta el número exacto de violaciones. Atrapa cerca de un tercio de los
problemas; el resto sale de esta lista.

## Paso 5 — Celular primero, de verdad

El paciente reserva desde el celular, casi siempre en la calle y con una mano.

- [ ] Probado a **390 px de ancho**. Nada se sale ni obliga a rodar de lado.
- [ ] Los botones se alcanzan con el pulgar: lo importante en la mitad de
      abajo, no arriba.
- [ ] El teclado no tapa el campo que se está llenando.
- [ ] El tipo de teclado correcto en cada campo: `type="tel"` para el celular,
      `type="email"` para el correo. Ahorra frustración real.
- [ ] Carga rápido con mala señal: sin fuentes pesadas, sin librerías enormes,
      imágenes comprimidas.

## Paso 6 — Los textos de la interfaz

El texto es diseño. Recórrelo con estas reglas:

**Botones:** empiezan con un verbo y dicen qué va a pasar.
"Confirmar mi cita", no "Enviar". "Ver mi agenda", no "Aceptar".

**Errores:** qué pasó, por qué, y qué hacer.
Mal: "Error de validación". Bien: "Esa hora ya la tomaron. Escoge otra de las
que quedan disponibles abajo."

**Estados vacíos:** qué es esto, por qué está vacío, y cómo se llena.
Mal: "Sin resultados". Bien: "No tienes citas para hoy. Cuando alguien reserve,
aparece aquí."

**Confirmaciones:** que se entienda la consecuencia y que los botones digan la
acción. "¿Cancelar la cita de Ana del jueves 3:00 p.m.? Le llega un aviso." con
botones "Cancelar la cita" y "Dejarla como está", nunca "Aceptar" y "Cancelar",
que en una pantalla de cancelación es una trampa.

**Una palabra por cosa, en todo el sistema.** Si es "cita", es cita en todas
partes: no "turno" en una pantalla y "reserva" en otra.

## Paso 7 — El informe

Cuando termines, entrégale al usuario esto y nada más:

```
DISEÑO — LO QUE CAMBIÉ

Jerarquía
  [qué estaba mal] -> [qué hice] -> [por qué]

Contraste
  [color viejo] daba X:1 (falla) -> [color nuevo] da Y:1 (pasa)

Uso y accesibilidad
  [N] puntos revisados, [N] corregidos
  Violaciones automáticas: [N]

Textos
  "[texto viejo]" -> "[texto nuevo]"

Lo que NO toqué y por qué
  [...]
```

Y una frase final honesta: qué quedó bien y qué sigue flojo. Si algo se ve
regular, dilo. El usuario le va a mostrar esto a un cliente que paga.

## Antes de grabar o entregar

Esta skill se corre **antes** de `entregar-al-cliente` y antes de grabar
cualquier demo. Lo que se ve es lo que se cobra: un sistema que funciona
perfecto pero se ve amateur se negocia hacia abajo, y uno que se ve de agencia
no se discute.

Material de apoyo, léelo solo cuando lo necesites:

- `${CLAUDE_SKILL_DIR}/references/paletas-y-tipografia.md` — paletas verificadas
  por nicho con su contraste ya calculado, y las combinaciones de tipografía que
  funcionan sin instalar nada.
- `${CLAUDE_SKILL_DIR}/references/componentes.md` — los componentes del sistema
  de reservas con sus estados y su accesibilidad resueltos, listos para copiar.
