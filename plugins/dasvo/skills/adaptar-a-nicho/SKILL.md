---
name: adaptar-a-nicho
description: Adapta el sistema de reservas base (construido para un consultorio odontológico) a otro tipo de negocio local, cambiando reglas de negocio, modelo de datos, vocabulario, servicios y estilo visual, no solo los colores. Trae 12 perfiles de nicho listos con servicios, precios orientativos, horarios, paleta y la diferencia estructural de cada uno.
when_to_use: Úsala cuando el usuario quiera usar el mismo sistema para otro rubro o diga cosas como "adaptar el sistema a una barbería", "lo mismo pero para un spa", "quiero venderlo a una veterinaria", "cambiar el sistema de odontología a peluquería", "sirve para un taller mecánico", "cómo lo hago para un salón de uñas", "adaptalo a una academia", "el sistema para psicologia", "cambiar de nicho", "reusar el proyecto para otro cliente", "que diga cliente y no paciente", "necesito que agende por barbero", "mi cliente es un estudio de tatuajes", "esto es para fisioterapia", "adaptar a otro negocio", "clonar el proyecto para otro rubro". También cuando ya tenga el sistema base funcionando y el cliente nuevo no sea un consultorio.
---

# Skill: Adaptar el Sistema de Citas a Otro Nicho

## Tu rol

Eres quien convierte el sistema base en un producto que se siente hecho a la
medida de OTRO negocio. La persona que te habla probablemente no sabe programar.

- Adaptar NO es cambiar colores y textos. Es cambiar reglas de negocio y, casi
  siempre, el modelo de datos. Si solo cambias colores, entregas un producto que
  falla el primer día.
- UNA instrucción a la vez cuando el usuario deba hacer algo fuera de la terminal.
- No avances de paso sin la confirmación explícita del usuario.
- Español simple, cero jerga sin explicarla en la misma frase.

## Paso 0 — Confirmar el punto de partida

1. Verifica que existe un proyecto con el sistema base funcionando (busca
   `CLAUDE.md` en la raíz y el flujo `/agendar`). Si no existe, dile que primero
   hay que construirlo con la skill `sistema-de-citas`.
2. Pregunta si esto es una copia para un cliente nuevo o un cambio sobre el
   proyecto actual. Si es copia, indícale crear una carpeta nueva y trabajar ahí:
   nunca se le mete mano al proyecto de un cliente que ya está en producción.
3. Confirma que el proyecto está limpio en git antes de tocar nada.

## Paso 1 — Elegir el nicho y cargar el perfil

Pregunta: "¿A qué tipo de negocio lo vamos a adaptar?" Ofrece la lista de los 12
perfiles disponibles: consultorio odontológico, barbería, spa, clínica estética,
veterinaria, fisioterapia, estudio de tatuajes, salón de uñas, peluquería, taller
mecánico, academia o centro de clases, consultorio de psicología.

Cuando responda, lee el perfil completo en `references/nichos.md` y muéstraselo
resumido (servicios, horario, diferencia estructural, paleta). Recuérdale que
los precios de ahí son ORIENTATIVOS y hay que reemplazarlos por los reales del
cliente. Pregunta qué cambia respecto al perfil.

Si el nicho no está en la lista, construye el perfil con él usando las mismas
nueve casillas del archivo de referencia y guárdalo ahí antes de seguir.

## Paso 2 — Las diferencias estructurales (esta es la parte que importa)

El sistema base asume: **un profesional, una cita por franja, duración fija,
un solo recurso**. Casi ningún nicho cumple eso. Identifica cuál de estos
cambios aplica y díselo al usuario en español antes de tocar código:

- **Varios profesionales en paralelo (barbería, peluquería, salón de uñas,
  fisioterapia).** Cambia el modelo de datos: nace la tabla `profesionales` y
  cada cita guarda `profesional_id`. La disponibilidad deja de ser "¿está libre
  esa hora?" y pasa a ser "¿hay al menos un profesional libre a esa hora?". El
  panel necesita filtro por profesional y vista de agenda por columna. Agrega en
  el flujo de reserva la opción "cualquiera disponible". El horario de atención
  ya no es uno solo: cada profesional tiene el suyo y sus días libres.
- **Un recurso además del profesional (spa, clínica estética).** Un servicio
  ocupa a la vez a la terapeuta Y una cabina o sala. Nace la tabla `recursos` y
  la relación servicio → recurso requerido. Un horario está disponible solo si
  hay profesional libre Y recurso libre. Este es el caso donde más se equivoca
  la gente: se agenda una hora con terapeuta disponible pero sin cabina.
- **Bloque de recuperación o limpieza posterior (clínica estética, algunos
  procedimientos odontológicos).** El servicio tiene `duracion_minutos` y además
  `buffer_posterior_minutos`. La franja que se bloquea en la agenda es la suma
  de las dos; lo que se le muestra y se le cobra al cliente final es solo la
  primera. Sin esto, el negocio queda con citas pegadas y colapsa.
- **Una segunda entidad además del cliente (veterinaria).** La cita necesita
  dueño Y mascota: nombre de la mascota y especie como campos obligatorios, raza
  y edad opcionales. Un dueño puede tener varias mascotas, así que la mascota no
  es un campo suelto del formulario, es un registro propio ligado al dueño.
- **Agenda por día o franja, no por hora exacta (taller mecánico).** Desaparece
  el cálculo de slots por minutos. Aparece: cupo máximo de vehículos por día (las
  bahías del taller) y franjas amplias tipo mañana o tarde. El formulario pide
  datos del vehículo (placa, marca, modelo, año), no un servicio con duración.
- **Cupos grupales en vez de citas individuales (academia o centro de clases).**
  Este es el cambio más grande. La unidad deja de ser la cita y pasa a ser la
  CLASE: día, hora, profesor, cupo máximo. La reserva es una inscripción a esa
  clase. Un mismo horario admite muchas personas hasta llenar el cupo. El panel
  muestra la lista de inscritos por clase y el porcentaje de ocupación, no una
  agenda de citas.

Explica al usuario cuál le toca y qué implica en trabajo. Pide confirmación
antes de continuar.

## Paso 3 — Vocabulario coherente en toda la interfaz

El vocabulario se cambia de punta a punta: interfaz, correos, mensajes de error,
panel y nombres de campos visibles. Un solo "paciente" olvidado en una barbería
delata que el sistema es reciclado.

Toma del perfil del nicho las tres palabras clave y aplícalas en todas partes:

- A quién se atiende: paciente / cliente / mascota y dueño / alumno.
- Qué se agenda: cita / turno / reserva / sesión / clase.
- Quién atiende: doctora / barbero / terapeuta / estilista / manicurista /
  tatuador / fisioterapeuta / mecánico / profesor / psicóloga.

Después de aplicarlo, busca en todo el proyecto las palabras del nicho anterior
y muestra al usuario la lista de coincidencias restantes. Debe quedar en cero.

## Paso 4 — Reescribir el CLAUDE.md ANTES de tocar código

No modifiques ni un archivo de la aplicación hasta que el `CLAUDE.md` esté
actualizado y aprobado. Actualiza:

1. Descripción del negocio, ciudad y zona horaria.
2. Tabla de servicios con duración, buffer si aplica y precio real.
3. Horario de atención, y horarios por profesional si hay varios.
4. Reglas de negocio nuevas del nicho (la propia del perfil incluida).
5. Vocabulario oficial del proyecto (las tres palabras del Paso 3).
6. Datos que se le piden al cliente final y los que están PROHIBIDOS.
7. Estilo visual: paleta en hex y tipografía.

Muestra el CLAUDE.md completo y pide un OK explícito. Si el usuario cambia algo,
edítalo y vuelve a pedir el OK.

## Paso 5 — Reglas del sistema base que ya no aplican

Antes de escribir código nuevo, haz la lista de lo que sobra y proponlo para
eliminación explícita, punto por punto. Nunca dejes reglas muertas "por si acaso":
son la fuente número uno de bugs raros y de campos vacíos en la base de datos.

Revisa al menos: campo "motivo de consulta", validaciones de anticipación mínima
que el nicho no necesita, estados de cita que no existen en este negocio, textos
legales de salud en negocios que no son de salud, la restricción de un solo
profesional, la duración fija por servicio, y cualquier servicio del negocio
anterior que quedó en la base de datos.

Preséntalo así y espera respuesta:

```
SOBRA DEL SISTEMA ANTERIOR
1. [qué es] — [dónde está] — propongo: ELIMINAR / CONSERVAR porque...
2. ...
¿Confirmas que elimine los marcados?
```

Lo que se elimina se elimina de verdad: código, columna en la base de datos (con
su migración) y texto en la interfaz.

## Paso 6 — Paleta y tipografía del nicho

Aplica la paleta y la tipografía recomendadas en el perfil del nicho. Una barbería
oscura con dorado y una tipografía condensada no se ve como un spa en tonos arena
con serif, y ninguno de los dos se ve como el azul clínico del consultorio.

1. Muéstrale al usuario los colores en hex con una frase de por qué encajan.
2. Ofrece cambiar el color primario si el negocio ya tiene identidad propia.
3. Cambia también la tipografía, el radio de los bordes y las fotos o iconos de
   ejemplo. La tipografía es la mitad del cambio de tono y casi nadie la toca.

## Paso 7 — Aplicar el cambio en el código, por etapas verificadas

Nunca todo de una vez. En este orden, y al final de cada etapa corres la
aplicación, la pruebas tú, le dices al usuario exactamente qué probar y esperas
su confirmación:

1. Base de datos: migración SQL con las tablas y columnas nuevas, y el borrado
   de lo que sobra. Actualiza las políticas RLS para las tablas nuevas.
2. Datos de servicios, profesionales y horarios del nicho.
3. Lógica de disponibilidad (aquí vive la diferencia estructural del Paso 2).
   Valídala siempre en el servidor.
4. Flujo de reserva y formulario con los datos del nicho.
5. Panel del negocio con las vistas que el nicho necesita.
6. Vocabulario y estilo visual.
7. Intento de romper el sistema: reservar en el pasado, fuera de horario, sobre
   un bloqueo, dos veces la misma franja, y el caso propio del nicho (dos citas
   al mismo barbero, cabina ocupada, cupo lleno de la clase, cupo de bahías del
   taller). Todo debe fallar con un mensaje amable.

## Paso 8 — Cierre

Al terminar, dile textualmente al usuario que antes de mostrarle nada al cliente
debe correr la revisión de seguridad, y ejecuta la skill `seguridad-web` si está
instalada. El cambio de nicho toca la base de datos y las políticas RLS: es
exactamente el momento donde se filtran datos por descuido.

Después ofrécele la skill `entregar-al-cliente` para el proceso de entrega.

## Reglas duras

- El CLAUDE.md se actualiza y se aprueba antes que el código. Siempre.
- Toda regla de negocio nueva se valida en el servidor, no solo en el formulario.
- Nada de datos clínicos, diagnósticos ni información de salud, en ningún nicho.
- Precios del archivo de referencia = orientativos. Se reemplazan por los reales.
- No agregues funciones que el usuario no pidió; propónlas al final de la etapa.
