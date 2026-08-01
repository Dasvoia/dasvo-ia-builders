# Componentes de un sistema de reservas

Los nueve componentes que aparecen en todo sistema de citas, resueltos de verdad. El CSS es puro y usa las variables de `paletas-y-tipografia.md`, sin Tailwind, para que se entienda qué hace cada línea. Si trabajas con Tailwind, traduce las clases pero conserva la estructura del HTML y los atributos de accesibilidad: eso es lo que no se puede improvisar.

---

## 1. Botón

**Para qué sirve.** Ejecutar la acción. En un flujo de reserva hay un solo botón primario visible por pantalla: el que avanza. Todo lo demás es secundario o de texto.

**Estados:** normal, hover, foco, presionado, deshabilitado, cargando.

```html
<button class="btn btn--primario" type="submit">Confirmar reserva</button>

<button class="btn btn--secundario" type="button">Volver</button>

<button class="btn btn--texto" type="button">Cambiar servicio</button>

<!-- Cargando: sigue diciendo qué está pasando, no se queda mudo -->
<button class="btn btn--primario" type="submit" aria-busy="true" disabled>
  <span class="btn__spinner" aria-hidden="true"></span>
  Confirmando…
</button>

<!-- Deshabilitado explicado: nunca dejes un botón muerto sin razón visible -->
<button class="btn btn--primario" type="submit"
        aria-describedby="motivo-bloqueo" disabled>Confirmar reserva</button>
<p id="motivo-bloqueo" class="ayuda">Elige primero un horario disponible.</p>
```

```css
.btn {
  /* El objetivo táctil: 44px de alto mínimo (WCAG 2.1 SC 2.5.5 es AAA,
     pero en móvil es lo que separa un botón usable de uno frustrante) */
  min-height: var(--alto-toque);
  min-width: 44px;
  padding: 0 var(--e5);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--e2);

  font-family: var(--fuente);
  font-size: var(--t-cuerpo);   /* 16px: nunca más chico */
  font-weight: 600;
  line-height: 1;

  border: 1px solid transparent;
  border-radius: var(--radio);
  cursor: pointer;
  transition: background-color .15s ease, border-color .15s ease;
}

/* ---- Primario ---- */
.btn--primario { background: var(--marca); color: #FFFFFF; }
.btn--primario:hover:not(:disabled) { background: var(--marca-oscuro); }
.btn--primario:active:not(:disabled) { background: var(--marca-oscuro);
  transform: translateY(1px); }

/* ---- Secundario ---- */
.btn--secundario {
  background: var(--fondo);
  color: var(--texto-fuerte);
  border-color: var(--borde);      /* 3:1 contra el fondo → cumple 1.4.11 */
}
.btn--secundario:hover:not(:disabled) { background: var(--fondo-suave); }

/* ---- Texto ---- */
.btn--texto {
  background: none;
  color: var(--marca);
  padding: 0 var(--e2);
  text-decoration: underline;      /* que se vea que es accionable sin color */
}

/* ---- Foco: el reemplazo obligatorio de outline:none ---- */
.btn:focus-visible {
  outline: 3px solid var(--marca);
  outline-offset: 2px;
}

/* ---- Deshabilitado ---- */
.btn:disabled { opacity: .55; cursor: not-allowed; }

/* ---- Cargando ---- */
.btn__spinner {
  width: 16px; height: 16px; border-radius: 50%;
  border: 2px solid rgba(255,255,255,.4);
  border-top-color: #FFFFFF;
  animation: girar .7s linear infinite;
}
@keyframes girar { to { transform: rotate(360deg); } }

@media (prefers-reduced-motion: reduce) {
  .btn__spinner { animation-duration: 2s; }
  .btn { transition: none; }
}
```

**Accesibilidad.**
- Usa `<button>`, no un `<div>` con `onClick`. Un `div` no se enfoca con Tab, no responde a Enter ni a Espacio, y el lector de pantalla no lo anuncia como botón.
- `type` explícito. Un `<button>` dentro de un `<form>` sin `type` es `submit` por defecto, y ese es el bug clásico de "el botón Volver manda el formulario".
- Cuando está cargando: `aria-busy="true"` y cambia el texto visible. "Confirmando…" le dice a todo el mundo qué pasa; un spinner solo no dice nada a un lector de pantalla.
- Si el botón está deshabilitado, di por qué en un texto asociado con `aria-describedby`. Un botón gris sin explicación es un callejón sin salida.

**El error más común.** `outline: none` sin reemplazo. Se pone porque el anillo del navegador se ve feo, y con eso quien navega con teclado pierde por completo dónde está: aprieta Tab siete veces sin ver nada moverse. En un flujo de reserva con calendario eso hace la página inservible, y rompe el criterio 2.4.7 (Foco visible, AA). Si lo quitas, pon `:focus-visible` con tu propio anillo.

---

## 2. Campo de formulario

**Para qué sirve.** Recoger un dato. En un sistema de reservas son cuatro o cinco: nombre, teléfono, correo, y a veces una nota.

**Estados:** normal, foco, error, deshabilitado, solo lectura.

```html
<div class="campo">
  <label class="campo__label" for="tel">Celular</label>
  <p class="campo__ayuda" id="tel-ayuda">Te enviamos la confirmación por WhatsApp.</p>
  <input class="campo__input" id="tel" name="tel"
         type="tel" inputmode="tel" autocomplete="tel"
         aria-describedby="tel-ayuda">
</div>

<!-- Con error -->
<div class="campo campo--error">
  <label class="campo__label" for="correo">Correo</label>
  <input class="campo__input" id="correo" name="correo"
         type="email" inputmode="email" autocomplete="email"
         aria-invalid="true" aria-describedby="correo-error">
  <p class="campo__error" id="correo-error">
    Falta el @. Escríbelo así: nombre@correo.com
  </p>
</div>

<div class="campo">
  <label class="campo__label" for="fecha">Fecha</label>
  <input class="campo__input" id="fecha" name="fecha" type="date"
         min="2026-08-01" max="2026-10-31">
</div>
```

```css
.campo { margin-bottom: var(--e5); }

.campo__label {
  display: block;
  font-size: var(--t-cuerpo);
  font-weight: 600;
  color: var(--texto-fuerte);
  margin-bottom: var(--e1);
}

.campo__ayuda {
  font-size: var(--t-chica);
  line-height: var(--lh-chica);
  color: var(--texto-suave);        /* pasa 4.5:1, no es gris decorativo */
  margin: 0 0 var(--e2);
}

.campo__input {
  width: 100%;
  min-height: var(--alto-toque);
  padding: var(--e3) var(--e4);
  font-family: var(--fuente);
  font-size: var(--t-cuerpo);       /* 16px o iOS hace zoom al enfocar */
  color: var(--texto-fuerte);
  background: var(--fondo);
  border: 1px solid var(--borde);
  border-radius: var(--radio);
}

.campo__input::placeholder { color: var(--texto-suave); }

.campo__input:focus-visible {
  outline: 3px solid var(--marca);
  outline-offset: 1px;
  border-color: var(--marca);
}

.campo__input:disabled {
  background: var(--fondo-suave);
  color: var(--texto-suave);
  cursor: not-allowed;
}

/* ---- Error: borde grueso + ícono + texto. Nunca solo el color (WCAG 1.4.1) ---- */
.campo--error .campo__input { border-color: var(--error); border-width: 2px; }

.campo__error {
  display: flex;
  gap: var(--e2);
  font-size: var(--t-chica);
  line-height: var(--lh-chica);
  color: var(--error);              /* 5.69:1 sobre blanco */
  margin: var(--e2) 0 0;
}

/* Ícono dibujado con CSS: no depende de una fuente de íconos ni de un emoji */
.campo__error::before {
  content: "!";
  flex-shrink: 0;
  width: 18px; height: 18px;
  display: inline-flex; align-items: center; justify-content: center;
  border: 2px solid var(--error);
  border-radius: 50%;
  font-weight: 700; font-size: 12px; line-height: 1;
}
```

**El `type` correcto importa mucho en celular.**

| Dato | `type` | `inputmode` | `autocomplete` | Qué gana el usuario |
|---|---|---|---|---|
| Celular | `tel` | `tel` | `tel` | Teclado numérico grande, sin letras |
| Correo | `email` | `email` | `email` | Teclado con `@` y `.` a la vista |
| Nombre | `text` | — | `name` | Autocompletado del navegador |
| Fecha | `date` | — | — | Selector nativo del sistema |

**Accesibilidad.**
- `<label for="id">` apuntando al `id` del input. Así el lector lo anuncia y, de paso, tocar la etiqueta enfoca el campo (objetivo táctil más grande gratis).
- La ayuda y el error se atan con `aria-describedby`. Sin eso, el lector de pantalla anuncia "Correo, campo de texto" y se calla: la persona nunca sabe que hay un error.
- `aria-invalid="true"` solo cuando hay error, y se quita al corregir.
- Marca los obligatorios de forma consistente y explica la convención una vez arriba. El asterisco solo no lo entiende todo el mundo.

**El error más común.** Usar el `placeholder` como etiqueta. Se ve "limpio" hasta que la persona empieza a escribir: el texto desaparece y ya nadie recuerda si ese campo era el celular o el teléfono fijo. Además el placeholder tiene poco contraste por diseño, no lo anuncian bien todos los lectores de pantalla, y en un formulario a medio llenar deja la pantalla llena de cajas anónimas. La etiqueta va **visible y arriba**, siempre. El placeholder es para un ejemplo del formato, no para el nombre del campo.

---

## 3. Selector de servicio

**Para qué sirve.** Elegir uno de varios servicios. Es una elección única, así que por debajo tiene que haber radio buttons de verdad, aunque por encima se vea como tarjetas.

**Estados:** normal, hover, foco, seleccionado, agotado.

```html
<fieldset class="servicios">
  <legend class="servicios__titulo">¿Qué te vas a hacer?</legend>

  <label class="servicio">
    <input class="servicio__radio" type="radio" name="servicio" value="limpieza">
    <span class="servicio__caja">
      <span class="servicio__nombre">Limpieza dental</span>
      <span class="servicio__meta">45 min · $80.000</span>
    </span>
  </label>

  <label class="servicio">
    <input class="servicio__radio" type="radio" name="servicio" value="blanqueamiento">
    <span class="servicio__caja">
      <span class="servicio__nombre">Blanqueamiento</span>
      <span class="servicio__meta">90 min · $320.000</span>
    </span>
  </label>
</fieldset>
```

```css
.servicios { border: 0; padding: 0; margin: 0 0 var(--e6); }
.servicios__titulo {
  padding: 0; margin-bottom: var(--e3);
  font-size: var(--t-h2); font-weight: 600; color: var(--texto-fuerte);
}

.servicio { display: block; margin-bottom: var(--e3); cursor: pointer; }

/* El radio real: invisible pero SIGUE existiendo y enfocándose.
   Nunca uses display:none ni visibility:hidden — eso lo saca del Tab. */
.servicio__radio {
  position: absolute;
  width: 1px; height: 1px;
  opacity: 0; margin: 0;
}

.servicio__caja {
  display: flex;
  flex-direction: column;
  gap: var(--e1);
  min-height: var(--alto-toque);
  padding: var(--e4);
  padding-left: calc(var(--e4) + 32px);   /* espacio para el círculo */
  position: relative;

  background: var(--fondo);
  border: 1px solid var(--borde);
  border-radius: var(--radio);
}

/* Círculo dibujado a mano */
.servicio__caja::before {
  content: "";
  position: absolute;
  left: var(--e4);
  top: 50%;
  transform: translateY(-50%);
  width: 20px; height: 20px;
  border: 2px solid var(--borde);
  border-radius: 50%;
  background: var(--fondo);
}

.servicio__radio:checked + .servicio__caja {
  border-color: var(--marca);
  border-width: 2px;
  background: var(--marca-claro);
  padding: calc(var(--e4) - 1px);
  padding-left: calc(var(--e4) + 31px);   /* compensa el borde de 2px */
}

.servicio__radio:checked + .servicio__caja::before {
  border-color: var(--marca);
  box-shadow: inset 0 0 0 4px var(--fondo), inset 0 0 0 10px var(--marca);
}

.servicio__radio:focus-visible + .servicio__caja {
  outline: 3px solid var(--marca);
  outline-offset: 2px;
}

.servicio:hover .servicio__caja { background: var(--fondo-suave); }

.servicio__nombre { font-weight: 600; color: var(--texto-fuerte); }
.servicio__meta   { font-size: var(--t-chica); color: var(--texto-suave); }
```

**Accesibilidad.**
- El grupo va en `<fieldset>` con `<legend>`. Así el lector anuncia "¿Qué te vas a hacer?, grupo" antes de leer cada opción.
- Con radios reales, las flechas del teclado ya mueven la selección dentro del grupo y el Tab salta al siguiente grupo. Eso es comportamiento nativo del navegador: no hay que programarlo.
- El estado seleccionado se distingue por **tres cosas a la vez**: color de fondo, grosor del borde y el punto dentro del círculo. Si fuera solo el color de fondo, alguien con daltonismo no vería la diferencia (WCAG 1.4.1).
- Toda la tarjeta es el objetivo táctil porque el `<label>` la envuelve.

**El error más común.** Hacer las tarjetas con `<div onClick>` y un `useState`. Se ve idéntico en pantalla, pero no se puede recorrer con Tab, no responde a las flechas, el lector de pantalla lo lee como texto suelto sin decir cuál está escogido, y el navegador no lo envía con el formulario. El otro error hermano es esconder el radio con `display: none`, que lo saca del orden de foco y produce exactamente el mismo problema.

---

## 4. Calendario y selector de hora

**Para qué sirve.** Escoger día y hora. Es la parte más difícil del sistema y donde se cae la mayoría de las reservas.

**Estados de un día:** disponible, sin cupo, seleccionado, hoy, fuera de rango, otro mes.

```html
<div class="cal">
  <div class="cal__barra">
    <button class="btn btn--secundario" type="button" aria-label="Mes anterior">←</button>
    <h2 class="cal__mes" id="cal-titulo" aria-live="polite">Agosto 2026</h2>
    <button class="btn btn--secundario" type="button" aria-label="Mes siguiente">→</button>
  </div>

  <table class="cal__grid" role="grid" aria-labelledby="cal-titulo">
    <thead>
      <tr>
        <th scope="col"><abbr title="Lunes">L</abbr></th>
        <th scope="col"><abbr title="Martes">M</abbr></th>
        <!-- … -->
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <button class="cal__dia" type="button" tabindex="-1">11</button>
        </td>
        <td>
          <button class="cal__dia cal__dia--sel" type="button" tabindex="0"
                  aria-pressed="true">12</button>
        </td>
        <td>
          <!-- Sin cupo: NO uses disabled. Un botón disabled no se enfoca y la
               persona con teclado no puede leer por qué está bloqueado. -->
          <button class="cal__dia" type="button" tabindex="-1"
                  aria-disabled="true">13<span class="sr">, sin cupos</span></button>
        </td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Horas del día escogido -->
<fieldset class="horas">
  <legend class="servicios__titulo">Horarios del miércoles 12</legend>
  <div class="horas__lista">
    <label class="hora">
      <input class="servicio__radio" type="radio" name="hora" value="09:00">
      <span class="hora__caja">9:00 a. m.</span>
    </label>
    <label class="hora">
      <input class="servicio__radio" type="radio" name="hora" value="09:45">
      <span class="hora__caja">9:45 a. m.</span>
    </label>
  </div>
</fieldset>

<!-- Cuando ese día no tiene nada libre -->
<div class="vacio" role="status">
  <p class="vacio__titulo">Ese día ya está lleno.</p>
  <p class="vacio__texto">El siguiente con espacio es el <strong>jueves 13</strong>.</p>
  <button class="btn btn--primario" type="button">Ver el jueves 13</button>
</div>
```

```css
.cal__barra {
  display: flex; align-items: center; justify-content: space-between;
  gap: var(--e3); margin-bottom: var(--e4);
}
.cal__mes { font-size: var(--t-h2); margin: 0; }

.cal__grid { width: 100%; border-collapse: collapse; table-layout: fixed; }
.cal__grid th {
  padding: var(--e2) 0;
  font-size: var(--t-chica); font-weight: 600; color: var(--texto-suave);
}
.cal__grid td { padding: 2px; text-align: center; }

.cal__dia {
  width: 100%;
  min-height: var(--alto-toque);
  font-family: var(--fuente);
  font-size: var(--t-cuerpo);
  color: var(--texto-fuerte);
  background: var(--fondo);
  border: 1px solid var(--borde-suave);
  border-radius: var(--radio-chico);
  cursor: pointer;
}
.cal__dia:hover { background: var(--fondo-suave); border-color: var(--borde); }

/* Seleccionado: relleno sólido + peso. No solo color. */
.cal__dia--sel {
  background: var(--marca);
  border-color: var(--marca);
  color: #FFFFFF;                 /* mínimo 4.5:1 en todas las paletas */
  font-weight: 700;
}

/* Hoy: subrayado grueso, se ve aunque el día también esté seleccionado */
.cal__dia--hoy { box-shadow: inset 0 -3px 0 var(--marca); }

/* Sin cupo: gris + tachado. El tachado es la segunda señal, no el color. */
.cal__dia[aria-disabled="true"] {
  color: var(--texto-suave);
  background: var(--fondo-suave);
  text-decoration: line-through;
  cursor: not-allowed;
}

.cal__dia:focus-visible { outline: 3px solid var(--marca); outline-offset: 2px; }

/* ---- Horas ---- */
.horas__lista {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(96px, 1fr));
  gap: var(--e2);
}
.hora__caja {
  display: flex; align-items: center; justify-content: center;
  min-height: var(--alto-toque);
  border: 1px solid var(--borde);
  border-radius: var(--radio);
  color: var(--texto-fuerte);
  background: var(--fondo);
}
.servicio__radio:checked + .hora__caja {
  background: var(--marca); border-color: var(--marca);
  color: #FFFFFF; font-weight: 600;
}
.servicio__radio:focus-visible + .hora__caja {
  outline: 3px solid var(--marca); outline-offset: 2px;
}

/* Texto solo para lectores de pantalla */
.sr {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
```

**Navegación con teclado (roving tabindex).** Solo un día tiene `tabindex="0"`; el resto tiene `-1`. Tab entra y sale del calendario de un salto, y dentro se mueve con las flechas.

```js
grid.addEventListener('keydown', (e) => {
  const saltos = { ArrowRight: 1, ArrowLeft: -1, ArrowDown: 7, ArrowUp: -7 };
  const salto = saltos[e.key];
  if (!salto) return;
  e.preventDefault();

  const dias = [...grid.querySelectorAll('.cal__dia')];
  const destino = dias[dias.indexOf(document.activeElement) + salto];
  if (!destino) return;                 // aquí se cambia de mes si quieres

  document.activeElement.tabIndex = -1;
  destino.tabIndex = 0;
  destino.focus();
});
```

También conviene: `Home` al primer día de la semana, `End` al último, `PageUp`/`PageDown` para cambiar de mes.

**Accesibilidad.**
- Al cambiar de mes, el `aria-live="polite"` del título anuncia "Septiembre 2026". Sin eso, quien no ve la pantalla no se entera de que el calendario cambió entero.
- Los días sin cupo llevan `aria-disabled="true"`, **no** el atributo `disabled`. `aria-disabled` los deja enfocables, así que la persona puede llegar hasta ellos y oír "13, sin cupos" en vez de encontrarse un hueco silencioso.
- Al escoger un día, mueve el foco al primer horario disponible o al encabezado "Horarios del…". Si el foco se queda en el día, la persona con lector no sabe que aparecieron horarios abajo.
- El estado "sin cupo" se comunica con color, tachado y texto oculto. Tres señales, no una.

**Qué hacer cuando ese día no tiene nada.** Lo peor es dejar el hueco vacío o mostrar "No hay resultados". Muestra el bloque de vacío con **la siguiente fecha que sí tiene espacio y un botón para saltar directo a ella**. Eso convierte un callejón sin salida en un paso más del flujo, y es la diferencia entre una reserva perdida y una hecha.

**El error más común.** Marcar el día escogido solo con un cambio de color de fondo suave. Con daltonismo, con la pantalla al sol o con el brillo bajo no se distingue de los demás, y la persona termina reservando otro día. Relleno sólido, cambio de peso y `aria-pressed`: las tres.

---

## 5. Resumen antes de confirmar

**Para qué sirve.** Es el último punto donde la persona puede darse cuenta de que se equivocó. Si el resumen está mal hecho, el negocio se come el no-show.

**Orden, de arriba abajo:**

1. **Servicio** — qué se va a hacer.
2. **Fecha y hora** — completa y en palabras: "miércoles 12 de agosto, 9:45 a. m.". No `12/08/2026 09:45`.
3. **Duración** — para que sepa cuánto tiempo bloquear.
4. **Profesional y lugar** — con quién y dónde, con la dirección.
5. **Datos de contacto** — el celular al que llegará el recordatorio.
6. **Precio** — al final.
7. **Política de cancelación** — una línea, visible, no escondida en un enlace.
8. **Botón de confirmar** — y debajo, un enlace de texto para volver.

```html
<section class="resumen" aria-labelledby="resumen-t">
  <h2 id="resumen-t">Revisa tu cita</h2>

  <dl class="resumen__lista">
    <div class="resumen__fila">
      <dt>Servicio</dt>
      <dd>Limpieza dental
        <a class="btn btn--texto" href="#servicio">Cambiar</a></dd>
    </div>
    <div class="resumen__fila">
      <dt>Cuándo</dt>
      <dd>Miércoles 12 de agosto, 9:45 a. m.
        <a class="btn btn--texto" href="#fecha">Cambiar</a></dd>
    </div>
    <div class="resumen__fila">
      <dt>Duración</dt><dd>45 minutos</dd>
    </div>
    <div class="resumen__fila">
      <dt>Dónde</dt><dd>Dra. Ospina · Calle 45 #12-30, consultorio 402</dd>
    </div>
    <div class="resumen__fila resumen__fila--total">
      <dt>Total</dt><dd>$80.000</dd>
    </div>
  </dl>

  <p class="resumen__politica">
    Puedes cancelar o mover la cita hasta 4 horas antes sin costo.
  </p>

  <button class="btn btn--primario" type="submit">Confirmar reserva</button>
</section>
```

```css
.resumen__lista { margin: 0 0 var(--e5); }
.resumen__fila {
  display: flex; justify-content: space-between; gap: var(--e4);
  padding: var(--e3) 0;
  border-bottom: 1px solid var(--borde-suave);
}
.resumen__fila dt { color: var(--texto-suave); font-size: var(--t-chica); }
.resumen__fila dd { margin: 0; color: var(--texto-fuerte); text-align: right; }
.resumen__fila--total {
  border-bottom: 0; border-top: 2px solid var(--borde);
  margin-top: var(--e2); padding-top: var(--e4);
}
.resumen__fila--total dt,
.resumen__fila--total dd { font-size: var(--t-h2); font-weight: 700;
                            color: var(--texto-fuerte); }
.resumen__politica {
  font-size: var(--t-chica); color: var(--texto-suave); margin: 0 0 var(--e5);
}
```

**Por qué el precio va aquí y no antes.** El precio se muestra dos veces: una en la tarjeta del servicio, como dato para comparar, y otra aquí como total. Lo que no debe pasar es que el precio sea grande y protagonista **al principio** del flujo. En ese momento la persona todavía no ha visto que hay hora disponible cuando le conviene, y el número es la única información que tiene para decidir. Cuando ya escogió servicio, día y hora, el precio se lee como confirmación de algo que ya decidió, no como el primer obstáculo. Y nunca lo escondas: un precio que aparece por sorpresa en el último paso genera abandono y desconfianza.

**Accesibilidad.** `<dl>` con `<dt>`/`<dd>` porque son pares etiqueta-valor, y el lector de pantalla los recorre emparejados. Cada "Cambiar" debe decir qué cambia — usa `aria-label="Cambiar el servicio"` si el texto visible es solo "Cambiar", porque quien navega por lista de enlaces oiría cinco "Cambiar" seguidos.

**El error más común.** Poner el resumen en un modal que tapa el formulario y del que solo se sale confirmando. La persona que quiere revisar un dato tiene que cerrar, perder la posición y volver a empezar. El resumen es una sección de la página, con enlaces de "Cambiar" que llevan al paso correspondiente sin perder lo demás.

---

## 6. Pantalla de confirmación

**Para qué sirve.** Que la persona cierre la pestaña tranquila. Si queda con dudas, llama al consultorio: eso es exactamente el trabajo que el sistema debía ahorrar.

Lo que necesita ver, en este orden:

1. **Confirmación inequívoca.** "Tu cita quedó agendada." En grande, con un ícono de éxito. No "Gracias" a secas: gracias no confirma nada.
2. **Los datos de la cita otra vez.** Servicio, fecha completa, hora, dirección, profesional. Que no tenga que buscarlos en el correo.
3. **El código de la reserva.** Corto y legible (`RSV-4821`), para mencionarlo por teléfono o WhatsApp.
4. **Adónde le llegó el comprobante.** "Te enviamos los detalles a 300 123 4567 por WhatsApp." Si no lo dices, la persona no sabe si esperar algo.
5. **Cómo cancelar o mover.** Un botón real, no un correo de contacto. Si cancelar es fácil, cancela con tiempo y el negocio revende el cupo.
6. **Agregar al calendario.** Un `.ics` o los enlaces a Google Calendar. Baja los no-shows más que cualquier recordatorio.
7. **Qué llevar o cómo llegar.** Una o dos líneas: "Llega 10 minutos antes", "El parqueadero es por la calle 46".

```html
<main class="confirmacion">
  <svg class="confirmacion__marca" viewBox="0 0 24 24" aria-hidden="true"
       fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
    <path d="M4 13l6 6L20 5"/>
  </svg>
  <h1>Tu cita quedó agendada</h1>
  <p class="confirmacion__cuando">Miércoles 12 de agosto, 9:45 a. m.</p>

  <p class="confirmacion__codigo">Código <strong>RSV-4821</strong></p>
  <p>Te enviamos los detalles al <strong>300 123 4567</strong> por WhatsApp.</p>

  <div class="confirmacion__acciones">
    <a class="btn btn--primario" href="/cita/RSV-4821.ics">Agregar a mi calendario</a>
    <a class="btn btn--secundario" href="/cita/RSV-4821">Cambiar o cancelar</a>
  </div>
</main>
```

**Accesibilidad.** Si la confirmación reemplaza el formulario sin recargar la página, mueve el foco al `<h1>` (`tabindex="-1"` + `.focus()`) o anúnciala con `role="status"`. Si no, quien usa lector de pantalla sigue oyendo el formulario viejo y no se entera de que ya reservó. El SVG del visto va con `aria-hidden="true"`: el texto ya dice lo que pasó.

**El error más común.** Redirigir al inicio después de reservar. La persona queda sin saber si funcionó, sin código y sin nada que mirar. La confirmación es una pantalla propia, con URL propia, a la que se pueda volver.

---

## 7. Mensajes de error y de vacío

**La estructura de tres partes.** Todo mensaje bien escrito tiene:

1. **Qué pasó**, en palabras del usuario, sin culparlo y sin jerga.
2. **Por qué**, solo si ayuda a entenderlo. Si no ayuda, se omite.
3. **Qué hacer ahora**, con una acción concreta y, si es posible, un botón que la ejecute.

| Situación | Mal | Bien (las tres partes) |
|---|---|---|
| Hora ya tomada | "Error 409: conflicto" | **Alguien tomó las 9:45 mientras reservabas.** Pasa cuando dos personas eligen a la vez. **Las 10:30 y las 11:15 siguen libres ese mismo día.** `[Tomar las 10:30]` |
| Fuera de horario | "Horario inválido" | **Los sábados atendemos hasta la 1:00 p. m.** **Te mostramos los horarios del lunes, o escoge otro día.** `[Ver el lunes]` |
| Muy poca anticipación | "Fecha no permitida" | **Las citas se reservan con 2 horas de anticipación.** Es el tiempo que necesita el consultorio para prepararse. **El horario más cercano hoy es a las 3:00 p. m.** `[Tomar las 3:00 p. m.]` |
| Sin conexión | "Network error" | **Se cayó la conexión y no pudimos guardar tu cita.** **Tus datos siguen aquí. Revisa el internet y vuelve a intentar.** `[Reintentar]` |
| Campo obligatorio | "Campo requerido" | **Falta tu celular.** Es a donde te llega el recordatorio. **Escríbelo con los 10 dígitos, sin espacios.** |
| Día sin cupos | "Sin resultados" | **El jueves 14 ya está lleno.** **El siguiente día con espacio es el viernes 15.** `[Ver el viernes 15]` |

**Reglas transversales.**
- **Nunca muestres el error técnico.** "Error 409", "PGRST116", "null is not an object" no significan nada para el dueño de la barbería ni para su cliente. Regístralos en el log; en pantalla va la versión humana.
- **Nunca culpes.** "Ingresaste un dato inválido" contra "Falta el @ en el correo". La segunda dice qué arreglar.
- **Nunca dejes un callejón sin salida.** Todo error termina con algo que se puede hacer, idealmente un botón.
- **No pierdas lo que ya escribió.** Si falla el envío, los campos siguen llenos. Perder el formulario es el motivo más común de abandono.

```html
<div class="msg msg--error" role="alert">
  <div>
    <p class="msg__titulo">Alguien tomó las 9:45 mientras reservabas.</p>
    <p class="msg__texto">Las 10:30 y las 11:15 siguen libres ese mismo día.</p>
    <button class="btn btn--secundario" type="button">Tomar las 10:30</button>
  </div>
</div>
```

```css
.msg {
  display: flex; gap: var(--e3);
  padding: var(--e4);
  border-radius: var(--radio);
  border-left: 4px solid;
  margin-bottom: var(--e4);
}

/* El ícono es la señal que no depende del color (WCAG 1.4.1) */
.msg::before {
  flex-shrink: 0;
  width: 22px; height: 22px;
  display: inline-flex; align-items: center; justify-content: center;
  border: 2px solid currentColor;
  border-radius: 50%;
  font-weight: 700; font-size: 14px; line-height: 1;
}
.msg--error::before,
.msg--alerta::before { content: "!"; }
.msg--exito::before  { content: "OK"; font-size: 10px; border-radius: 999px;
                       width: auto; padding: 0 6px; }
/* El `color` fija el currentColor que usa el ícono de arriba */
.msg--error  { background: var(--error-fondo);  border-color: var(--error);
               color: var(--error);  }
.msg--alerta { background: var(--alerta-fondo); border-color: var(--alerta);
               color: var(--alerta); }
.msg--exito  { background: var(--exito-fondo);  border-color: var(--exito);
               color: var(--exito);  }

.msg__titulo { font-weight: 600; color: var(--texto-fuerte); margin: 0 0 var(--e1); }
.msg__texto  { font-size: var(--t-chica); color: var(--texto-cuerpo); margin: 0 0 var(--e3); }
```

**Accesibilidad.** `role="alert"` para errores que interrumpen (se anuncia de inmediato) y `role="status"` para información que no urge (se anuncia cuando el lector termina lo que está diciendo). No pongas `role="alert"` en todo: si todo interrumpe, la persona apaga el lector.

**El error más común.** Un `toast` rojo en la esquina que desaparece a los 3 segundos. Quien lee despacio no alcanza, quien usa lector de pantalla puede perdérselo, y el mensaje no queda cerca del campo que hay que arreglar. Los errores de formulario van **junto al campo**, y ahí se quedan hasta que se corrijan.

---

## 8. La tabla de citas del panel del dueño

**Para qué sirve.** El dueño abre esto veinte veces al día, casi siempre desde el celular entre cliente y cliente. Si en móvil se ve como una tabla apretada con scroll horizontal, deja de usarlo y vuelve al cuaderno.

**El patrón: filas que se vuelven tarjetas.** Se escribe un solo HTML —una tabla de verdad, semántica— y el CSS la convierte en tarjetas por debajo de cierto ancho. En escritorio sigue siendo una tabla comparable; en celular es una lista de tarjetas legibles.

```html
<table class="citas">
  <caption class="sr">Citas del miércoles 12 de agosto</caption>
  <thead>
    <tr>
      <th scope="col">Hora</th>
      <th scope="col">Cliente</th>
      <th scope="col">Servicio</th>
      <th scope="col">Estado</th>
      <th scope="col">Acciones</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-etq="Hora"><strong>9:45 a. m.</strong></td>
      <td data-etq="Cliente">Marta Ruiz · 300 123 4567</td>
      <td data-etq="Servicio">Limpieza dental (45 min)</td>
      <td data-etq="Estado"><span class="chip chip--ok">Confirmada</span></td>
      <td data-etq="Acciones">
        <button class="btn btn--texto" type="button">Reagendar</button>
        <button class="btn btn--texto" type="button">Cancelar</button>
      </td>
    </tr>
  </tbody>
</table>
```

```css
.citas { width: 100%; border-collapse: collapse; }
.citas th {
  text-align: left; padding: var(--e3) var(--e4);
  background: var(--fondo-claro);
  font-size: var(--t-chica); color: var(--texto-cuerpo);
  border-bottom: 1px solid var(--borde);
}
.citas td { padding: var(--e4); border-bottom: 1px solid var(--borde-suave); }
.citas tbody tr:hover { background: var(--fondo-suave); }

.chip {
  display: inline-block; padding: 2px var(--e2);
  border-radius: 999px; font-size: var(--t-chica); font-weight: 600;
}
.chip--ok { background: var(--exito-fondo); color: var(--exito); }

/* ---- Celular: cada fila se vuelve una tarjeta ---- */
@media (max-width: 640px) {
  .citas thead { display: none; }          /* el encabezado ya no sirve */
  .citas, .citas tbody, .citas tr, .citas td { display: block; width: 100%; }

  .citas tr {
    border: 1px solid var(--borde);
    border-radius: var(--radio);
    margin-bottom: var(--e4);
    padding: var(--e2) var(--e4);
    background: var(--fondo);
  }

  .citas td {
    display: flex;
    justify-content: space-between;
    gap: var(--e4);
    padding: var(--e2) 0;
    border-bottom: 1px solid var(--borde-suave);
  }
  .citas td:last-child { border-bottom: 0; }

  /* La etiqueta de la columna vuelve, ahora dentro de la celda */
  .citas td::before {
    content: attr(data-etq);
    font-size: var(--t-chica);
    color: var(--texto-suave);
    flex-shrink: 0;
  }
}
```

**Accesibilidad.** `display: block` sobre una tabla **le quita la semántica de tabla** en varios lectores de pantalla: dejan de anunciar "fila 3, columna Estado". Por eso el `data-etq` es obligatorio: con la etiqueta visible dentro de cada celda, la información sigue siendo comprensible aunque se haya perdido la estructura. Y el `<caption>` (aunque esté oculto visualmente) dice de qué es la tabla.

**El error más común.** Meter la tabla en un `overflow-x: auto` y darla por resuelta. El dueño tiene que desplazar de lado para ver el estado de cada cita, y la columna que más mira —el estado— es la que queda siempre fuera de pantalla. Si de todas formas usas scroll horizontal, al menos fija la primera columna y ponle `tabindex="0"` al contenedor para que se pueda desplazar con teclado.

---

## 9. Estados de carga

**Para qué sirve.** Tapar el hueco entre que la persona aprieta y que pasa algo. Sin eso, aprieta dos veces y reserva dos citas.

**Qué mostrar mientras se confirma una reserva:**

- El botón cambia a "Confirmando…" con `aria-busy="true"` y queda deshabilitado. Eso resuelve el doble envío.
- El resumen sigue visible. No lo tapes con una pantalla de carga: la persona quiere seguir viendo lo que está reservando.
- Si pasa de 5 segundos, un texto extra: "Estamos guardando tu cita, no cierres esta pantalla."
- Nunca un bloqueo de pantalla completa. Si algo falla, la persona queda atrapada.

**Por qué el esqueleto le gana al giro.** Cuando cargas una lista de horarios o el panel de citas, un esqueleto —bloques grises con la forma del contenido que viene— es mejor que un spinner por tres razones:

1. **Dice qué va a llegar.** El ojo ya se coloca donde estará el contenido, así que cuando aparece no hay que releer la pantalla.
2. **No salta el diseño.** El esqueleto ocupa el mismo espacio que el contenido final, así que nada se mueve al llegar. Un spinner centrado colapsa y empuja todo hacia abajo.
3. **Se siente más rápido.** El mismo tiempo de espera se percibe más corto cuando hay estructura que cuando hay un círculo dando vueltas, porque el spinner no da ninguna información sobre el progreso.

El spinner sigue teniendo su lugar: **dentro de un botón**, para una acción puntual que ya se disparó. Ahí sí es lo correcto.

```html
<div class="esqueleto" role="status" aria-live="polite">
  <span class="sr">Cargando horarios disponibles…</span>
  <div class="esqueleto__bloque" style="width: 40%; height: 20px;"></div>
  <div class="esqueleto__grid">
    <div class="esqueleto__bloque" style="height: 44px;"></div>
    <div class="esqueleto__bloque" style="height: 44px;"></div>
    <div class="esqueleto__bloque" style="height: 44px;"></div>
  </div>
</div>
```

```css
.esqueleto__bloque {
  background: var(--fondo-claro);
  border-radius: var(--radio-chico);
  margin-bottom: var(--e3);
  animation: latir 1.6s ease-in-out infinite;
}
.esqueleto__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(96px, 1fr));
  gap: var(--e2);
}
@keyframes latir { 50% { opacity: .55; } }

/* Respeta a quien pidió menos movimiento (WCAG 2.3.3) */
@media (prefers-reduced-motion: reduce) {
  .esqueleto__bloque { animation: none; opacity: .8; }
}
```

**Accesibilidad.** El esqueleto es puro adorno visual: sin el `<span class="sr">` que dice "Cargando horarios disponibles…", quien usa lector de pantalla oye silencio y cree que la página se rompió. `role="status"` con `aria-live="polite"` lo anuncia sin interrumpir.

**El error más común.** Dejar el botón activo mientras se procesa. La persona no ve reacción, vuelve a apretar, y quedan dos citas a la misma hora. Deshabilitar el botón al primer clic no es un detalle de diseño: es la protección más barata contra reservas duplicadas.

---

## Checklist de 15 puntos

Antes de dar una pantalla por terminada, recórrela:

1. **Un solo botón primario visible.** Si hay dos, uno de los dos es secundario.
2. **Todo texto pasa 4.5:1** contra el fondo real donde está, no contra blanco imaginario.
3. **Todo lo enfocable tiene anillo de foco visible.** Recorre la pantalla entera con Tab sin tocar el mouse; si en algún momento no ves dónde estás, está roto.
4. **Todo lo que se toca mide al menos 44px de alto,** con separación entre objetivos vecinos.
5. **Todo campo tiene etiqueta visible arriba.** Ningún placeholder haciendo de etiqueta.
6. **Ningún estado se comunica solo con color.** Seleccionado, con error, sin cupo: siempre una segunda señal (borde, ícono, texto, tachado).
7. **Los errores están junto al campo** que hay que corregir, y dicen qué hacer.
8. **Ningún mensaje técnico llega a la pantalla.** Ni códigos, ni nombres de tabla, ni `undefined`.
9. **Ningún estado vacío es un callejón sin salida.** Todos ofrecen la siguiente acción.
10. **El botón de envío se deshabilita al primer clic** y cambia de texto.
11. **Se ve bien a 360px de ancho.** Ninguna tabla con scroll horizontal, ningún texto cortado.
12. **Los inputs son de 16px** para que iOS no haga zoom al enfocarlos.
13. **Máximo cuatro tamaños de letra** en la pantalla, todos de los tokens.
14. **Ningún hex suelto en el código.** Todo color viene de una variable.
15. **La página funciona entera con teclado,** de principio a fin: llegar al calendario, moverse entre días con flechas, escoger hora, llenar los campos y confirmar sin tocar el mouse ni una vez.
