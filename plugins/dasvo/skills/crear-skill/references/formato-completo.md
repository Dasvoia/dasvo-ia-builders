# Formato completo de una skill

Referencia. Léela cuando vayas a escribir el archivo, no antes.

## Dónde se instala

| Alcance | Ruta |
|---|---|
| Personal (todos los proyectos del usuario) | `~/.claude/skills/<nombre>/SKILL.md` |
| De proyecto (solo ese repositorio) | `.claude/skills/<nombre>/SKILL.md` |

Siempre es una CARPETA con un archivo `SKILL.md` adentro. Los archivos de apoyo
van en esa misma carpeta, normalmente en `references/`.

## Cómo se llama el comando

- El comando `/<nombre>` sale del NOMBRE DE LA CARPETA.
- En skills personales y de proyecto, el campo `name` del frontmatter es solo la
  etiqueta que se muestra en el listado: no cambia el comando.
- En skills de plugin, `name` sí cambia el último segmento del comando.
- Nombre de carpeta: minúsculas, guiones, sin espacios ni tildes.

## Campos del frontmatter

Van entre `---` al principio del archivo. TODOS son opcionales; se recomienda
`description`. No existen otros campos: no inventes ninguno.

| Campo | Para qué sirve |
|---|---|
| `name` | Etiqueta que se muestra en el listado de skills |
| `description` | Qué hace y cuándo usarla; es lo que decide si la skill se activa |
| `when_to_use` | Condiciones y frases de disparo, complemento del `description` |
| `argument-hint` | Pista de los argumentos que se muestra al escribir el comando |
| `arguments` | Definición de los argumentos que acepta la skill |
| `disable-model-invocation` | En `true`, Claude no la activa solo; solo el usuario con `/` |
| `user-invocable` | En `false`, deja de aparecer como comando `/` para el usuario |
| `allowed-tools` | Herramientas permitidas sin preguntar durante el turno que la invoca |
| `disallowed-tools` | Herramientas bloqueadas para esta skill |
| `model` | Modelo con el que se ejecuta la skill |
| `effort` | Nivel de esfuerzo de razonamiento con el que se ejecuta |
| `context` | Con valor `fork`, la skill corre en un subagente aparte |
| `agent` | Subagente encargado de ejecutar la skill |
| `background` | Ejecuta la skill en segundo plano |
| `hooks` | Hooks asociados a la skill |
| `paths` | Rutas asociadas a la skill |
| `shell` | Shell usado para ejecutar comandos de la skill |

Notas de uso:

- `description` y `when_to_use` se truncan JUNTOS a 1.536 caracteres en el
  listado de skills. El caso de uso principal va primero, porque lo que se corta
  es el final.
- Si omites `description`, se usa el primer párrafo del contenido del archivo.
- `allowed-tools` acepta lista separada por espacios o por comas. El permiso
  aplica solo durante el turno en que se invoca la skill.

## Sustituciones disponibles

Funcionan en el cuerpo del `SKILL.md` y en las reglas Bash de `allowed-tools`:

| Sustitución | Qué contiene |
|---|---|
| `${CLAUDE_SKILL_DIR}` | Carpeta de la skill (para leer sus archivos de apoyo) |
| `${CLAUDE_PROJECT_DIR}` | Raíz del proyecto |
| `$ARGUMENTS` | Todo lo que el usuario escribió después del comando |
| `$0`, `$1`, `$2`, ... | Argumentos por posición |

Los argumentos indexados usan comillas estilo shell.

## Divulgación progresiva

El cuerpo del `SKILL.md` permanece en contexto en los turnos siguientes una vez
cargado. Cada línea es un costo que se repite. Por eso:

- Cuerpo: corto, imperativo, solo el procedimiento.
- Material largo (plantillas, listas de campos, ejemplos, checklists extensos):
  en `references/` y se lee solo cuando hace falta.

## Plantilla en blanco

```markdown
---
name: nombre-visible
description: Qué hace, empezando por el caso de uso principal. Úsala cuando el usuario diga "frase 1", "frase 2", "frase 3", incluyendo variantes cortas y mal escritas.
when_to_use: "Situaciones concretas en las que aplica y cuándo NO usarla porque le toca a otra skill."
argument-hint: "[qué se espera como argumento]"
---

# Título corto

## Cuándo actúas
Una o dos líneas.

## Paso 1 — ...
Instrucciones imperativas dirigidas a Claude.

## Paso 2 — ...
...

## Cierre
Qué le confirmas al usuario al terminar.
```

## Tres `description` malos y su versión corregida

**Malo 1 (habla de sí mismo, no del caso de uso)**

> Esta skill es una herramienta muy útil y completa que sirve para ayudarte con
> temas de reservas.

**Corregido**

> Crea y ajusta el sistema de reservas de un negocio local en Next.js y
> Supabase. Úsala cuando el usuario diga "quiero una agenda en línea", "sistema
> de citas", "que mis clientes reserven solos", "reservas", "agendamiento".

---

**Malo 2 (vago, sin frases disparadoras: nunca se activa)**

> Ayuda con la base de datos.

**Corregido**

> Diseña y corrige tablas, relaciones y políticas RLS en Supabase. Úsala cuando
> el usuario diga "crear la tabla de citas", "no me deja guardar", "error de
> permisos en Supabase", "RLS", "la consulta no devuelve nada", "base de datos".

---

**Malo 3 (invade el territorio de otras skills: se activa siempre)**

> Úsala siempre que el usuario hable de un proyecto, de código, de clientes o de
> cualquier cosa relacionada con el negocio.

**Corregido**

> Revisa la seguridad de un proyecto antes de entregarlo o publicarlo: llaves
> expuestas, RLS y validación en el servidor. Úsala cuando el usuario diga
> "voy a publicar", "entregar al cliente", "revisa la seguridad", "api key",
> "es seguro esto". NO la uses para construir funciones nuevas ni para
> diseñar la base de datos.
