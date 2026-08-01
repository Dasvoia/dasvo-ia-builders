# CLAUDE.md — Consultorio Odontológico Dra. Ramírez

> Nombre y datos ficticios creados para este proyecto de demostración.
> Los parámetros (servicios, horarios, reglas) replican un caso real.

## Qué es este proyecto

Sistema de agendamiento en línea para un consultorio odontológico pequeño.
El objetivo: que un paciente pueda reservar su cita solo, a cualquier hora,
sin llamar ni escribir, y que la doctora vea su agenda organizada en un panel.

## El negocio

- Nombre: Consultorio Odontológico Dra. Ramírez
- Ciudad: Bogotá, Colombia. Zona horaria: America/Bogota (usar SIEMPRE esta zona, en servidor y en cliente).
- Atiende una sola profesional. Solo puede haber una cita a la vez.
- El público llega desde Instagram y desde Google. La mayoría entra por celular.

## Servicios, duración y precio orientativo

| Servicio | Duración | Precio (COP, "desde") |
|---|---|---|
| Valoración (primera vez) | 40 min | $80.000 |
| Control | 20 min | $50.000 |
| Limpieza dental | 45 min | $120.000 |
| Blanqueamiento | 60 min | $350.000 |
| Urgencia | 30 min | $90.000 |

Los precios se muestran como orientativos ("desde"), nunca como cotización final.

## Horario de atención

- Lunes a viernes: 8:00–12:00 y 14:00–18:00
- Sábado: 8:00–13:00
- Domingo: cerrado
- El bloque 12:00–14:00 nunca se agenda (almuerzo).
- Festivos: no se programan en código. La doctora los bloquea desde el panel
  con la función de bloqueos, igual que vacaciones o emergencias.

## Reglas de negocio (no negociables)

1. Los horarios disponibles se calculan según la duración del servicio elegido.
   Una cita nunca se solapa con otra cita ni con un bloqueo.
2. Anticipación mínima para agendar: 2 horas. Máximo: 30 días a futuro.
3. No se puede agendar fuera del horario de atención.
4. Un horario confirmado desaparece de inmediato para los demás.
   Si dos personas intentan el mismo horario a la vez, solo la primera lo consigue:
   la validación final ocurre en el servidor, nunca solo en el navegador.
5. Estados de una cita: pendiente → atendida o cancelada.

## Datos del paciente

Se pide únicamente: nombre completo, celular, correo y motivo general de consulta.

PROHIBIDO pedir o guardar: historia clínica, diagnósticos, tratamientos previos
o cualquier dato de salud sensible. Este sistema agenda citas, no maneja
información clínica.

Antes de confirmar, casilla obligatoria de autorización de tratamiento de
datos personales (Ley 1581 de 2012, Colombia), con enlace a la política.

## Idioma y tono

Todo en español de Colombia. Trato de "usted". Textos cortos y claros.
Mensajes de error amables que digan qué hacer, no códigos técnicos.

## Estilo visual

Limpio y confiable: fondo blanco, azul sobrio como color principal,
tipografía grande y legible. Diseñar primero para celular.
Sin animaciones innecesarias ni librerías de UI pesadas: componentes propios simples.

## Stack

- Next.js (App Router) + TypeScript + Tailwind CSS
- Base de datos: Supabase (Postgres + Auth)
- Publicación: Vercel

## Cómo trabajar en este proyecto

- Antes de dar una tarea por terminada, corre la aplicación y prueba el flujo completo.
- Ninguna llave o secreto va en el código: todo por variables de entorno.
- No cambies reglas de negocio ni alcance sin preguntar primero.
- Si una instrucción es ambigua, pregunta antes de asumir.
