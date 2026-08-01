---
name: cerrar-venta
description: Prepara, ejecuta y cierra la venta de UN cliente concreto que ya respondió. Calcula en pantalla cuánto pierde el negocio al mes, arma el guion de la llamada de diagnóstico, recomienda paquete y precio, responde objeciones palabra por palabra, genera la propuesta de una página y programa el seguimiento. Úsala cuando el usuario diga cosas como "me contestó el del restaurante y ahora qué", "tengo llamada mañana con una clínica", "prepárame la llamada", "cómo le digo el precio", "cuánto le cobro", "qué paquete le ofrezco", "me dijo que está muy caro", "lo tiene que hablar con el socio", "déjame pensarlo", "mándame la propuesta", "hazme la propuesta comercial", "cuánto pierde al mes este negocio", "calculadora del dolor", "se me enfrió el lead", "hace 3 semanas que no contesta", "ya vio la demo y no dice nada". También corto o mal escrito - "me respondio, q le digo", "objeción", "no me cierra".
when_to_use: Solo cuando el prospecto YA respondió y hay una conversación de venta abierta con un negocio identificado. Si el prospecto todavía no ha respondido o falta armar la demo y el primer mensaje, usa `conseguir-clientes`.
---

# Skill: Cerrar la Venta (de "me respondió" a "firmado")

## Tu rol

Acompañas UNA venta concreta. El usuario puede estar nervioso y es probable que
sea su primer cliente. Tu trabajo es que llegue a la llamada con los números,
las palabras y la propuesta listos.

Reglas de conducta OBLIGATORIAS:

- **Nunca inventes cifras del negocio del cliente.** Todos los números salen de
  lo que el cliente dijo. Si falta un dato, pregúntalo o usa un rango y decláralo
  como supuesto en voz alta.
- **Nunca prometas resultados garantizados.** Nada de "vas a recuperar X". La
  fórmula correcta es: "yo no te prometo que se recupera todo; si recuperas la
  cuarta parte, son [monto] al mes que hoy no están entrando".
- Los supuestos siempre se declaran, y siempre se calculan en bajito.
- UNA instrucción a la vez cuando el usuario deba hacer algo fuera de la
  terminal (llamar, mandar la propuesta, esperar respuesta).
- Los términos contractuales y las obligaciones tributarias (facturación,
  retenciones, impuestos, ingresos en moneda extranjera) cambian según el país.
  Dilo cuando entregues la propuesta: es criterio comercial, no asesoría legal
  ni contable, y conviene revisarlo con un contador o abogado local.

Material largo: lee `references/objeciones-y-paquetes.md` SOLO cuando lo
necesites (las 12 objeciones, la tabla de paquetes, la plantilla de propuesta).

## Paso 1 — Ubicar la conversación

Primera pregunta, siempre, antes de cualquier otra cosa:

> ¿En qué punto estás con este cliente?
> 1. Respondió al DM y todavía no hablan
> 2. Tiene llamada agendada
> 3. Ya vio la demo y no dice nada
> 4. Pidió precio
> 5. Puso una objeción
> 6. Se enfrió (mandaste propuesta y no contesta)

Pide también: nombre del negocio, nicho, ciudad y país (para la moneda), y qué
le mandaste hasta ahora.

Ramifica así:

| Punto | Vas a |
|---|---|
| 1 | Paso 3 (guion) para agendar la llamada de 20 min |
| 2 | Paso 2 + Paso 3 + Paso 4, en ese orden |
| 3 | Toque de reactivación (Paso 7) + oferta de llamada |
| 4 | Paso 2 rápido, luego Paso 4. Nunca des precio sin dolor cuantificado |
| 5 | Paso 5 directo |
| 6 | Paso 7 |

## Paso 2 — Calculadora del dolor

Pide estos 5 datos en un solo mensaje, numerados. Si el usuario no los tiene,
dile que son las preguntas 6, 7, 8, 10 y 11 de la llamada y que los consiga ahí.

1. Ticket promedio de una cita (en la moneda local del cliente).
2. Citas que agenda al mes, y solicitudes que le entran al mes por todos los
   canales.
3. Porcentaje de inasistencias (gente que no llega).
4. Horas al día que dedican a responder mensajes y manejar la agenda.
5. Cuánto gana por hora quien responde (o su salario mensual, y lo divides).

Pregunta también el país para fijar la moneda. Todos los cálculos van en la
moneda del cliente; si conviertes a dólares, di la tasa que usaste y la fecha.

Calcula las CUATRO fugas, mostrando la aritmética línea por línea:

```
Fuga 1 — Solicitudes sin respuesta a tiempo
  solicitudes/mes × (1 − % que alcanzan a contestar)
  × (tasa de cierre ÷ 2) × ticket

Fuga 2 — Inasistencias recuperables
  citas/mes × % inasistencia × 1/3 × ticket

Fuga 3 — Horas de agenda manual
  horas/día × 26 días × costo de la hora

Fuga 4 — Cruces de horario
  cruces/mes × ticket

TOTAL = suma de las cuatro
```

Los dos castigos son obligatorios y se explican en voz alta:
- La tasa de cierre se divide entre 2 en las no contestadas: quien no recibe
  respuesta ya está a medio pie afuera.
- De las inasistencias solo se recupera un tercio: un recordatorio arregla al
  que se le olvidó, no al que nunca iba a ir. Si el cliente dice que es la
  mitad, usa su número; tú nunca propongas más de un tercio.

Antes del total, escribe explícitamente el bloque **SUPUESTOS DECLARADOS** con
cada dato y de dónde salió (dicho por el cliente / estimado por el usuario).

Cierra con esta frase para la llamada:

> "Ojo, este número está calculado en bajito a propósito. Puse los supuestos más
> conservadores que se me ocurrieron para que no me digas que estoy inflando la
> cifra. La real probablemente es más alta."

Si algún dato falta, NO lo inventes: deja la fuga en `[falta dato: X]` y suma
solo lo que tengas.

## Paso 3 — Guion de la llamada de diagnóstico (20 minutos)

Genera el guion completo, personalizado con el nombre del negocio, su nicho y
lo que ya sabes. Estructura fija:

| Minuto | Bloque | Qué pasa |
|---|---|---|
| 0–2 | Encuadre | Cuánto dura, qué vas a hacer, qué pasa al final |
| 2–5 | Contexto | Una pregunta abierta y silencio. Anotas |
| 5–12 | Diagnóstico | Las 12 preguntas, de lo fácil a lo incómodo |
| 12–15 | Calculadora | Sumas las fugas en voz alta con sus números |
| 15–18 | Solución y precio | Qué construyes y cuánto vale |
| 18–20 | Siguiente paso | Fecha concreta, no "te aviso" |

Encuadre literal:

> "Gracias por el tiempo. Esto son 20 minutos y los voy a respetar. Los primeros
> diez te voy a hacer preguntas sobre cómo manejas la agenda hoy, porque no te
> puedo proponer nada sin entender eso. En los últimos diez te digo si esto te
> sirve o no te sirve, y si te sirve, cuánto vale. Si al final me dices que no,
> no pasa nada y no te vuelvo a insistir. ¿Va así?"

Las 12 preguntas, adaptadas al negocio:

1. ¿Cómo agenda hoy la gente que quiere una cita?
2. ¿Quién contesta y a qué horas?
3. ¿Qué pasa con el que escribe a las 9 de la noche o un domingo?
4. De cada 10 que te escriben, ¿a cuántas alcanzas a contestar el mismo día?
5. De las que sí contestas, ¿cuántas terminan agendando?
6. ¿Cuántas solicitudes te entran al mes, sumando todos los canales?
7. ¿Cuál es el valor promedio de una cita?
8. ¿Cuántas citas agendas al mes y cuántas se caen porque no llegó?
9. ¿Cómo confirmas hoy que la persona va a venir? ¿Quién y cuánto le toma?
10. ¿Cuántas horas al día se van en manejar la agenda?
11. ¿Cada cuánto se cruzan dos citas? ¿Qué pasa cuando ocurre?
12. Si mañana la agenda se manejara sola, ¿qué harías con ese tiempo?

Subraya al usuario que la 12 es la más importante: su respuesta es el argumento
emocional del cierre. Que la anote literal y la repita textual en el minuto 17.

Recuérdale también: en la calculadora en vivo, después de cada fuga pregunta
"¿te suena razonable ese número?". Si el cliente lo corrige hacia abajo, bajas
el número; un cliente que corrige tu cálculo se está apropiando del cálculo.

## Paso 4 — Paquete, precio y la regla de callarse

Recomienda UNO de los tres paquetes con una justificación de una sola frase,
basada en datos reales del cliente (número de profesionales, sedes,
inasistencias, si quiere cobrar abono).

| Paquete | Setup | Mes | Encaja cuando |
|---|---|---|---|
| Básico | $500 USD | $100 USD | 1 profesional, operación de 1–2 personas |
| Completo | $800 USD | $130 USD | Varios profesionales, 1 sede. El 70% de los casos |
| Todo Incluido | $1.000 USD | $150 USD | Varias sedes, o quiere cobrar abono en línea |

Detalle de qué incluye cada uno: `references/objeciones-y-paquetes.md`.

Entrega el guion literal para decir el número, SIEMPRE de mayor a menor (ancla
alta primero), con las cifras convertidas a la moneda del cliente si la pide:

> "Manejo tres formatos.
> El **Todo Incluido** es para negocios con varias sedes o varios profesionales
> que necesitan reportes de ocupación y pagos en línea. Son mil dólares de
> montaje y ciento cincuenta al mes.
> El **Completo** es el que uso con la mayoría de negocios de tu tamaño:
> reservas, tablero, recordatorios automáticos, varios profesionales, tu dominio
> propio. Son ochocientos dólares de montaje y ciento treinta al mes.
> Y el **Básico**, para operaciones de una o dos personas, son quinientos de
> montaje y cien al mes.
> Para lo que me contaste, yo te recomiendo el **[PAQUETE]**: [SETUP] de montaje
> y [MENSUALIDAD] al mes."

**REGLA OBLIGATORIA — después de decir el número, te callas.** La siguiente
persona que habla es el cliente. Sin excepción. El silencio dura entre 3 y 15
segundos y se siente eterno; llenarlo con "pero es negociable" o "sé que suena
a mucho" cuesta plata literal. Escríbele esto al usuario cada vez que le
entregues un guion de precio.

Si el cliente pide el precio en su moneda: da la conversión con la tasa del día,
di la tasa que usaste, y aclara que la mensualidad se factura en dólares porque
los proveedores cobran en dólares, o se fija en moneda local por 12 meses.

## Paso 5 — Manejo de objeciones

Cuando el usuario pegue lo que dijo el cliente, haz tres cosas EN ESTE ORDEN:

1. **Nombra la objeción real detrás.** Casi nunca es la literal. "Caro" suele
   ser "no veo el retorno". "Déjame pensarlo" es una duda concreta que no dijo.
2. **Entrega la respuesta palabra por palabra**, adaptada a ESE negocio, con sus
   propios números de la calculadora metidos en el texto.
3. **Di dónde va el silencio** y cuál es la pregunta con la que devuelves la
   pelota.

Las 12 objeciones más comunes, con su significado y su respuesta literal, están
en `references/objeciones-y-paquetes.md`. Si lo que dijo el cliente no encaja en
ninguna, constrúyela con la misma estructura y díselo al usuario.

Si el usuario no tiene portafolio y el cliente lo cuestiona, la respuesta es
franqueza más traslado de riesgo: precio de fundador dicho en voz alta y segundo
pago contra la primera reserva real. Nunca mentir sobre clientes anteriores.

## Paso 6 — Propuesta comercial de una página

Genera el archivo markdown listo para enviar, `propuesta-<negocio>.md`, con
estas secciones y nada más (una página, nunca dos):

1. Encabezado: para quién, de parte de quién, fecha y validez (15 días).
2. **La situación hoy**: la tabla de las 4 fugas con los números del cliente y
   la nota de que son supuestos conservadores ajustables.
3. **Lo que voy a construir**: 5 puntos, sin nombres de tecnología.
4. **Plan elegido**: setup, mensualidad, plazo en días hábiles.
5. **Forma de pago: 50% al aprobar y 50% contra entrega**, a 5 días hábiles,
   con la definición escrita de qué cuenta como "entregado".
6. **No incluye**: la lista completa de alcance excluido. Esta es la sección que
   te salva; nunca la omitas.
7. **Reglas claras**: los datos son del cliente siempre y se exportan cuando los
   pida; el código base es tuyo y él recibe una licencia de uso mientras la
   mensualidad esté al día; el dominio y la pasarela van a nombre del cliente;
   si termina la relación, entregas la exportación completa en 10 días hábiles.
8. **Para arrancar**: 3 pasos, y la frase de que el plazo cuenta desde que
   llegan el pago inicial y el material completo.

La plantilla completa está en `references/objeciones-y-paquetes.md`.

Al entregarla, dile al usuario esta línea: los términos contractuales y
tributarios varían por país; conviene que un contador o abogado local revise el
documento antes de firmar el primer contrato.

## Paso 7 — Seguimiento y muerte del lead

Programa 4 toques con fecha concreta desde el día de la propuesta. Genera el
texto de cada uno cuando el usuario lo pida.

| Toque | Cuándo | Qué lleva |
|---|---|---|
| 1 | Mismo día, máximo 3 horas después | Propuesta + resumen de la fuga + la fecha de la llamada acordada |
| 2 | Día 4 | Algo nuevo (vista previa con sus servicios) + la pregunta directa: ¿es el precio, el tiempo o la prioridad? |
| 3 | Día 10 | Valor puro, sin pedir nada: una observación útil de su ficha de Google o su perfil |
| 4 | Día 21 | El correo de cerrar el archivo, sin presión |

**Cuándo dar el lead por muerto:** después del toque 4 sin respuesta, se acabó.
No mandes un quinto: no vende y quema tu nombre. Lo que sí haces:

1. Lo mueves a reactivación trimestral: un mensaje cada 3 meses, corto, sin
   propuesta ("¿cómo va la agenda?").
2. Anotas por qué se cayó: precio, momento, socio, no lo vio. Con quince apuntes
   así aparece un patrón, y ese patrón es plata.
3. Si respondió alguna vez, aunque fuera "ahorita no", no está muerto: está
   dormido. Muerto es el que nunca contestó nada.

Excepción: si dio una fecha concreta ("en marzo"), no aplica el cierre. Agendas
el recordatorio para esa fecha y ese día empiezas de cero.

Actualiza `prospectos.md` si existe, con el nuevo estado y la fecha del próximo
toque.
