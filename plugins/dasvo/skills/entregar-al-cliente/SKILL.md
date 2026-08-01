---
name: entregar-al-cliente
description: Lleva el sistema de reservas de "funciona en mi computador" a "el cliente lo está usando y me paga la mensualidad". Cubre la checklist previa a la entrega, a nombre de quién quedan las cuentas de Supabase y Vercel, el manual de uso del dueño, la capacitación de 30 minutos con el equipo, el seguimiento de los primeros 30 días, el alcance del mantenimiento mensual y el pedido de testimonio y referidos.
when_to_use: Úsala cuando el usuario ya tenga el sistema listo o casi listo y toque entregarlo, o diga cosas como "ya terminé el sistema y ahora qué", "cómo se lo entrego al cliente", "entrega", "checklist de entrega", "a nombre de quién dejo las cuentas", "el cliente quiere ser dueño de la base de datos", "traspasar Supabase al cliente", "manual para el cliente", "cómo le enseño a usarlo", "capacitación", "el de recepción no quiere usarlo", "qué le mando al cliente la primera semana", "cómo justifico los 100 dolares al mes", "qué incluye el mantenimiento", "me está pidiendo cosas que no acordamos", "cómo le pido un testimonio", "pedir referidos", "se quiere dar de baja". También si va a cobrar la primera mensualidad y no tiene el alcance por escrito.
---

# Skill: Entregar el Sistema al Cliente

## Tu rol

Eres quien convierte un proyecto terminado en un cliente que paga todos los
meses. La parte técnica ya está; lo que falta es lo que decide si el cliente se
queda o se va a los tres meses.

- UNA instrucción a la vez cuando el usuario deba hacer algo fuera de la terminal
  (entrar a Supabase, escribirle al cliente, hacer la llamada).
- No avances de fase sin que el usuario confirme que la anterior está hecha.
- Todo lo que se acuerde con el cliente queda POR ESCRITO. Sin excepción.
- Los textos largos (manual, guion, mensajes, alcance) están en
  `references/plantillas-entrega.md`. Léelo cuando toque generarlos, rellénalo
  con los datos reales del negocio y entrégaselo al usuario como archivo.

## Fase 1 — Checklist previa a la entrega

Recórrela EN ORDEN. Verifica tú lo que puedas verificar; para lo que dependa del
usuario, pide una sola cosa a la vez y espera confirmación. No pases al siguiente
punto con uno pendiente.

1. **Revisión de seguridad ejecutada.** Corre la skill `seguridad-web` completa.
   Si algún punto quedó en rojo, la entrega se detiene aquí.
2. **Dominio conectado.** Dominio propio del cliente o subdominio suyo. Nada de
   entregar una URL `algo-xyz123.vercel.app`: se ve a medio hacer y le cuesta al
   cliente defender el precio ante su socio. Verifica que el certificado HTTPS
   está activo y que la versión sin `www` y con `www` funcionan.
3. **Variables de entorno en producción.** Confirma que están cargadas en Vercel,
   que son las del proyecto correcto y que hubo un deploy DESPUÉS de cargarlas.
   Comprobar sin imprimir valores en pantalla.
4. **Correos de confirmación funcionando, si el sistema los envía.** Haz una
   reserva de prueba y revisa que llega el correo, con el nombre del negocio como
   remitente, sin enlaces rotos y sin caer en spam. Revisa la bandeja de spam
   explícitamente. Si no hay correos, dilo claro en la entrega para que nadie los
   espere.
5. **Reserva real de punta a punta desde un celular.** El usuario, con datos
   ficticios, desde su celular y con datos móviles (no wifi): elegir servicio,
   día y hora, llenar el formulario, confirmar, ver la pantalla de confirmación,
   y que la reserva aparezca en el panel. Que verifique también que el teclado no
   tapa los campos y que los botones se alcanzan con el pulgar.
6. **Prueba en el navegador del cliente.** Pregunta qué usa el negocio: muchos
   consultorios y talleres siguen en computadores viejos con Windows y con Edge.
   Prueba ahí y en el celular del dueño, que casi siempre es el que importa.
7. **Zona horaria correcta.** Este es el error que más entregas daña. Verifica
   que una reserva hecha a las 9:00 aparece como 9:00 en el panel, en el correo y
   en la base de datos según la zona del negocio, y que sigue correcta después de
   medianoche y en el último día del mes. Vercel corre en UTC: si el cálculo no
   fija la zona explícitamente, va a fallar.

Al terminar, muestra el resumen con estado de los siete puntos y el veredicto:
LISTO PARA ENTREGAR o CORREGIR ANTES DE ENTREGAR.

## Fase 2 — A nombre de quién quedan las cuentas

Esta decisión se toma ANTES de la reunión de entrega, se explica al cliente y se
pone por escrito. Hay dos modelos válidos y la elección tiene consecuencias
económicas reales, así que no la dejes al azar: pregunta y decide con el usuario.

**Modelo A — Infraestructura consolidada bajo la cuenta del proveedor.**
Es el predeterminado para los paquetes Básico y Completo, y es el que sostiene
el margen del negocio: un solo plan Pro de Vercel cubre todos los proyectos y
cada proyecto adicional de Supabase cuesta bastante menos que un plan completo.
El costo marginal de cada cliente nuevo cae a una fracción del primero.
También permite desplegar y arreglar a cualquier hora sin pedir contraseñas, y
suspender el servicio si el cliente deja de pagar.

Su riesgo real, y no lo escondas: si la relación termina mal, el cliente puede
acusar de retención de datos. Por eso el Modelo A **solo se ofrece con estas
tres cláusulas escritas**, y son obligatorias:

1. Copia completa de los datos entregada al cliente en un plazo definido (10 días
   hábiles) cuando la pida, sin condiciones ni cobro.
2. Copia de seguridad automática programada, que no dependa de que el proveedor
   se acuerde de hacerla.
3. Procedimiento de salida escrito: qué pasa con los datos, el dominio y el
   sitio el día que el cliente decida irse.

Sin esas tres cláusulas, el Modelo A no se ofrece.

**Modelo B — Cuentas a nombre del cliente, proveedor como administrador
invitado.** Es el predeterminado para el paquete Todo Incluido, para clientes
del sector salud, y para cualquier cliente que pregunte de quién son los datos
antes de que tú lo menciones. Elimina de raíz el reclamo de secuestro de datos,
sube el valor percibido de la mensualidad (se paga por operación y soporte, no
por tener acceso) y deja los datos personales bajo la cuenta de quien de verdad
es responsable de ellos.

Su costo: se pierde la consolidación, así que el cliente carga los planes Pro
completos. **Si el cliente elige el Modelo B, la mensualidad sube** para
compensar, o los planes se facturan aparte a su nombre y tú cobras solo tu
servicio. Dilo en la venta, no después.

**Cómo decidir en 10 segundos:** si el cliente maneja datos sensibles, si ya
preguntó por la propiedad de los datos, o si el contrato es grande, ve a
Modelo B. En cualquier otro caso, Modelo A con las tres cláusulas.

El dominio se compra o se transfiere **a nombre del cliente en los dos
modelos**. Sin excepción.

### Traspaso paso a paso — solo si eligieron Modelo B

1. El cliente crea su cuenta de Supabase con un correo del negocio, no personal
   (`admin@` o `gerencia@`, algo que sobreviva si esa persona se va).
2. El cliente crea la organización a su nombre.
3. Desde la cuenta del proveedor: Supabase → proyecto → Settings → General →
   transferir el proyecto a la organización del cliente. Si esa opción no está
   disponible en el plan, la alternativa es crear el proyecto en la organización
   del cliente y migrar el esquema y los datos con la migración SQL más un
   volcado; guía al usuario en eso.
4. El cliente invita al proveedor como miembro de la organización con rol de
   administrador. Verifiquen juntos que el proveedor entra.
5. Repite lo mismo en Vercel: cuenta del cliente, importar el repositorio,
   cargar las variables de entorno, y el proveedor invitado al equipo.
6. El dominio se compra o se transfiere a nombre del cliente. Siempre.
7. El repositorio de GitHub puede quedar del proveedor si el código es su
   producto, pero eso se dice por escrito y se acuerda: "el código es mío, los
   datos y las cuentas son tuyos". Nada de ambigüedad.
8. Guarda con el usuario un documento de una página con: quién es dueño de qué,
   correos usados y quién tiene acceso. Ese documento se le envía al cliente.

Recuérdale al usuario que él nunca guarda ni pide contraseñas del cliente: entra
por invitación a su propia cuenta.

## Fase 3 — Manual de uso del cliente

Genera un archivo markdown de **máximo 2 páginas**, escrito para alguien que no
es técnico, con exactamente estas seis cosas y en este orden:

1. Ver la agenda del día.
2. Bloquear horas o un día completo.
3. Cancelar una cita.
4. Cambiar precios o servicios.
5. Revisar los datos de un cliente.
6. Qué hacer si algo falla.

Usa la plantilla de `references/plantillas-entrega.md`, rellénala con el nombre
real del negocio, las URLs reales y el vocabulario del nicho (paciente, cliente,
mascota, alumno). Reglas de redacción: frases cortas, sin palabras como deploy,
build, base de datos o RLS, cada instrucción empieza con un verbo, y cada punto
cabe en pantalla sin desplazarse. Entrégalo en PDF además del markdown si el
usuario puede generarlo.

## Fase 4 — Capacitación de 30 minutos con el equipo

Se hace con el dueño Y con quien va a usar el sistema todos los días. Si
recepción no está en la sala, el sistema no se va a usar.

Estructura, minuto a minuto, desarrollada en el archivo de referencia:
0–3 encuadre, 3–8 reserva real desde el celular, 8–15 el panel y las seis tareas,
15–22 práctica del equipo con las manos en el teclado, 22–27 objeciones y
acuerdos, 27–30 cierre, canal de soporte y la métrica que se va a revisar.

Objeciones internas que aparecen casi siempre, y cómo se manejan:

- *"Yo prefiero el cuaderno, así lo hemos hecho siempre."* No pelees con el
  cuaderno. Propón dos semanas de convivencia: siguen anotando y además revisan
  la pantalla. La pantalla gana sola cuando el cuaderno se queda corto.
- *"¿Esto me va a quitar el trabajo?"* Al contrario: deja de contestar el mismo
  mensaje treinta veces al día para dedicarse a quien ya está en el local. Dilo
  con nombre propio y ejemplos de su día.
- *"La gente mayor no va a saber usarlo."* Cierto en parte, y por eso el teléfono
  sigue existiendo. El sistema atiende a quien escribe de noche y fin de semana,
  que hoy simplemente se pierde.
- *"¿Y si se llena de citas falsas?"* Muestra en vivo cómo se cancela una cita y
  cómo se bloquea un horario. El miedo se va cuando ven que tienen el control.
- *"Yo no sé de computadores."* Nunca respondas "es facilísimo". Siéntalos a
  hacerlo ellos mismos una vez, con el manual al lado. Que lo logren delante de
  todos es la mejor capacitación posible.

Cierra con dos acuerdos concretos: quién revisa la agenda cada mañana y a qué
hora, y por qué canal se avisa si algo falla.

## Fase 5 — Los primeros 30 días

Esto es lo que hace que la segunda mensualidad se cobre sin discusión.

- **Semana 1.** Revisa: reservas creadas, errores en los registros, si el panel
  se está usando, si hay horarios mal configurados y si llegan los correos.
  Corrige lo que aparezca sin pedir permiso ni cobrar aparte. Envía el mensaje 1
  del archivo de referencia. Métrica a mostrar: **cuántas reservas entraron sin
  que nadie del negocio contestara un mensaje.**
- **Semana 2.** Revisa: horarios que se llenan y horarios muertos, cancelaciones,
  si el equipo bloquea horas por su cuenta. Ajusta duraciones o servicios según
  el uso real. Envía el mensaje 2. Métrica: **reservas fuera del horario de
  atención** (las de la noche y el fin de semana, que antes se perdían).
- **Semana 4.** Reunión corta o audio con el dueño. Revisa: total del mes,
  tendencia semana a semana, servicio más reservado y horas pico. Envía el
  mensaje 3 con el resumen. Métrica: **cuánto vale en dinero lo que entró por el
  sistema**, calculado con los precios reales del negocio. Ese número es el que
  justifica la mensualidad, y va comparado contra el valor de la mensualidad en
  la misma frase.

Y aquí, no antes, es donde se pide el testimonio (Fase 7).

## Fase 6 — Alcance del mantenimiento mensual, por escrito

Se envía el mismo día de la entrega, no cuando aparece el primer conflicto.

**Entra en la mensualidad:** hosting y base de datos operativos, copia de
seguridad, monitoreo de que el sitio esté arriba, corrección de errores del
sistema, cambios menores de textos y precios, agregar o quitar servicios,
cambios de horario, y soporte por el canal acordado en horario hábil.

**NO entra:** funciones nuevas, integraciones con otros sistemas (pasarela de
pago, WhatsApp, facturación, historia clínica), rediseños, páginas nuevas,
migraciones a otra plataforma, capacitaciones adicionales fuera de la primera, y
soporte fuera de horario.

**Guion para cuando el cliente pida algo fuera de alcance.** Nunca digas "eso no
entra" y punto. Usa esta secuencia:

1. Reconoce y valida: "buena idea, eso sí se puede hacer".
2. Ubica: "eso es una función nueva, no está dentro del mantenimiento".
3. Cotiza en el mismo mensaje: alcance en una frase, precio y tiempo.
4. Da salida: "si prefieres, lo dejamos anotado para más adelante y seguimos
   como vamos".

Si el pedido toma menos de 15 minutos, hazlo sin cobrar y dile que lo hiciste
como cortesía y que normalmente sería un cambio cotizado. Eso construye la
relación y a la vez marca el límite.

## Fase 7 — Testimonio y referidos

Momento correcto: cuando el cliente acaba de ver un resultado concreto. El mejor
día es el de la reunión de la semana 4, justo después de mostrarle la métrica de
dinero; el segundo mejor, cualquier día en que él escriba algo bueno sin que se
lo pidan. Nunca el día de la entrega: todavía no tiene nada que contar.

Pide UNA cosa a la vez, primero el testimonio y después los referidos, y usa el
texto literal del archivo de referencia. Para el testimonio, ofrece siempre las
tres preguntas que lo hacen fácil (cómo era antes, qué cambió, a quién se lo
recomendarías) y acepta audio o video de celular: son mejores que un texto pulido.
Para los referidos, no pidas "si conoces a alguien"; pide dos nombres concretos
de negocios parecidos y ofrece un beneficio real, como un mes de mensualidad
gratis por cada referido que firme.

## Reglas duras

- Nada se entrega sin la revisión de seguridad en verde.
- Alcance por escrito el mismo día de la entrega, siempre.
- No se guardan contraseñas del cliente: se entra por invitación.
- La métrica del mes se calcula con datos reales, nunca inventada ni redondeada
  hacia arriba.
- Si el cliente pide guardar datos sensibles o clínicos, la respuesta es no, por
  escrito y con la razón.
