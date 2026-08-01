# Catálogo de errores comunes — Next.js + TypeScript + Tailwind + Supabase + Vercel

Cómo usar este archivo: busca el mensaje del error por su texto literal. Cuando
un mismo mensaje puede tener varias causas, están ordenadas de más probable a
menos probable. Comprueba en ese orden y no saltes a la última sin descartar la
primera.

Nota general: casi cualquier cambio en `.env.local`, en `next.config.js` o una
instalación nueva de dependencias exige detener el servidor (Ctrl+C) y volver a
arrancarlo con `npm run dev`. Muchos "sigue igual" son eso.

---

## A. No arranca el proyecto

### 1. `command not found: npm` / `npm no se reconoce como un comando`

Qué significa: la computadora no tiene Node.js instalado, o la terminal no lo
encuentra.

Causas, por probabilidad:
1. Node.js nunca se instaló.
2. Se instaló pero la terminal estaba abierta desde antes y no ve el cambio.

Solución:
1. Cierra la terminal, abre una nueva y ejecuta `node -v`.
2. Si sigue sin aparecer, descarga la versión LTS desde nodejs.org, instálala
   con las opciones por defecto y reinicia la terminal.
3. Verifica de nuevo con `node -v` y `npm -v`. Necesitas Node 20.9 o superior (LTS actual); 18.18 solo si fijas Next.js 15.

### 2. `Error: Cannot find module 'next'` al arrancar

Qué significa: falta la carpeta de dependencias del proyecto.

Causas:
1. Nunca se corrió `npm install` en esta carpeta.
2. Se está ejecutando el comando desde la carpeta equivocada.
3. La instalación se cortó a la mitad.

Solución:
1. Confirma que estás en la carpeta del proyecto: debe existir `package.json`.
2. Ejecuta `npm install` y espera a que termine sin errores.
3. Si falla a la mitad, borra `node_modules` y `package-lock.json`, y repite
   `npm install`.

### 3. `Error: listen EADDRINUSE: address already in use :::3000`

Qué significa: el puerto 3000 ya está ocupado; casi siempre por otra ventana de
terminal con el mismo proyecto corriendo.

Solución:
1. Busca otra terminal abierta con `npm run dev` y ciérrala con Ctrl+C.
2. Si no la encuentras, arranca en otro puerto: `npm run dev -- -p 3001` y abre
   `http://localhost:3001`.

### 4. `You are using Node.js 16.x. For Next.js, Node.js version >= 18.18.0 is required`

Qué significa: la versión de Node es demasiado vieja.

Solución: instala la versión LTS actual desde nodejs.org, cierra y reabre la
terminal, comprueba con `node -v` y vuelve a ejecutar `npm install`.

### 5. La terminal se queda en `Starting...` y nunca abre la página

Causas:
1. Sí arrancó, pero el usuario está abriendo la URL equivocada. Debe ser
   `http://localhost:3000`, no `https://` ni el nombre del proyecto.
2. Un archivo tiene un error de sintaxis y el compilador está atascado.
3. La primera compilación de un proyecto grande tarda; espera 60 segundos.

Solución: lee la terminal completa buscando la primera línea roja. La primera
importa, las siguientes suelen ser consecuencia.

---

## B. Compilación y tipos

### 6. `Module not found: Can't resolve 'date-fns'` (o cualquier otro paquete)

Qué significa: el código usa una librería que no está instalada.

Causas:
1. Falta instalarla: `npm install date-fns`.
2. El nombre está mal escrito en el `import`.
3. Es un archivo propio del proyecto y la ruta está mal (mayúsculas incluidas:
   en Vercel `Boton.tsx` y `boton.tsx` son archivos distintos, aunque en
   Windows o Mac funcionen igual).

Solución: instala, corrige el nombre o corrige la ruta, y reinicia el servidor.

### 7. `Type error: Property 'nombre' does not exist on type '...'`

Qué significa: le pides a un objeto un campo que TypeScript no sabe que existe.

Causas:
1. El tipo o la interfaz no incluye ese campo; hay que agregarlo.
2. El campo en la base de datos se llama distinto (`nombre_cliente` vs
   `nombre`).
3. Los tipos generados desde Supabase están desactualizados tras cambiar la
   tabla.

Solución: compara el nombre exacto de la columna en Supabase con el del tipo en
el código. Si cambiaste la tabla, regenera los tipos.

### 8. `Type 'string | null' is not assignable to type 'string'`

Qué significa: ese valor puede venir vacío y el código asume que siempre trae
algo. Es un aviso legítimo, no un capricho.

Solución: decide qué pasa cuando viene vacío y escríbelo. Por ejemplo un valor
por defecto (`dato ?? "Sin nombre"`) o una comprobación previa. No lo silencies
con `as string`: eso esconde el fallo hasta que rompa frente al cliente.

### 9. `'x' is declared but its value is never read`

Qué significa: hay una variable o un import sin usar. Molesta pero rara vez
rompe.

Solución: bórralo. Si iba a usarse, úsalo.

### 10. `Error: You're importing a component that needs useState. It only works in a Client Component, but none of its parents are marked with "use client"`

Qué significa: en el App Router los componentes son de servidor por defecto y
ese no puede usar estado ni eventos de clic.

Solución: agrega `"use client"` como PRIMERA línea del archivo del componente
interactivo (formularios, calendarios, botones con `onClick`). Deja como
componentes de servidor los que solo muestran datos.

### 11. `ReferenceError: window is not defined` o `document is not defined`

Qué significa: el código intentó usar el navegador mientras corría en el
servidor, donde no existe ventana ni documento.

Solución: mueve ese código dentro de un `useEffect` (que solo corre en el
navegador) o marca el componente con `"use client"`.

---

## C. Carga pero se ve mal

### 12. La página aparece sin estilos, todo en blanco y negro apilado

Causas:
1. Tailwind no está procesando los archivos: revisa que las rutas de `content`
   en la configuración de Tailwind incluyan las carpetas donde están tus
   componentes.
2. Falta importar el CSS global en el layout raíz.
3. El servidor no se reinició tras cambiar la configuración.

Solución: revisa en ese orden y reinicia `npm run dev`.

### 13. Cambié una clase de Tailwind y no pasa nada

Causas:
1. El nombre de la clase se está construyendo con texto dinámico. Tailwind solo
   detecta clases escritas completas en el código; algo como
   `` `text-${color}-500` `` no funciona. Escribe las clases completas y elige
   entre ellas.
2. Otra clase más específica la está pisando.
3. Caché del navegador: recarga forzada con Ctrl+Shift+R (Cmd+Shift+R en Mac).

### 14. En el celular se ve encimado o se sale de la pantalla

Causas:
1. Anchos fijos en píxeles en vez de anchos flexibles.
2. Falta la variante responsive: en Tailwind se diseña primero para móvil y se
   agregan tamaños mayores con `md:` y `lg:`.
3. Una tabla o un texto largo sin corte fuerza el ancho.

Solución: prueba siempre en la vista de móvil del navegador (Inspeccionar →
icono de celular) antes de darlo por bueno.

### 15. `Error: Hydration failed because the initial UI does not match what was rendered on the server`

Qué significa: el servidor pintó una cosa y el navegador pintó otra distinta.

Causas, por probabilidad:
1. Fechas y horas: `new Date()`, `toLocaleString()` o "hoy" calculados en ambos
   lados con zonas horarias distintas.
2. Valores aleatorios (`Math.random()`) o IDs generados al vuelo.
3. Lectura de `localStorage` o del tamaño de la ventana durante el primer
   render.
4. HTML inválido, como una etiqueta de bloque dentro de un párrafo.

Solución: fija la zona horaria del negocio y formatea las fechas siempre igual;
o mueve ese cálculo a un `useEffect` para que ocurra solo en el navegador.

---

## D. La base de datos rechaza la operación

### 16. `new row violates row-level security policy for table "citas"`

Qué significa: RLS está activo y no hay una política que permita esa inserción
a quien la está haciendo.

Causas:
1. Falta la política de INSERT para el público (cualquiera debe poder crear una
   cita desde el formulario).
2. La política existe pero exige una condición que el formulario no cumple.
3. Se está usando la llave equivocada.

Solución: crea la política de INSERT para el rol público en la tabla de citas,
y deja lectura, actualización y borrado solo para el usuario autenticado.
NUNCA apagues RLS para salir del paso: eso deja la tabla abierta a internet.

### 17. La consulta no da error pero devuelve una lista vacía, y en el panel de Supabase sí hay filas

Causas, por probabilidad:
1. Falta la política de SELECT para ese rol. Sin política de lectura, RLS
   devuelve cero filas sin considerarlo un error.
2. Un filtro de la consulta no coincide (fecha, estado, mayúsculas).
3. Estás consultando otro proyecto de Supabase (URL de otro entorno).

### 18. `relation "public.citas" does not exist`

Qué significa: la tabla no existe con ese nombre en ese proyecto.

Causas:
1. La migración o el SQL de creación nunca se ejecutó.
2. El nombre está en singular/plural distinto, o con mayúsculas.
3. Estás apuntando a otro proyecto de Supabase.

### 19. `duplicate key value violates unique constraint`

Qué significa: se intentó guardar algo que ya existe en una columna que exige
valores únicos.

En un sistema de citas suele ser lo correcto: dos personas pidieron el mismo
horario. Solución: captura ese error específico y muestra al cliente un mensaje
amable ("ese horario acaba de ocuparse, elige otro") y recarga la lista de
horarios disponibles. No lo trates como una falla del sistema.

### 20. `Invalid API key` o `JWT expired`

Causas:
1. La llave pegada en `.env.local` está incompleta o tiene un espacio al inicio
   o al final.
2. Se pegó la llave de otro proyecto.
3. La llave se rotó en Supabase y no se actualizó en el proyecto ni en Vercel.

Solución: vuelve a copiar la llave pública desde Supabase → Settings → API,
pégala limpia y reinicia el servidor. Nunca la muestres en pantalla ni en el
chat.

### 21. `Failed to fetch` o `TypeError: fetch failed` al hablar con Supabase

Causas, por probabilidad:
1. La URL del proyecto está mal o quedó como `undefined` (variable de entorno
   ausente).
2. No hay conexión a internet.
3. El proyecto de Supabase está pausado (plan Free se pausa tras una semana sin
   actividad). Entra al panel y reactívalo.
4. Caída puntual del servicio: revisa el estado de Supabase.

---

## E. Local sí, publicado no

### 22. En la URL de Vercel la página truena, y en local funciona perfecto

Causa casi segura: las variables de entorno no existen en Vercel. `.env.local`
nunca se sube (y está bien que no se suba).

Solución:
1. Vercel → el proyecto → Settings → Environment Variables.
2. Agrega `NEXT_PUBLIC_SUPABASE_URL` y `NEXT_PUBLIC_SUPABASE_ANON_KEY` con los
   mismos valores del `.env.local`, marcadas para Production.
3. Vuelve a desplegar: Deployments → el último → Redeploy. Agregar variables
   NO reconstruye el sitio por sí solo.

### 23. `Build failed` en Vercel con un error de tipos que en local no salía

Qué significa: en local `npm run dev` es tolerante; el build de producción no.

Solución: corre `npm run build` en tu computadora ANTES de publicar. Ese
comando reproduce exactamente lo que hace Vercel. Arregla lo que salga y vuelve
a subir.

### 24. Se publicó, pero la URL muestra la versión vieja

Causas, por probabilidad:
1. Caché del navegador. Recarga forzada o abre en ventana de incógnito.
2. El commit no se subió: `git status` y `git push`.
3. El despliegue falló y Vercel mantiene el anterior en línea. Revisa
   Deployments: el último debe estar en Ready, no en Error.

### 25. `404: NOT_FOUND` en una ruta que existe en local

Causas:
1. Diferencia de mayúsculas en el nombre de la carpeta o el archivo. El
   servidor de Vercel distingue mayúsculas; Windows y Mac normalmente no.
2. El archivo no se subió a git (revisa que no esté ignorado por error).

---

## F. Sin error visible, resultado incorrecto

### 26. La cita se guarda con una hora distinta a la que eligió el cliente

Causa: desfase de zona horaria. La base guarda en UTC y en algún punto se
convierte dos veces, o no se convierte.

Solución: define la zona horaria del negocio en un solo lugar del proyecto,
guarda siempre en el mismo formato y convierte únicamente al mostrar. Prueba
con una cita a las 8:00 a.m. y otra a las 11:00 p.m.: si el día cambia, el
error está en la conversión.

### 27. Aparecen horarios disponibles que ya estaban ocupados

Causas, por probabilidad:
1. El cálculo de disponibilidad no descuenta la duración del servicio, solo la
   hora de inicio.
2. No se están considerando los bloqueos ni los días no laborables.
3. La lista se cargó una vez y no se refresca al cambiar de día.

### 28. El formulario dice "cita creada" pero en la base no hay nada

Causas, por probabilidad:
1. Se ignoró el error que devuelve Supabase: el código muestra el mensaje de
   éxito sin revisar si la operación falló. Revisa siempre el error de la
   respuesta antes de dar por buena la operación.
2. RLS bloqueó la inserción (ver punto 16).
3. Se está escribiendo en otro proyecto o en otra tabla.

### 29. Los correos o mensajes de confirmación no llegan

Causas, por probabilidad:
1. Cayeron en spam.
2. El proveedor de envío no está configurado con un dominio verificado.
3. El envío falla en silencio porque el error no se está revisando.

---

## Comandos de rescate

- Ver qué archivos cambiaste: `git status` y `git diff`
- Deshacer los cambios de un archivo: `git checkout -- ruta/al/archivo`
- Ver el historial: `git log --oneline`
- Deshacer un commit sin borrar historial: `git revert <id>`
- Limpiar caché de Next.js: borra la carpeta `.next` y arranca de nuevo
- Reinstalar dependencias: borra `node_modules`, ejecuta `npm install`
- Probar el build real: `npm run build`

Nunca uses `git reset --hard` ni `git push --force` con un usuario que no
programa: ambos borran trabajo sin posibilidad de recuperarlo fácil.
