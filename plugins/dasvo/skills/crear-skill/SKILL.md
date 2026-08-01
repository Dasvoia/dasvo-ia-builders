---
name: crear-skill
description: Crea una skill nueva de Claude Code bien formada, sin que el usuario tenga que saber el formato. Entrevista corto, decide si de verdad debe ser una skill (o si va al CLAUDE.md o a un subagente), escribe el frontmatter y el description con las frases disparadoras correctas, crea la carpeta en la ruta que corresponde y prueba que se active.
when_to_use: "Úsala cuando el usuario quiera convertir algo que repite en un comando reutilizable: \"quiero una skill para X\", \"hazme una skill\", \"hazme un skill\", \"crear skil\", \"quiero un comando /algo\", \"comando personalizado\", \"siempre le pido lo mismo a Claude\", \"cómo automatizo esto que repito\", \"quiero que Claude haga esto solo\", \"guárdame este proceso\", \"esto lo hago cada semana, no quiero explicarlo otra vez\". También cuando pida corregir, mejorar o revisar una skill que ya existe y no se está activando."
argument-hint: "[para qué quieres la skill]"
---

# Crear una skill

La persona que te habla probablemente no sabe programar. Habla en español
simple, tú haces el trabajo, ella solo responde preguntas y confirma.

Si el usuario escribió algo después del comando, úsalo como respuesta a la
pregunta 1 y no la vuelvas a hacer.

## Paso 1 — Entrevista (un solo mensaje, 5 preguntas numeradas)

Dile que si no sabe alguna, escriba "decide tú" y tú eliges lo razonable.

1. ¿Qué tarea repites y quieres dejar guardada?
2. Cuando la invoques, ¿qué debería pasar exactamente? Dime el resultado final
   que esperas ver.
3. ¿Con qué frases la llamarías tú, con tus palabras? Dame 2 o 3.
4. ¿Quieres que Claude la active solo cuando detecte el tema, o solo tú
   escribiendo `/nombre`?
5. ¿Es para este proyecto nada más, o para todos tus proyectos?

Resume las respuestas en 4 líneas y pide confirmación antes de crear archivos.

## Paso 2 — Decidir si de verdad es una skill

No todo lo que el usuario pide debe ser una skill. Muéstrale esta tabla y di
cuál elegiste y por qué. Si no es skill, haz lo que corresponda y termina ahí.

| Lo que pide | Va en | Por qué |
|---|---|---|
| Un dato fijo del proyecto (horarios, colores, stack, reglas del negocio) | `CLAUDE.md` | Se carga siempre, no hay que invocarlo |
| Un procedimiento con pasos que se repite y se invoca | Skill | Se carga solo cuando hace falta |
| Trabajo largo y sucio que solo debe devolver un resumen (auditar, buscar en todo el repo, probar flujos) | Subagente | Corre en su propia ventana y no ensucia la conversación |
| Una sola instrucción de una línea | Nada | Se pide y ya; una skill para esto es costo sin beneficio |

Si sale "subagente", usa la skill `crear-subagente`.

## Paso 3 — Escribir el `description`

Es lo único que decide si la skill se activa o no. Reglas:

- Primera frase: el caso de uso principal, en presente y concreto. Nada de
  "esta skill sirve para...".
- Después: las frases disparadoras reales que dio el usuario, entre comillas,
  incluyendo variantes cortas y mal escritas (sin tildes, en singular, con
  errores de dedo).
- Di también cuándo NO usarla si hay otra skill parecida que podría chocar.
- `description` + `when_to_use` juntos se cortan a 1.536 caracteres en el
  listado. Cuenta los caracteres y recorta si te pasas: lo importante va
  primero, porque lo que se corta es el final.

Escribe el borrador, muéstraselo al usuario y pregúntale si con esas frases él
la llamaría de verdad.

## Paso 4 — Crear la estructura

El comando `/nombre` sale del NOMBRE DE LA CARPETA, no del campo `name`.
Elige un nombre de carpeta corto, en minúsculas y con guiones.

- Solo este proyecto: `.claude/skills/<nombre>/SKILL.md`
- Todos sus proyectos: `~/.claude/skills/<nombre>/SKILL.md`

Reglas del cuerpo:

- Corto e imperativo, dirigido a Claude. Una vez cargado, el cuerpo se queda en
  contexto en los turnos siguientes: cada línea se paga en todos los turnos.
- Si el material pasa de una pantalla (listas largas, plantillas, ejemplos,
  tablas de referencia), sácalo a `references/` dentro de la misma carpeta y
  desde el cuerpo di cuándo leerlo, por ejemplo:
  `Lee ${CLAUDE_SKILL_DIR}/references/formato-completo.md solo cuando toque escribir el archivo.`
- Si el usuario eligió "solo yo con `/`", agrega `disable-model-invocation: true`.

Los campos del frontmatter, las sustituciones y la plantilla en blanco están en
`${CLAUDE_SKILL_DIR}/references/formato-completo.md`. Léelo antes de escribir el
archivo. No inventes campos que no estén en esa lista.

## Paso 5 — Probar

Propón 3 frases con las que la skill DEBERÍA activarse y 2 con las que NO
debería (temas vecinos que pertenecen a otra skill). Para cada una di si el
`description` la cubre y por qué. Si alguna de las 3 no queda cubierta, o
alguna de las 2 sí se activaría, corrige el `description` y vuelve a probar.

Luego pide al usuario que abra una sesión nueva de Claude Code y escriba
`/<nombre>` para verla en el listado.

## Paso 6 — Cerrar

Termina siempre con estas cuatro líneas:

- Archivo creado en: (ruta completa)
- Se invoca escribiendo: `/<nombre-de-la-carpeta>`
- Se activa sola cuando: (resumen en una línea)
- Para cambiarla: dime "edita la skill <nombre>" y la ajusto
