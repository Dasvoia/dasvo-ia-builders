# Dasvo IA Builders — 13 skills para Claude Code

Construye, blinda, vende y entrega plataformas de agendamiento a medida para
negocios locales (consultorios, barberías, spas, clínicas estéticas,
veterinarias) usando Claude Code, Next.js, Supabase y Vercel.

No necesitas saber programar. Las skills le dicen a Claude Code qué hacer y en
qué orden; tú solo decides y creas tus cuentas.

---

Biblioteca completa con las guías y las plantillas: **https://dasvo-recursos.vercel.app**

---

## Instalación (30 segundos)

Abre Claude Code y escribe estas dos líneas, una por una:

```
/plugin marketplace add Dasvoia/dasvo-ia-builders
```

```
/plugin install dasvo@dasvo-ia-builders
```

Y luego:

```
/reload-plugins
```

Ya está. Escribe `/` y verás las 13 skills.

> Si `/plugin` no te aparece, tu Claude Code está desactualizado. Actualízalo y
> vuelve a intentar.

---

## Cómo se usan

Escribe `/dasvo:` y sale la lista. También puedes escribir el nombre corto
directo, por ejemplo `/setup-cuentas`.

Y en muchos casos ni siquiera hace falta invocarlas: si escribes "quiero crear
un sistema de citas para un cliente", Claude Code carga sola la skill que toca.

### Fase 1 — Montar

| Skill | Qué hace |
|---|---|
| `/dasvo:setup-cuentas` | Crea y conecta Supabase, GitHub y Vercel, y deja las llaves seguras |
| `/dasvo:sistema-de-citas` | La principal: te entrevista, escribe el CLAUDE.md y construye por etapas |
| `/dasvo:adaptar-a-nicho` | Adapta el sistema a otro negocio. 12 perfiles con sus reglas propias |
| `/dasvo:ahorro-tokens` | Que tu plan de Claude rinda el doble |

### Fase 2 — Blindar

| Skill | Qué hace |
|---|---|
| `/dasvo:diseno-pro` | Que el sistema se vea de agencia: tokens, jerarquía, contraste WCAG AA y textos |
| `/dasvo:seguridad-web` | Revisión obligatoria antes de entregar, publicar o grabar |
| `/dasvo:arreglar-errores` | Protocolo de 6 pasos y 29 errores de este stack catalogados |
| `/dasvo:publicar-online` | GitHub, Vercel, dominio propio y URL real |

### Fase 3 — Vender

| Skill | Qué hace |
|---|---|
| `/dasvo:conseguir-clientes` | Califica el prospecto, clona la demo, escribe el mensaje |
| `/dasvo:cerrar-venta` | Calculadora del dolor, precio, 12 objeciones y la propuesta |
| `/dasvo:entregar-al-cliente` | Manual, capacitación, primeros 30 días y mantenimiento |

### Fase 4 — Escalar

| Skill | Qué hace |
|---|---|
| `/dasvo:crear-skill` | Convierte lo que repites en una skill propia |
| `/dasvo:crear-subagente` | Delega trabajo pesado sin llenar el contexto |

---

## Requisitos

- **Claude Code** instalado, con una cuenta de pago de Claude (Pro, Max, Team o
  Enterprise) o acceso por API. El plan gratuito no lo incluye.
- **Node.js** versión LTS, desde nodejs.org. Si te falta, `/dasvo:setup-cuentas`
  te guía para instalarlo.
- Windows, Mac o Linux.

---

## Por dónde empezar

```
/dasvo:setup-cuentas
```

Te lleva de la mano, un paso a la vez, hasta tener las tres cuentas listas.
Después, `/dasvo:sistema-de-citas` construye el primer sistema.

---

## Actualizar

Cuando salga una versión nueva:

```
/plugin marketplace update dasvo-ia-builders
```

---

## Aviso sobre los números

Los precios de Vercel y Supabase que citan estas skills se verificaron en julio
de 2026. **Verifícalos antes de cotizarle a un cliente**: cambian.

El modelo de precios que se enseña ($500–$1.000 de instalación, $100–$150 de
mensualidad) es un modelo de mercado, no una promesa de ingresos.

Los términos contractuales y tributarios varían por país. Revisa los tuyos con
un contador o abogado local antes de firmar tu primer contrato.
