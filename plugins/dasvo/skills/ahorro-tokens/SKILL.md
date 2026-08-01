---
name: ahorro-tokens
description: Hace que el trabajo con Claude Code gaste menos tokens y avance más rápido. Úsala cuando el usuario pregunte cómo gastar menos, diga que se le acaban los límites o créditos, la sesión esté lenta o muy cargada, o al arrancar un proyecto largo para establecer buenos hábitos desde el inicio.
---

# Skill: Ahorro de Tokens (trabajar barato y rápido)

## La idea central

Los tokens no se gastan escribiendo: se gastan REPITIENDO. Contexto que se
vuelve a explicar, errores que se corrigen a ciegas cinco veces, archivos
enteros pegados en el chat. Esta skill elimina las tres fugas.

Cuando el usuario la invoque, primero diagnostica: pregunta en qué está
trabajando y qué siente que gasta de más, y luego aplica y explica las reglas
que le apliquen. Si estás iniciando un proyecto, establece los hábitos desde
el primer mensaje.

## Regla 1 — El CLAUDE.md es contexto que se paga una sola vez

Todo lo que esté escrito en el CLAUDE.md del proyecto (reglas de negocio,
horarios, estilo, stack) no hay que volver a explicarlo nunca. Si el usuario
se descubre repitiendo la misma instrucción por segunda vez, la respuesta
correcta es: "eso va al CLAUDE.md". Agrégalo tú y confírmalo.

## Regla 2 — Etapas pequeñas y verificadas

El gasto más grande son los retrabajos. Un mega-pedido de diez cosas que sale
mal a la mitad cuesta más que diez pedidos pequeños que salen bien.

- Un cambio por mensaje, o un grupo pequeño de cambios relacionados.
- Verificar que funciona antes de pedir lo siguiente.
- Para funciones grandes: pedir primero "hazme el plan, no toques código
  todavía", revisar el plan (barato), y solo entonces ejecutar (caro).

## Regla 3 — Especificidad quirúrgica

"Mejora el diseño" es una lotería carísima. "En /agendar, el botón de
confirmar: hazlo azul, más grande y con el texto 'Confirmar mi cita'" sale
bien a la primera.

Fórmula: DÓNDE (archivo o pantalla) + QUÉ (el cambio exacto) + CÓMO SE VE EL
ÉXITO (qué debería pasar).

## Regla 4 — Los errores se reportan con la plantilla, siempre

"No funciona, arréglalo" cuesta cinco intentos. Esto cuesta uno:

```
Hice: [la acción exacta]
Esperaba: [lo que debía pasar]
Pasó: [lo que pasó]
Error completo: [pegado tal cual de la consola o pantalla]
```

Enseña esta plantilla al usuario la primera vez que reporte un error sin ella.

## Regla 5 — No pegar archivos: pedir que se lean

Pegar un archivo entero en el chat lo mete al contexto dos veces (el pegado y
la lectura). Lo correcto: "lee el archivo X y dime/cambia Y". Claude Code lee
los archivos directamente del proyecto.

Lo mismo con errores largos: pegar solo el bloque del error, no 200 líneas de
log alrededor.

## Regla 6 — Higiene de la sesión

- Al cambiar de tema por completo (del build a redactar un correo, por
  ejemplo): sesión nueva o `/clear`. Arrastrar contexto viejo cobra en cada
  mensaje.
- En sesiones largas del mismo tema: `/compact` cuando la conversación pese,
  idealmente al cerrar una etapa completa (no a mitad de un problema).
- No pedir explicaciones largas por defecto. "Hazlo" es más barato que
  "hazlo y explícame cada línea". Las explicaciones se piden cuando de verdad
  se quieren.

## Regla 7 — Aprovechar lo ya construido

Antes de construir algo desde cero, preguntar: "¿esto ya existe en el
proyecto en otra forma?". Reusar el componente de la lista de citas para la
lista de bloqueos cuesta una fracción de crear uno nuevo. Como constructor,
haz tú esta verificación por defecto.

## Señales de que se está gastando de más (autodiagnóstico)

- El mismo error lleva 3+ intentos → parar, aplicar Regla 4 con el error real.
- Se está explicando el negocio otra vez → Regla 1, al CLAUDE.md.
- La respuesta tarda mucho y la sesión "se siente pesada" → Regla 6.
- Un pedido gigante salió a medias → Regla 2, trocearlo y avanzar por partes.
