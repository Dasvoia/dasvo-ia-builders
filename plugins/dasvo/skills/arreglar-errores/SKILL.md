---
name: arreglar-errores
description: "Diagnostica y arregla cualquier fallo de un proyecto Next.js + Supabase + Vercel con un protocolo ordenado: primero pide el reporte completo, clasifica el fallo en una de seis familias, formula una sola hipótesis y hace el cambio mínimo que la comprueba. Evita el bucle de parchar a ciegas."
when_to_use: "Úsala apenas el usuario reporte que algo falla, aunque lo diga mal o corto: \"no funciona\", \"no me sirve\", \"se rompio\", \"se rompió todo\", \"me sale error\", \"me salio un error rojo\", \"no carga\", \"la pagina esta en blanco\", \"no me deja guardar la cita\", \"no arranca\", \"npm run dev no funciona\", \"error de tipos\", \"build failed\", \"falla el deploy\", \"en mi compu si funciona pero en internet no\", \"se ve raro\", \"se desordenó todo\", \"la hora sale corrida\", \"no me guarda nada en la base de datos\", \"ya intenté de todo y sigue igual\", \"llevamos rato con esto\". También cuando tú mismo lleves dos intentos fallidos arreglando algo y necesites reordenar el diagnóstico en vez de seguir probando."
---

# Skill: Arreglar Errores

## Tu rol

La persona probablemente NO sabe programar y está frustrada. Tú diagnosticas,
ella solo copia, pega y confirma. Reglas:

- Nunca digas "prueba esto a ver". Di qué crees que pasa y qué vas a comprobar.
- UN cambio a la vez. Cambiar tres cosas juntas hace imposible saber cuál sirvió.
- Cero jerga sin traducir en la misma frase.
- Prohibido inventar la causa. Si no sabes, dilo y busca evidencia.

## Paso 0 — Exigir el reporte antes de tocar nada

Si el usuario solo dijo "no funciona" o "se rompió", NO empieces a cambiar
archivos. Pide esto, con amabilidad y explicando por qué:

> Para no perder tiempo adivinando, necesito cuatro cosas:
> 1. ¿Qué hiciste justo antes? (el último clic o el último comando)
> 2. ¿Qué esperabas que pasara?
> 3. ¿Qué pasó en realidad?
> 4. Pega el error completo, tal cual, sin resumirlo ni recortarlo.
>
> Con esto suelo encontrarlo al primer intento. Sin esto, probamos a ciegas y
> tardamos el triple.

Dónde está el error, según dónde falle:

- La terminal donde corre `npm run dev`: el texto rojo completo.
- El navegador: clic derecho → Inspeccionar → pestaña Console.
- Vercel: el proyecto → Deployments → el despliegue fallido → Build Logs.
- Supabase: el panel → Logs.

Si el usuario no encuentra el error, pídele una captura de pantalla completa.

## Paso 1 — Clasificar el fallo en una familia

Antes de diagnosticar, di en voz alta a cuál pertenece. Cada familia manda a un
lugar distinto:

| Familia | Señal | Dónde se mira |
|---|---|---|
| 1. No arranca el proyecto | `npm run dev` muere o el puerto no abre | Terminal, `package.json`, versión de Node |
| 2. Compilación o tipos | "Type error", "Module not found", el build falla | El archivo y la línea que nombra el error |
| 3. Carga pero se ve mal | Sin estilos, desordenado, encimado | Navegador, Tailwind, caché |
| 4. La base de datos rechaza | Guarda nada, "new row violates policy", array vacío | Supabase: RLS, tabla, columnas |
| 5. Local sí, publicado no | Funciona en tu compu y falla en la URL | Variables de entorno en Vercel, build logs |
| 6. Sin error visible, resultado incorrecto | Horas corridas, cupos que no cuadran, datos raros | Lógica y zona horaria; no hay error que leer |

Si la familia no está clara, empieza por reproducir (paso 2) y clasifica después.

## Paso 2 — Protocolo de seis pasos

Aplícalo en orden, siempre, sin saltarte ninguno:

1. **Reproducir.** Consigue que el fallo ocurra a voluntad. Si no se puede
   reproducir, no se puede arreglar: anota los pasos exactos que lo provocan.
2. **Aislar.** Reduce a la pieza más pequeña que falla: ¿una página o todas?
   ¿un servicio o todos? ¿un horario o cualquiera? ¿un navegador o todos?
3. **Una hipótesis, escrita.** Di: "creo que falla porque X; si es X, entonces
   Y debería estar mal". Una sola. Si tienes dos, ordénalas por probabilidad y
   prueba la primera.
4. **Cambio mínimo.** Haz solo lo que comprueba la hipótesis. Nada de
   reescribir el archivo entero ni de "ya que estoy, mejoro esto".
5. **Verificar.** Repite los pasos del punto 1. Si el fallo sigue, deshaz el
   cambio antes de probar la siguiente hipótesis. Un arreglo que no arregló no
   se queda en el código.
6. **Registrar.** Al terminar, escribe una línea al usuario: qué era, por qué
   pasaba y qué se cambió. Si el proyecto tiene `CLAUDE.md`, anota ahí la causa
   para no repetirla.

## Regla anti-bucle: tres intentos y paras

Si tres hipótesis distintas no resolvieron el problema, DETENTE. No sigas
parchando: cada parche encima de otro parche crea errores nuevos que se ven
como el original.

Qué haces en su lugar:

1. Dilo claro: "llevamos tres intentos, voy a volver atrás y replantear".
2. Revierte a lo último que funcionaba:
   - Cambios sin guardar en git: `git diff` para ver qué se tocó y
     `git checkout -- <archivo>` para devolver ese archivo. Confirma con el
     usuario archivo por archivo antes de descartar nada.
   - Si ya hay commits: `git log --oneline` para ver la lista y
     `git revert <id>` para deshacer ese commit creando uno nuevo. Nunca uses
     `git reset --hard` con un usuario que no programa: borra trabajo sin aviso.
   - Si no hay git todavía, copia la carpeta del proyecto antes de tocar nada.
3. Vuelve a empezar desde el paso 1 con una pregunta distinta: en vez de
   "¿por qué falla esto?", pregunta "¿estoy seguro de que el problema está
   donde creo?". Comprueba lo que diste por hecho: que la variable existe, que
   el archivo se guardó, que el servidor se reinició, que estás mirando la
   pestaña correcta.

## Los fallos más comunes de este stack

Síntoma → causa habitual. Confirma antes de arreglar, no asumas.

- **"undefined" en una URL de Supabase, o el cliente no conecta.** Variable de
  entorno faltante o mal escrita. Debe llamarse exactamente
  `NEXT_PUBLIC_SUPABASE_URL` y `NEXT_PUBLIC_SUPABASE_ANON_KEY`. Sin el prefijo
  `NEXT_PUBLIC_` el navegador no la ve. Tras editar `.env.local` hay que
  reiniciar `npm run dev`.
- **La consulta devuelve lista vacía o "violates row-level security policy".**
  RLS está bloqueando una operación legítima. Falta la política para ese rol.
  No apagues RLS: escribe la política correcta.
- **Las horas salen corridas.** Desfase de zona horaria: la base guarda en UTC
  y el navegador muestra en la zona local. Define UNA zona (la del negocio),
  guarda siempre igual y convierte solo al mostrar.
- **"Hydration failed" o "Text content did not match".** El servidor y el
  navegador renderizaron cosas distintas, casi siempre fechas, horas o
  `new Date()` calculados en ambos lados. Calcula la fecha en un solo lugar o
  renderízala solo en el cliente.
- **"Module not found: Can't resolve 'x'".** Dependencia no instalada.
  `npm install x` y reiniciar el servidor.
- **El cambio no aparece aunque el código está bien.** Caché del navegador o de
  Next.js. Recarga forzada (Ctrl+Shift+R o Cmd+Shift+R), y si sigue, borra la
  carpeta `.next` y vuelve a arrancar.
- **Funciona en local y falla publicado.** Las variables de entorno no se
  cargaron en el hosting. Se configuran en Vercel → Settings → Environment
  Variables y hay que volver a desplegar: agregarlas no reconstruye solo.

El catálogo completo, con el mensaje literal, qué significa y la solución paso
a paso, está en `${CLAUDE_SKILL_DIR}/references/errores-comunes.md`. Búscalo
ahí por el texto del error antes de improvisar un diagnóstico.

## Cuándo parar y pedir ayuda humana

Para y sugiere ayuda si: el fallo persiste tras revertir y replantear dos
veces; hay riesgo de perder datos de clientes reales; el problema está en el
servicio de un tercero (Supabase o Vercel caídos, un cobro rechazado); o hay
algo legal o de seguridad de por medio (una llave filtrada, datos personales
expuestos).

Prepara tú este resumen para que el usuario lo pegue donde pida ayuda:

```
Qué hace el proyecto: (una línea)
Stack: Next.js App Router + TypeScript + Tailwind + Supabase + Vercel
Qué intentaba hacer:
Qué esperaba que pasara:
Qué pasó:
Error completo:
Qué ya probamos (y qué pasó en cada intento): 1. 2. 3.
Dónde falla: solo local / solo publicado / en ambos
```

Recuérdale al usuario que jamás pegue llaves, contraseñas ni el contenido de
`.env.local` en un foro, un chat o un grupo de soporte.
