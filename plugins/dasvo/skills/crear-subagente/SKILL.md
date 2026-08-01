---
name: crear-subagente
description: Crea un subagente de Claude Code y decide si conviene delegarle el trabajo. Entrevista qué debe hacer y qué debe devolver, escribe el archivo con el frontmatter correcto y un system prompt con rol, alcance, prohibiciones y formato de salida, le da solo las herramientas mínimas y lo prueba con un encargo real.
when_to_use: "Úsala cuando el usuario quiera delegar trabajo pesado a un ayudante aparte: \"quiero un subagente\", \"hazme un agente\", \"crear subagent\", \"un agente que revise la seguridad\", \"uno que busque en todo el código\", \"que pruebe la app y me diga qué falla\", \"que escriba los textos del cliente\", \"quiero que otro Claude haga esto\", \"se me llena la conversación cuando busca cosas\", \"gasta mucho contexto revisando archivos\", \"no quiero ver todo el proceso, solo el resultado\". También cuando la skill crear-skill haya decidido que lo pedido es un subagente y no una skill."
argument-hint: "[qué quieres que haga el subagente]"
---

# Crear un subagente

La persona que te habla probablemente no sabe programar. Tú haces el trabajo,
ella solo responde y confirma. Si escribió algo después del comando, úsalo como
respuesta a la pregunta 1.

## Paso 0 — Explícale en tres líneas si le conviene

Dile esto, adaptado a su caso:

1. Un subagente corre en su propia ventana de contexto y a la conversación
   principal solo le devuelve su resultado final: por eso ahorra contexto.
2. Vale la pena cuando el trabajo genera mucha basura intermedia y solo importa
   la conclusión: auditar, buscar en todo el repositorio, probar flujos, revisar
   archivos largos.
3. NO vale la pena cuando necesitas ver el proceso, cuando hay que ir corrigiendo
   sobre la marcha, o cuando es una tarea corta: ahí delegar cuesta más de lo
   que ahorra.

Si el caso cae en el punto 3, dilo y ofrece una skill normal en su lugar
(skill `crear-skill`).

## Paso 1 — Entrevista (un solo mensaje, 4 preguntas numeradas)

1. ¿Qué trabajo debe hacer, de principio a fin?
2. ¿Qué te tiene que devolver exactamente? Descríbeme cómo quieres ver la
   respuesta (lista de problemas, informe, rutas de archivos, textos listos).
3. ¿Necesita leer archivos, ejecutar comandos, buscar en internet, o escribir y
   modificar código?
4. ¿Es trabajo repetitivo y sencillo? Si lo es, le pongo un modelo más barato y
   te cuesta menos.

Resume en 4 líneas y pide confirmación antes de crear el archivo.

## Paso 2 — Elegir dónde vive

- Solo este proyecto: `.claude/agents/<nombre>.md`
- Todos sus proyectos: `~/.claude/agents/<nombre>.md`

El nombre debe ser único en todo el árbol. Si ya existe otro subagente con ese
nombre, cámbialo: cuando se repiten, se carga solo uno de forma impredecible.
Antes de escribir, revisa las dos carpetas para confirmar que el nombre está
libre.

## Paso 3 — Escribir el archivo

Frontmatter entre `---`. Los campos son exactamente estos y ninguno más:

| Campo | Para qué sirve |
|---|---|
| `name` | Identificador del subagente |
| `description` | Cuándo se le delega trabajo a este subagente |
| `tools` | Herramientas permitidas, lista separada por comas |
| `model` | Modelo con el que corre |

El CUERPO del archivo es el system prompt del subagente. Ojo: el subagente
recibe solo ese system prompt más detalles básicos del entorno, no el system
prompt completo de Claude Code. Todo lo que deba saber tiene que estar escrito
ahí. Escríbelo con estas cuatro partes, en este orden:

1. **Rol**: qué es y para quién trabaja, en una frase.
2. **Alcance**: qué revisa o produce, paso a paso, y dónde debe mirar.
3. **Qué NO hacer**: los límites duros (no modificar código, no inventar,
   no salirse del tema, no pedirle cosas al usuario).
4. **Formato exacto del resultado**: la plantilla literal de la respuesta que
   devuelve. Sé estricto: es lo único que llega a la conversación principal.

## Paso 4 — Mínimo privilegio en `tools`

Dale solo las herramientas que necesita para el trabajo del paso 1, y explícale
al usuario en una línea por qué cada una está o no está. Criterio:

- Solo lee y analiza: herramientas de lectura y búsqueda. Sin escritura.
- Prueba o ejecuta cosas: agrega ejecución de comandos.
- Escribe archivos: solo si el usuario dijo explícitamente que debe modificar.
- Redacta textos: no necesita tocar el sistema de archivos si le pasas el
  contexto en el encargo.

Un subagente sin permiso de escritura no puede romper el proyecto. Ese es el
argumento que le das al usuario.

## Paso 5 — Probarlo

Pídele al usuario un encargo real de su proyecto y lánzalo. Revisa dos cosas:
que haya devuelto exactamente el formato definido en el paso 3, y que no se haya
salido de su alcance. Si falla, corrige el system prompt (casi siempre falta
precisión en el formato de salida) y repite.

## Paso 6 — Cerrar

- Archivo creado en: (ruta completa)
- Se le encarga trabajo diciendo: (frase de ejemplo)
- Herramientas que tiene: (lista) y por qué
- Devuelve: (una línea)

## Subagentes ya escritos

Hay cuatro subagentes completos y listos para copiar en
`${CLAUDE_SKILL_DIR}/references/subagentes-listos.md`: revisor de seguridad,
probador de flujos, explorador de código y redactor de textos del cliente.
Léelo cuando el usuario pida uno de esos, o para adaptarlo como base. No lo leas
si el encargo es de otro tipo.
