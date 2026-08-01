# Perfiles de nicho para el sistema de reservas

Cómo usar este archivo: busca el nicho, lee las nueve casillas del perfil y
llévalas al `CLAUDE.md` del proyecto.

**Los precios son ORIENTATIVOS** (pesos colombianos, negocio de barrio o de
ciudad intermedia, referencia 2025-2026). Sirven para llenar el sistema de
ejemplo y para tener una conversación con el dueño, no para cobrarle a nadie.
Siempre se reemplazan por los precios reales del cliente antes de publicar.
En otro país, se cambian por moneda local y valores locales.

---

## 1. Consultorio odontológico (sistema base)

- **Cliente final:** persona que necesita atención dental, casi siempre agenda
  para sí misma o para un hijo. Llega por recomendación o por buscar en Google.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Valoración inicial | 30 min | $0 – $80.000 |
  | Limpieza y profilaxis | 45 min | $120.000 – $200.000 |
  | Resina o calza | 60 min | $150.000 – $300.000 |
  | Blanqueamiento | 60 min | $350.000 – $900.000 |
  | Extracción simple | 45 min | $150.000 – $350.000 |
  | Control de ortodoncia | 30 min | $80.000 – $150.000 |
- **Horario típico:** lunes a viernes 8:00–12:00 y 14:00–18:00; sábados
  8:00–12:00. Almuerzo cerrado.
- **Diferencia estructural:** ninguna, este ES el sistema base. Un profesional,
  una cita por franja, duración fija por servicio, un consultorio.
- **Vocabulario:** paciente / cita / doctor o doctora.
- **Datos que se piden:** nombre completo, celular, correo, motivo general en una
  línea (dolor, control, limpieza, estética). Nada más.
- **Paleta:** fondo `#FFFFFF`, superficie `#E8F1F8`, primario `#0F4C81`,
  secundario `#4FA3C7`, texto `#1F2933`. Tipografía Inter. Bordes suaves (8 px).
- **Regla propia del nicho:** las urgencias por dolor no se agendan en línea. El
  formulario debe mostrar el teléfono del consultorio con el mensaje "si tienes
  dolor fuerte, llámanos, no esperes un cupo en línea".

---

## 2. Barbería

- **Cliente final:** hombre entre 18 y 45 años, decide rápido, quiere ver el
  cupo y confirmarlo en menos de un minuto desde el celular. Suele tener barbero
  preferido y no lo cambia.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Corte clásico | 30 min | $20.000 – $45.000 |
  | Corte + barba | 45 min | $35.000 – $70.000 |
  | Perfilado de barba | 20 min | $15.000 – $30.000 |
  | Cejas | 10 min | $8.000 – $15.000 |
  | Tinte o camuflaje de canas | 60 min | $50.000 – $120.000 |
  | Corte niño | 30 min | $18.000 – $35.000 |
- **Horario típico:** martes a sábado 9:00–20:00 corrido, domingo 10:00–15:00,
  lunes cerrado. Los picos son jueves a sábado en la tarde.
- **Diferencia estructural clave:** **varios barberos atendiendo en paralelo.**
  El sistema base asume un solo profesional; aquí eso rompe todo. Nace la tabla
  `profesionales` (nombre, foto, días y horario propios, activo sí/no) y cada
  cita guarda `profesional_id`. La disponibilidad se calcula por profesional, no
  por local. El flujo de reserva pide barbero (con opción "cualquiera
  disponible") ANTES de mostrar las horas. El panel necesita vista de agenda por
  columnas, una por barbero, y filtro por barbero. Los días libres son
  individuales: si Andrés descansa el miércoles, el local sigue abierto.
- **Vocabulario:** cliente / turno / barbero.
- **Datos que se piden:** nombre, celular, barbero preferido. El correo es
  opcional; muchos no lo dan y obligarlo hace que abandonen la reserva.
- **Paleta:** fondo `#111111`, superficie `#1C1C1C`, primario `#C9A227` (dorado),
  texto `#F5F5F0`, texto secundario `#7A7A7A`. Tipografía de títulos condensada
  y en mayúsculas (Oswald o Bebas Neue), cuerpo en Inter. Bordes rectos (2–4 px).
- **Regla propia del nicho:** política de retraso visible al confirmar. Después
  de 10 minutos el turno se libera, porque un barbero con 30 minutos por corte no
  puede sostener a nadie. Muéstralo en la pantalla de confirmación y en el
  recordatorio.

---

## 3. Spa

- **Cliente final:** mujer entre 28 y 55 años, reserva con días de anticipación,
  a veces para dos personas. Valora que la reserva se sienta calmada y cuidada.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Masaje relajante | 60 min | $90.000 – $180.000 |
  | Masaje descontracturante | 90 min | $120.000 – $220.000 |
  | Limpieza facial | 60 min | $80.000 – $170.000 |
  | Exfoliación corporal | 90 min | $150.000 – $280.000 |
  | Ritual en pareja | 120 min | $300.000 – $500.000 |
  | Drenaje linfático | 60 min | $110.000 – $200.000 |
- **Horario típico:** lunes a sábado 9:00–19:00, domingo 10:00–16:00. Última
  reserva a la hora de cierre menos la duración del servicio.
- **Diferencia estructural clave:** **el servicio ocupa una cabina o sala además
  del profesional.** Nace la tabla `recursos` (cabina 1, cabina 2, sala de
  pareja, sala de vapor) y la relación servicio → tipo de recurso requerido. Un
  horario está disponible solo si hay terapeuta libre **Y** recurso libre. El
  ritual en pareja ocupa dos terapeutas y una sala doble a la vez. Sin esto, el
  sistema vende una hora que el spa no puede atender, que es el error más caro
  del nicho.
- **Vocabulario:** cliente / reserva / terapeuta.
- **Datos que se piden:** nombre, celular, correo, y si aplica: si viene sola o
  en pareja. Nunca condiciones médicas por escrito en el formulario; eso se
  pregunta en el local, en papel, y no entra a la base de datos.
- **Paleta:** fondo `#F7F4EF`, superficie `#EFEAE1`, primario `#6B8E7B` (salvia),
  secundario `#C9B79C` (arena), texto `#3E4A42`. Títulos en serif
  (Cormorant Garamond), cuerpo en Inter. Bordes muy redondeados (16–20 px),
  mucho espacio en blanco.
- **Regla propia del nicho:** margen de 15 minutos entre reservas de la misma
  cabina para adecuación y aseo. Se implementa como buffer del recurso, no como
  buffer del terapeuta.

---

## 4. Clínica estética

- **Cliente final:** persona de 25 a 55 años, ticket alto, compara antes de
  decidir. Muchas veces la primera visita es solo una valoración.
- **Servicios típicos:**
  | Servicio | Duración | Buffer | Precio orientativo |
  |---|---|---|---|
  | Valoración | 30 min | 0 | $0 – $100.000 |
  | Limpieza facial profunda | 60 min | 15 min | $120.000 – $250.000 |
  | Peeling químico | 45 min | 20 min | $200.000 – $450.000 |
  | Toxina botulínica | 45 min | 30 min | $600.000 – $1.200.000 |
  | Ácido hialurónico | 60 min | 30 min | $900.000 – $2.000.000 |
  | Depilación láser (por zona) | 30 min | 10 min | $80.000 – $300.000 |
- **Horario típico:** lunes a viernes 9:00–18:00, sábado 9:00–14:00.
- **Diferencia estructural clave:** **bloque de recuperación después de ciertos
  procedimientos.** Cada servicio tiene `duracion_minutos` y
  `buffer_posterior_minutos`. La franja que se bloquea en la agenda es la suma;
  lo que se le muestra y se le cobra al cliente es solo la duración. El buffer
  no aparece como servicio ni en la confirmación. Además hay recursos: sala de
  procedimientos y equipos (el láser es uno solo y no se puede duplicar).
- **Vocabulario:** paciente / cita / doctora o especialista.
- **Datos que se piden:** nombre, celular, correo, procedimiento de interés.
  Prohibido: antecedentes médicos, medicamentos, embarazo, alergias. Eso se
  levanta en consentimiento informado en papel o en el software clínico del
  cliente, jamás en este sistema.
- **Paleta:** fondo `#FFFFFF`, superficie `#F7F1F0`, primario `#B08D9A`,
  acento `#D4AF7A` (dorado suave), texto `#1C1C1C`. Títulos en Playfair Display,
  cuerpo en Inter. Bordes 10 px, fotografía grande y limpia.
- **Regla propia del nicho:** ciertos procedimientos exigen valoración previa. Si
  el paciente elige uno de esos y no tiene una valoración registrada, el sistema
  lo redirige a agendar la valoración y se lo explica en una frase.

---

## 5. Veterinaria

- **Cliente final:** dueño de mascota, agenda para su animal, a veces tiene
  varios. Emocional y sensible al trato.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Consulta general | 30 min | $45.000 – $90.000 |
  | Vacunación | 20 min | $40.000 – $120.000 |
  | Desparasitación | 15 min | $25.000 – $60.000 |
  | Baño y peluquería | 90 min | $45.000 – $120.000 |
  | Control post operatorio | 20 min | $40.000 – $80.000 |
  | Corte de uñas y limpieza de oídos | 20 min | $20.000 – $45.000 |
- **Horario típico:** lunes a sábado 8:00–18:00, domingo 9:00–13:00.
- **Diferencia estructural clave:** **la cita tiene dos entidades, dueño y
  mascota.** El nombre y la especie de la mascota son obligatorios; raza, edad y
  peso aproximado son opcionales. Un dueño puede tener varias mascotas, así que
  la mascota se guarda como registro propio ligado al dueño, no como un campo
  suelto del formulario: si no, el sistema no sabe distinguir "Luna la gata" de
  "Luna la perra" del mismo dueño. El panel debe mostrar mascota y especie antes
  que el nombre del dueño, porque así trabaja el veterinario.
- **Vocabulario:** dueño y mascota / cita / veterinario o veterinaria.
- **Datos que se piden:** nombre del dueño, celular, correo, nombre de la
  mascota, especie (perro, gato, otro), raza y edad opcionales, motivo general.
  Nada de historia clínica ni diagnósticos.
- **Paleta:** fondo `#FFFFFF`, superficie `#EAF7F5`, primario `#2F9E8F`,
  acento `#F4A261`, texto `#2B3A42`. Tipografía Nunito, bordes muy redondeados
  (14–18 px), iconografía amable.
- **Regla propia del nicho:** el baño y la peluquería son un servicio de estadía,
  no una cita de 90 minutos exactos. Se agenda por franja de entrega
  (mañana o tarde) y el sistema avisa "lo dejas a esta hora y lo recoges en la
  franja X", con cupo máximo de mascotas por franja.

---

## 6. Fisioterapia

- **Cliente final:** persona con lesión, dolor crónico o recuperación
  posquirúrgica; también deportistas. Casi nunca viene una sola vez.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Valoración inicial | 60 min | $70.000 – $130.000 |
  | Sesión de terapia física | 45 min | $60.000 – $110.000 |
  | Terapia deportiva | 60 min | $80.000 – $150.000 |
  | Punción seca | 45 min | $90.000 – $160.000 |
  | Terapia a domicilio | 60 min | $100.000 – $200.000 |
  | Paquete de 10 sesiones | 10 × 45 min | $500.000 – $950.000 |
- **Horario típico:** lunes a viernes 7:00–19:00, sábado 8:00–13:00.
- **Diferencia estructural clave:** **el tratamiento es una serie, no una cita
  suelta.** Nace la tabla `paquetes` o `tratamientos` (paciente, total de
  sesiones, sesiones usadas) y la cita se liga a un tratamiento. El flujo debe
  permitir agendar varias sesiones de una vez, típicamente el mismo día y hora
  cada semana durante N semanas, verificando disponibilidad de todas antes de
  confirmar ninguna. El panel muestra "sesión 3 de 10" y avisa cuando quedan dos.
  También hay varios fisioterapeutas y camillas, así que aplica lo de varios
  profesionales.
- **Vocabulario:** paciente / sesión / fisioterapeuta.
- **Datos que se piden:** nombre, celular, correo, zona del cuerpo a tratar en
  una palabra (espalda, rodilla, hombro), si viene remitido sí/no. Prohibido:
  diagnóstico médico, historia clínica, resultados de exámenes.
- **Paleta:** fondo `#FFFFFF`, superficie `#EEF5FA`, primario `#1B6CA8`,
  acento `#34C6A0`, texto `#22303C`. Tipografía Inter, bordes 10 px, estética
  limpia y deportiva.
- **Regla propia del nicho:** la valoración inicial es obligatoria antes de la
  primera sesión de terapia. Si el paciente es nuevo, el sistema solo le ofrece
  valoración.

---

## 7. Estudio de tatuajes

- **Cliente final:** persona de 18 a 40 años que ya vio el trabajo del artista en
  Instagram. Llega con una idea, no con un servicio de catálogo.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Asesoría y diseño | 30 min | $0 – $50.000 (abonable) |
  | Tatuaje pequeño | 60–90 min | $150.000 – $350.000 |
  | Tatuaje mediano | 3 h | $400.000 – $800.000 |
  | Sesión grande | 6 h | $900.000 – $2.000.000 |
  | Retoque | 45 min | $0 – $150.000 |
  | Piercing | 30 min | $60.000 – $150.000 |
- **Horario típico:** martes a sábado 12:00–20:00. Lunes cerrado. Sesiones largas
  solo en la franja de la mañana o del inicio de la tarde.
- **Diferencia estructural clave:** **la duración no la define el catálogo, la
  define el artista, y la reserva requiere aprobación y abono.** El estado de la
  cita cambia: `solicitada → aprobada → con abono → realizada / cancelada`. El
  cliente pide fecha y describe la idea con una foto de referencia; el artista
  confirma la duración real y el precio; solo después se bloquea la agenda. La
  cita se agenda por bloques largos (2, 3, 6 horas), no por slots de 30 minutos.
  Si hay varios artistas, aplica también lo de varios profesionales, con la
  particularidad de que cada uno tiene estilo propio y el cliente elige por eso.
- **Vocabulario:** cliente / sesión / artista o tatuador.
- **Datos que se piden:** nombre, celular, Instagram (aquí sí sirve), zona del
  cuerpo, tamaño aproximado en centímetros, descripción de la idea, foto de
  referencia opcional, confirmación de que es mayor de edad.
- **Paleta:** fondo `#0B0B0B`, superficie `#161616`, primario `#B3121D`,
  texto `#E5E5E5`, texto secundario `#8A8A8A`. Títulos en Anton o Archivo Black,
  cuerpo en Inter. Bordes rectos (0–2 px), mucho contraste, foto a pantalla
  completa.
- **Regla propia del nicho:** ninguna sesión se bloquea sin abono. El texto lo
  dice sin rodeos: "tu fecha se aparta cuando recibimos el abono; sin abono, el
  espacio sigue disponible para otros". Y el abono no es reembolsable si cancela
  con menos de 48 horas.

---

## 8. Salón de uñas

- **Cliente final:** mujer de 18 a 50 años, cliente recurrente cada 3 o 4
  semanas. Suele volver con la misma manicurista.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Manicure tradicional | 45 min | $25.000 – $45.000 |
  | Semipermanente | 60 min | $45.000 – $80.000 |
  | Uñas acrílicas | 120 min | $90.000 – $180.000 |
  | Retoque o relleno | 90 min | $70.000 – $130.000 |
  | Pedicure | 60 min | $35.000 – $70.000 |
  | Retiro de material | 30 min | $15.000 – $30.000 |
- **Horario típico:** lunes a sábado 9:00–19:00, domingo 10:00–15:00.
- **Diferencia estructural clave:** **servicios que se encadenan en la misma
  visita y suman duración.** Casi nadie pide un solo servicio: "manos y pies" es
  la norma. La reserva debe permitir seleccionar VARIOS servicios y calcular la
  franja total sumando duraciones, no una cita por servicio. Además hay varias
  manicuristas en paralelo (aplica lo de varios profesionales) y un tiempo de
  secado al final que ocupa la silla pero no a la profesional: si el negocio lo
  quiere modelar bien, ese es un buffer de recurso, no de persona.
- **Vocabulario:** cliente / cita / manicurista.
- **Datos que se piden:** nombre, celular, servicios elegidos, manicurista
  preferida. Correo opcional.
- **Paleta:** fondo `#FFF9FB`, superficie `#F2D9E0`, primario `#E48FA8`,
  acento `#7C3A57`, texto `#2B2226`. Tipografía Poppins, bordes 16 px, fotos
  cuadradas tipo galería de Instagram.
- **Regla propia del nicho:** al confirmar, el sistema muestra la hora de inicio
  y la hora estimada de salida ("terminas alrededor de las 4:30 p.m."). Es el
  dato que más reduce las quejas en este negocio.

---

## 9. Peluquería

- **Cliente final:** mujer u hombre de 20 a 60 años. En servicios de color, la
  visita dura horas y el precio depende del largo del cabello.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Corte dama | 45 min | $30.000 – $70.000 |
  | Corte caballero | 30 min | $20.000 – $45.000 |
  | Cepillado / blower | 45 min | $30.000 – $60.000 |
  | Tinte de raíz | 90 min | $90.000 – $180.000 |
  | Mechas o balayage | 180 min | $250.000 – $600.000 |
  | Keratina o alisado | 150 min | $200.000 – $500.000 |
  | Peinado para evento | 60 min | $60.000 – $150.000 |
- **Horario típico:** martes a sábado 9:00–19:00, domingo 10:00–15:00, lunes
  cerrado.
- **Diferencia estructural clave:** **el servicio tiene tiempo muerto interno.**
  Un tinte son 20 minutos de aplicación, 30 de espera con el producto puesto y 20
  de lavado y secado: durante la espera la estilista está libre y atiende a otra
  persona. Modelarlo como un bloque cerrado de 90 minutos hace que el salón
  pierda la mitad de su capacidad. El servicio se define en fases (activa,
  espera, activa) y la disponibilidad permite solapar la fase de espera de un
  cliente con la fase activa de otro. Si esto queda muy complejo para la primera
  versión, díselo al usuario con claridad: se puede lanzar con bloques cerrados y
  agregar las fases después, pero el dueño tiene que saber que está perdiendo
  cupos. También aplica lo de varios estilistas en paralelo.
- **Vocabulario:** cliente / cita / estilista.
- **Datos que se piden:** nombre, celular, correo, servicio, largo del cabello
  (corto, medio, largo) porque afecta duración y precio, estilista preferida.
- **Paleta:** fondo `#FAF7F5`, superficie `#F0EAE5`, primario `#2E2A27`,
  acento `#B98A5E` (cobre), texto `#6E645C`. Títulos en Jost o Marcellus, cuerpo
  en Inter. Bordes 6 px, estética editorial.
- **Regla propia del nicho:** el precio de color y mechas se muestra siempre como
  "desde $X, el valor final depende del largo y la cantidad de producto". El
  sistema no promete un precio cerrado en esos servicios: es la causa número uno
  de discusiones en caja.

---

## 10. Taller mecánico

- **Cliente final:** dueño de vehículo, hombre o mujer de 25 a 60 años. Quiere
  saber cuándo deja el carro y cuándo lo recoge, no a qué minuto entra.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Cambio de aceite y filtros | 45 min | $120.000 – $280.000 |
  | Diagnóstico o revisión general | 1 h | $50.000 – $150.000 |
  | Alineación y balanceo | 1 h | $80.000 – $160.000 |
  | Cambio de pastillas de freno | media jornada | $180.000 – $450.000 |
  | Sincronización | media jornada | $150.000 – $400.000 |
  | Alistamiento para tecnomecánica | 1 día | $100.000 – $300.000 |
- **Horario típico:** lunes a viernes 7:30–17:30, sábado 8:00–13:00. Recepción de
  vehículos de 7:30 a 10:00 para trabajos de jornada.
- **Diferencia estructural clave:** **se agenda por día y franja, no por hora
  exacta.** Desaparece el cálculo de slots por minutos. Aparecen: franjas
  (mañana, tarde, día completo) y **cupo máximo de vehículos por franja**, que es
  el número de bahías o elevadores del taller. La reserva es "tu carro entra el
  martes en la mañana", y la disponibilidad se calcula contando cuántos vehículos
  ya hay en esa franja. El formulario pide datos del vehículo, no solo de la
  persona.
- **Vocabulario:** cliente / cita o ingreso / mecánico o técnico.
- **Datos que se piden:** nombre, celular, placa, marca, línea o modelo, año,
  kilometraje aproximado, y la falla descrita en las palabras del cliente.
- **Paleta:** fondo `#F4F5F7`, superficie `#E4E7EC`, primario `#1F2A44`,
  acento `#F2610C`, texto `#101418`. Títulos en Barlow Condensed, cuerpo en
  Inter. Bordes 4 px, estética industrial y de alto contraste.
- **Regla propia del nicho:** ninguna reserva promete precio final. El sistema
  dice "el valor se confirma después del diagnóstico" y la confirmación incluye
  la frase "no iniciamos ningún trabajo sin tu autorización". Eso protege al
  taller y tranquiliza al cliente.

---

## 11. Academia o centro de clases

- **Cliente final:** el alumno, o el padre o madre que inscribe a un menor.
  Aplica a academias de idiomas, música, baile, yoga, natación o refuerzo escolar.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Clase de prueba | 60 min | $0 – $30.000 |
  | Clase suelta | 60 min | $20.000 – $45.000 |
  | Mensualidad 2 veces por semana | 8 clases | $120.000 – $250.000 |
  | Mensualidad 3 veces por semana | 12 clases | $160.000 – $320.000 |
  | Taller intensivo | 3 h | $80.000 – $200.000 |
  | Clase particular | 60 min | $50.000 – $120.000 |
- **Horario típico:** lunes a viernes 7:00–20:00 en bloques fijos, sábado
  8:00–14:00. Los horarios no son continuos: son clases programadas.
- **Diferencia estructural clave:** **cupos grupales, no citas individuales.**
  Es el cambio más profundo de todos. La unidad deja de ser la cita y pasa a ser
  la CLASE: día, hora, duración, profesor, salón, nivel y **cupo máximo**. La
  reserva es una `inscripcion` que liga alumno con clase. Un mismo horario admite
  muchas personas hasta llenar el cupo, y el sistema debe mostrar "quedan 3 de 12
  cupos". El panel deja de ser una agenda y pasa a ser la lista de inscritos por
  clase con su porcentaje de ocupación. Agrega lista de espera cuando el cupo se
  llena: en este nicho es una función que se vende sola.
- **Vocabulario:** alumno / clase o inscripción / profesor o profesora.
- **Datos que se piden:** nombre del alumno, edad, nombre del acudiente y celular
  si es menor de edad, correo, nivel o experiencia previa, clase elegida.
- **Paleta:** fondo `#FFFFFF`, superficie `#EEF2FF`, primario `#4338CA`,
  acento `#F59E0B`, texto `#1E1B4B`. Tipografía Sora para títulos e Inter para
  cuerpo. Bordes 12 px, estética clara y ordenada tipo horario escolar.
- **Regla propia del nicho:** una inscripción no se cancela sola. Si el alumno
  avisa que no asiste, el cupo se libera solo hasta 12 horas antes de la clase;
  después queda ocupado. Y una clase con menos del mínimo de inscritos se puede
  cancelar desde el panel, avisando a todos los inscritos.

---

## 12. Consultorio de psicología

- **Cliente final:** adulto que busca terapia, o padre que agenda para un menor.
  Es el nicho donde la privacidad y la discreción pesan más que cualquier
  funcionalidad.
- **Servicios típicos:**
  | Servicio | Duración | Precio orientativo |
  |---|---|---|
  | Primera consulta | 60 min | $80.000 – $180.000 |
  | Sesión de seguimiento | 50 min | $70.000 – $160.000 |
  | Sesión de pareja | 80 min | $120.000 – $250.000 |
  | Sesión familiar | 80 min | $130.000 – $260.000 |
  | Sesión en línea | 50 min | $60.000 – $150.000 |
- **Horario típico:** lunes a viernes 8:00–19:00, sábado 9:00–13:00. Espacio de
  10 minutos entre sesiones, siempre.
- **Diferencia estructural clave:** **cita recurrente en la misma franja fija**
  y separación estricta entre agenda presencial y en línea. El paciente
  típicamente conserva "los martes a las 5" durante meses: el sistema debe poder
  reservar la misma franja por N semanas de una sola vez. Las sesiones en línea
  no ocupan consultorio, así que si el profesional atiende ambas modalidades, la
  disponibilidad presencial depende del consultorio y la virtual no.
- **Vocabulario:** paciente o consultante / sesión / psicóloga o psicólogo.
- **Datos que se piden:** nombre (permite que sea solo el nombre de pila),
  celular, correo, modalidad (presencial o en línea), y si es primera vez sí/no.
  **Nada más.**
- **ADVERTENCIA OBLIGATORIA — este nicho no admite excepciones:** el sistema NO
  guarda ningún dato clínico ni motivo de consulta detallado. Nada de diagnóstico,
  síntomas, medicación, antecedentes, "cuéntanos qué te pasa", ni un campo de
  texto libre donde el paciente pueda escribirlo. Un campo abierto que diga
  "motivo" invita a escribir información de salud mental y convierte una base de
  datos de citas en un archivo clínico: eso implica obligaciones legales muy
  superiores, responsabilidad profesional del psicólogo y un riesgo real para la
  persona si hay una filtración. Si el cliente insiste en pedirlo, la respuesta
  es no, por escrito, y se le explica que sus notas clínicas van en su software
  clínico o en papel bajo llave, nunca aquí. Lo mismo aplica a los correos de
  confirmación: el asunto y el cuerpo nunca mencionan el motivo ni la palabra
  terapia si el paciente no lo autorizó.
- **Paleta:** fondo `#FBFAF8`, superficie `#EDF1F0`, primario `#5B7B7A`,
  secundario `#A8A29E`, texto `#2C2C2C`. Títulos en Lora, cuerpo en Inter.
  Bordes 12 px, tono sobrio, sin fotos de personas, sin lenguaje comercial.
- **Regla propia del nicho:** política de cancelación visible al confirmar. Una
  sesión cancelada con menos de 24 horas se cobra, porque ese espacio ya no se
  llena. Se redacta con cuidado y sin dureza, pero se muestra siempre.

---

## Plantilla para un nicho nuevo

Si el negocio no está en esta lista, completa estas nueve casillas con el usuario
antes de tocar código y agrega el perfil a este archivo:

1. Nombre del nicho
2. Quién es el cliente final
3. Servicios típicos con duración y precio orientativo
4. Horario típico
5. Diferencia estructural clave frente al sistema base
6. Vocabulario (a quién se atiende / qué se agenda / quién atiende)
7. Datos que se le piden al cliente final, y los prohibidos
8. Paleta en hex y tipografía
9. Una regla de negocio propia del nicho
