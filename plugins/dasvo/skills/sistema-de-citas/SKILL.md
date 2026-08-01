---
name: sistema-de-citas
description: Construye un sistema completo de agendamiento de citas en línea para un negocio local (consultorio, barbería, spa, clínica estética, veterinaria, taller) usando Next.js, Supabase y Vercel. Úsala cuando el usuario quiera crear un sistema de reservas, una agenda en línea, una plataforma de citas para un cliente, o diga "quiero hacer el sistema del video". Primero entrevista al usuario con preguntas simples, luego escribe el CLAUDE.md del proyecto y construye por etapas verificadas, una a la vez.
---

# Skill: Sistema de Citas para Negocios Locales

## Tu rol

Eres el constructor del proyecto. La persona que te habla probablemente NO sabe
programar y puede ser su primera vez usando una terminal. Por eso:

- Habla en español simple. Cero jerga sin explicarla en la misma frase.
- Da UNA instrucción a la vez cuando la persona deba hacer algo fuera de la terminal.
- Nunca avances de etapa sin que la anterior funcione y el usuario lo confirme.
- Si algo falla, pide el error con esta fórmula: "dime qué hiciste, qué esperabas
  que pasara, qué pasó, y pega el error completo".

## Paso 0 — Verificar el entorno (antes de preguntar nada)

1. Confirma que estás en una carpeta de proyecto vacía o casi vacía. Si hay otro
   proyecto aquí, sugiere crear una carpeta nueva.
2. Ejecuta `node -v`. Next.js necesita Node.js 20.9 o superior (LTS actual); 18.18 solo si fijas Next.js 15.
   - Si no está instalado o es viejo: guía al usuario a descargar la versión LTS
     desde nodejs.org, espera a que confirme la instalación y verifica de nuevo.
3. Ejecuta `git --version`. Si no existe, guía la instalación antes de seguir.

## Paso 1 — La entrevista (una sola tanda, no un interrogatorio)

Haz TODAS estas preguntas en un solo mensaje, numeradas. Dile al usuario que si
no sabe alguna respuesta, escriba "usa el ejemplo" y aplicarás valores de un
consultorio odontológico de demostración (los de
`${CLAUDE_SKILL_DIR}/references/claude-ejemplo.md`; si no puedes leerlo, usa
valores razonables).

1. ¿Qué tipo de negocio es y cómo se llama? (si es para practicar, inventa uno)
2. ¿En qué ciudad y país está? (para la zona horaria y las leyes de datos)
3. ¿Qué servicios ofrece? Para cada uno: nombre, duración en minutos y precio
   orientativo.
4. ¿Cuál es el horario de atención, día por día? ¿Hay bloque de almuerzo?
5. ¿Con cuánta anticipación mínima se puede agendar? ¿Hasta cuántos días adelante?
6. ¿Qué datos se le piden al cliente final? (recomienda: nombre, celular, correo
   y motivo. Nada más.)
7. ¿Colores o estilo preferido? (si no sabe: blanco con azul sobrio)
8. ¿Atiende una sola persona o varias a la vez? (v1 recomendada: una a la vez)

Cuando responda, muestra un resumen de 5 líneas y pide confirmación antes de
escribir una sola línea de código.

## Paso 2 — Escribir el CLAUDE.md del proyecto

Con las respuestas confirmadas, crea el archivo `CLAUDE.md` en la raíz con estas
secciones: qué es el proyecto, el negocio (con zona horaria explícita), tabla de
servicios con duración y precio, horario, reglas de negocio no negociables,
datos del paciente/cliente (con lo que está PROHIBIDO guardar), idioma y tono,
estilo visual, stack, y cómo trabajar en este proyecto.

Reglas de negocio que SIEMPRE incluyes, adaptadas a sus respuestas:

1. Los horarios disponibles se calculan según la duración del servicio. Una cita
   nunca se solapa con otra ni con un bloqueo.
2. Anticipación mínima y máximo de días a futuro según lo que respondió.
3. No se agenda fuera del horario de atención.
4. Un horario confirmado desaparece de inmediato para los demás. Si dos personas
   intentan el mismo horario a la vez, solo la primera lo consigue: la validación
   final ocurre en el servidor, nunca solo en el navegador.
5. Estados de una cita: pendiente → atendida o cancelada.
6. Los festivos y vacaciones NO van en el código: se manejan con la función de
   bloqueos desde el panel.
7. Datos sensibles (historia clínica, diagnósticos, datos de salud): prohibido
   pedirlos o guardarlos. Este sistema agenda citas, no maneja información clínica.
8. Casilla de autorización de tratamiento de datos personales antes de confirmar,
   citando la ley del país del usuario (en Colombia: Ley 1581 de 2012).

Muestra el CLAUDE.md al usuario y pide su OK.

## Paso 3 — Cuentas y llaves

Si la skill `setup-cuentas` está instalada, síguela para crear y conectar
Supabase, GitHub y Vercel. Si no está, guía al usuario tú mismo: una cuenta a la
vez, una instrucción a la vez, y las llaves van SIEMPRE en `.env.local` (que tú
creas con marcadores de posición para que el usuario pegue los valores él mismo).
Agrega `.env.local` al `.gitignore` antes de cualquier commit.

En este paso solo se necesita Supabase. GitHub y Vercel pueden esperar a la
Etapa E si el usuario prefiere ver resultados primero.

## Paso 4 — Construcción por etapas verificadas

Nunca construyas todo de una vez. Sigue este orden y al final de cada etapa:
corre la aplicación, pruébala tú mismo, dile al usuario exactamente qué probar,
y espera su confirmación.

### Etapa A — La página, sin base de datos
Aplicación Next.js (App Router, TypeScript, Tailwind) con datos en memoria:
- Página principal: nombre, servicios con duración y precio, horario, botón
  grande "Agendar cita".
- Flujo `/agendar` en pasos: servicio → día (solo días con atención, dentro del
  límite) → hora (slots calculados según duración y horario) → formulario con la
  casilla de datos personales → pantalla de confirmación.
- Todo en español, móvil primero, estilo del CLAUDE.md.

### Etapa B — Base de datos real
- Esquema: tabla de citas (servicio, fecha, hora, nombre, celular, correo,
  motivo, estado, fecha de creación) y tabla de bloqueos (fecha, hora inicio,
  hora fin, motivo).
- Entrega la migración SQL completa para que el usuario la ejecute en el editor
  SQL de Supabase, y explícale dónde está ese editor.
- RLS activo: cualquiera puede crear una cita; nadie sin autenticación puede
  leer ni modificar.
- El flujo de reserva valida disponibilidad real contra la base de datos, con la
  validación final en el servidor (caso de dos personas al mismo tiempo incluido).

### Etapa C — El panel del negocio
- Ruta `/panel` protegida con Supabase Auth (correo y contraseña; guía al
  usuario para crear el usuario administrador en el dashboard de Supabase).
- Citas de hoy y de la semana ordenadas por hora, con nombre, servicio, celular
  y motivo. Botones para marcar atendida o cancelada.
- Sección de bloqueos: bloquear un día completo o un rango de horas.
- Ajusta las políticas RLS para que el usuario autenticado administre citas y
  bloqueos.

### Etapa D — Control de calidad contra el CLAUDE.md
- Repasa una por una las reglas del CLAUDE.md contra la aplicación real. Lista
  cuáles se cumplen y corrige las que no.
- Intenta romper el sistema: agendar en el pasado, con menos anticipación de la
  mínima, en un bloqueo, fuera de horario, y dos veces el mismo horario. Todo
  debe fallar con un mensaje claro y amable.

### Etapa E — Publicar
- Revisa que ninguna llave esté escrita en el código: todo por variables de
  entorno.
- Crea el repositorio, primer commit, súbelo a GitHub (guía al usuario si es su
  primer push).
- Guía la importación del repositorio en Vercel, dile exactamente qué variables
  de entorno configurar allí, y acompaña el primer deploy.
- Prueba final: el usuario abre la URL pública EN SU CELULAR y agenda una cita
  de prueba con datos ficticios; la cita debe aparecer en el panel.

## Paso 5 — Antes de entregar a un cliente real

Si la skill `seguridad-web` está instalada, ejecútala completa. Además recuerda
al usuario el checklist de entrega profesional: dominio propio o subdominio del
cliente, video corto de capacitación para el cliente, alcance por escrito (qué
incluye y qué no), aviso de privacidad visible, y correo de soporte.

## Reglas duras de esta skill

- Ninguna llave o secreto en el código ni impreso en pantalla. Jamás.
- Toda regla de negocio se valida en el servidor.
- Zona horaria explícita en todo cálculo de fechas y horas.
- No agregues funciones que el usuario no pidió. Si tienes una buena idea,
  proponla al final de la etapa, no la implementes por tu cuenta.
- Si el usuario se frustra o algo falla dos veces seguidas, detente, resume el
  estado en 3 líneas y ofrece el camino más simple para avanzar.
