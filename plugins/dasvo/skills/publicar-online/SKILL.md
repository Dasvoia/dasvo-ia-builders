---
name: publicar-online
description: "Lleva el proyecto de la computadora a internet con una URL real que el cliente pueda abrir: revisión previa, subida a GitHub en repositorio privado, conexión con Vercel, variables de entorno configuradas antes del primer despliegue, dominio propio y verificación en un celular real. Incluye el costo mensual verdadero por cliente y la restricción de licencia de Vercel Hobby."
when_to_use: "Úsala cuando el usuario quiera poner el proyecto en línea o hablar de lo que eso cuesta, aunque lo diga corto o mal escrito: \"subirlo a internet\", \"publicar la pagina\", \"publicar la web\", \"quiero que el cliente lo vea\", \"cómo lo pongo online\", \"pasarlo a produccion\", \"deploy\", \"hacer deploy\", \"subir a vercel\", \"subir a github\", \"conectar el dominio\", \"comprar el dominio\", \"quiero que tenga su propio nombre\", \"ya está listo, qué sigue\", \"me falla el deploy\", \"el deploy dio error\", \"cómo subo los cambios nuevos\", \"cómo vuelvo a la versión anterior\", \"cuánto me cuesta tenerlo online\", \"puedo usar el plan gratis con un cliente\", \"se me pausó el proyecto de supabase\"."
---

# Skill: Publicar el Proyecto en Internet

## Tu rol

La persona puede no haber usado git ni GitHub nunca. Tú ejecutas los comandos,
ella solo hace clics en la web y confirma. Reglas:

- UNA instrucción a la vez cuando tenga que salir de la terminal.
- No avances de paso sin su "listo".
- Las llaves nunca pasan por el chat: tú le das los NOMBRES de las variables,
  ella pega los VALORES en el formulario de Vercel.
- Si algo falla, usa la skill `arreglar-errores` en vez de improvisar.

## Paso 1 — Revisión previa (sin esto no se publica)

Verifica tú mismo, marca [OK] o [FALLA] y corrige antes de seguir:

1. El proyecto compila de verdad: ejecuta `npm run build`. Este comando es el
   mismo que corre Vercel; si falla aquí, el despliegue fallará igual. Arregla
   todo antes de continuar.
2. `.env.local` está en `.gitignore`.
3. `.env.local` NUNCA fue subido. Revisa el historial de git. Si alguna vez
   entró, esa llave se considera quemada: se rota en Supabase y se actualiza.
4. No hay llaves, contraseñas ni tokens escritos dentro del código.
5. La revisión de seguridad ya se corrió con la skill `seguridad-web`. Si no,
   córrela ahora: RLS activo, validación en el servidor, datos personales.

Si algo sale [FALLA], se arregla. No se publica con un [FALLA].

## Paso 2 — Subir el código a GitHub

Si el usuario nunca ha usado git, explícalo en una frase: GitHub es donde vive
el código; Vercel lo lee de ahí para publicar el sitio.

1. Comprueba `git --version`. Si no existe, guía la instalación y espera.
2. Configura el nombre y correo si es la primera vez:
   `git config --global user.name "Su Nombre"` y
   `git config --global user.email "su@correo.com"`.
3. En la carpeta del proyecto: `git init` (si aún no es repositorio),
   `git add .`, `git commit -m "Primera version del sistema de citas"`.
4. Antes del commit, muestra `git status` y confirma que `.env.local` NO
   aparece en la lista de archivos a subir. Si aparece, detente y arréglalo.
5. Dile al usuario, una sola instrucción: "entra a github.com, botón New
   repository, ponle el nombre del proyecto, marca **Private**, no marques
   ninguna casilla de README ni .gitignore, y dale Create. Pégame la URL que
   te muestre."
6. Con esa URL: `git remote add origin <url>`, `git branch -M main`,
   `git push -u origin main`. Si pide credenciales, GitHub ya no acepta
   contraseña: se usa un token personal o el inicio de sesión del navegador.

**Por qué privado:** el repositorio contiene la estructura de la base de datos,
las reglas del negocio del cliente y el diseño completo del sistema. Público
significa que cualquiera puede copiarlo y estudiar cómo atacarlo. Además, el
trabajo es del cliente: no es tuyo para regalarlo. Vercel funciona igual con
repositorios privados.

## Paso 3 — Conectar Vercel y desplegar

1. Usuario: "entra a vercel.com y inicia sesión con GitHub".
2. Usuario: "Add New → Project → busca el repositorio → Import".
3. **Antes de dar Deploy**, en Environment Variables agrega las dos variables.
   Dile los nombres exactos y que él pegue los valores:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   Deben quedar marcadas para Production (y Preview si aparece la opción).
4. Deploy. Tarda entre uno y tres minutos.
5. Vercel entrega una URL tipo `nombre-del-proyecto.vercel.app`. Esa ya es una
   página real en internet.

Si el despliegue falla, ve a la sección "Si el despliegue falla" más abajo.

## Paso 4 — El costo real y la licencia (dilo antes de que el cliente pregunte)

Datos verificados a julio de 2026:

| Servicio | Plan gratis | Plan de producción |
|---|---|---|
| Vercel | Hobby: gratis, pero **NO permite uso comercial** | Pro: **20 USD/mes por asiento**, 1 TB de transferencia |
| Supabase | Free: 0 USD, 500 MB de base, 5 GB de egress, máximo 2 proyectos activos, **se pausa tras 1 semana sin actividad** | Pro: **25 USD/mes**, 8 GB de disco, 250 GB de egress, nunca se pausa. Proyectos adicionales desde 10 USD/mes |

**Costo real por cliente en producción: 45 USD/mes** (Vercel Pro 20 + Supabase
Pro 25). Si ya tienes Vercel Pro y Supabase Pro para tu agencia, cada cliente
adicional suma solo el proyecto extra de Supabase, desde 10 USD/mes.

La regla de licencia: el plan Hobby de Vercel es para proyectos personales y
no comerciales. El sitio de un cliente que te paga es uso comercial: va en
Vercel Pro. No es un detalle técnico, es la licencia del servicio, y una cuenta
suspendida deja el sitio del cliente fuera de línea sin aviso.

La pausa de Supabase Free: el proyecto se pausa tras una semana sin actividad.
En un negocio real esto significa que un lunes cualquiera el formulario de
reservas simplemente no responde y nadie se entera hasta que un cliente se
queja. Inaceptable en producción.

Cómo se cubre: si le cobras al negocio una mensualidad de 100 USD, 45 se van en
infraestructura y 55 quedan de margen; si cobras 150, quedan 105. Explícale al
usuario que estos 45 USD son costo fijo del servicio, no ganancia, y que debe
cobrarlos dentro de la mensualidad, nunca poner el sitio de un cliente en los
planes gratuitos "mientras tanto".

## Paso 5 — Dominio propio

Con la URL `.vercel.app` el sistema ya funciona; el dominio propio es
presentación.

Opción A, dominio nuevo (el cliente no tiene web):
1. Comprarlo en Namecheap, GoDaddy, Cloudflare o Porkbun. Costo típico
   10 a 15 USD al año. Que lo compre el cliente con SU cuenta y su tarjeta: el
   dominio debe quedar a su nombre.
2. En Vercel: el proyecto → Settings → Domains → escribe el dominio → Add.
3. Vercel muestra los registros DNS a configurar. Normalmente un registro A
   para el dominio raíz y un CNAME para `www`.
4. Usuario: "entra donde compraste el dominio, busca DNS o Administrar DNS, y
   agrega estos registros tal cual". Dale un registro a la vez.
5. Propagación: suele tardar de 10 minutos a 2 horas, y puede llegar hasta 48
   horas. Vercel emite el certificado HTTPS solo cuando el DNS ya apunta bien.

Opción B, subdominio del dominio que el cliente ya tiene (más rápido y sin
tocar su web actual): usar `citas.sunegocio.com` o `reservas.sunegocio.com`.
Solo se agrega un registro CNAME apuntando al valor que indique Vercel. Su web
actual no se toca ni se cae. Recomienda esta opción cuando el cliente ya tenga
página.

Mientras propaga: usa la URL `.vercel.app` para las pruebas y para enseñárselo
al cliente. Funciona igual. No cambies nada del DNS "porque no aparece": los
cambios repetidos reinician el tiempo de propagación.

## Paso 6 — Verificación después de publicar

No des el trabajo por entregado sin hacer esto, en este orden:

1. Abre la URL en un **celular real**, no solo en el simulador del navegador.
2. Haz una reserva de prueba completa, de principio a fin, como lo haría un
   cliente.
3. Comprueba en Supabase que esa reserva llegó a la tabla, con todos los datos.
4. Revisa la hora guardada: debe coincidir con la que elegiste. Prueba también
   una cita temprano (8:00 a.m.) y otra tarde (8:00 p.m.) para descartar
   desfase de zona horaria.
5. Ábrelo en un navegador distinto y en ventana de incógnito.
6. Verifica que el horario ya reservado deje de aparecer como disponible.
7. Borra las reservas de prueba antes de entregar.

## Si el despliegue falla

Los cinco fallos más comunes:

1. **Build failed por error de tipos.** En local `npm run dev` es tolerante, el
   build no. Corre `npm run build` en tu computadora, arregla y vuelve a subir.
2. **La página truena en la URL pero funciona en local.** Faltan las variables
   de entorno en Vercel. Settings → Environment Variables → agrégalas → y
   **vuelve a desplegar**: agregarlas no reconstruye el sitio solo.
3. **404 en una ruta que sí existe.** Diferencia de mayúsculas en el nombre de
   un archivo o carpeta. El servidor las distingue; Windows y Mac no.
4. **Module not found de un paquete que sí tienes.** Se instaló pero no quedó
   en `package.json`, o el archivo no se subió a git. Revisa `git status` y
   reinstala con `npm install <paquete>` para que quede registrado.
5. **Se publicó la versión vieja.** El commit no se subió (`git push`), o es
   caché del navegador (recarga forzada / incógnito). Revisa en Deployments que
   el último despliegue esté en Ready y no en Error.

Para cualquier otro error, abre Vercel → Deployments → el despliegue fallido →
Build Logs, y trabaja con la skill `arreglar-errores`.

## Publicar cambios después de la primera vez

Cada vez que hagas un cambio: `git add .`, `git commit -m "qué cambiaste"`,
`git push`. Vercel detecta el push y despliega solo en un par de minutos. No
hay que volver a configurar nada.

Regla: corre `npm run build` antes de cada push. Diez segundos de espera evitan
un sitio roto frente al cliente.

## Volver a la versión anterior si un cambio rompe algo

Lo más rápido, y sin tocar código: Vercel → Deployments → busca el último
despliegue que funcionaba → menú de tres puntos → **Promote to Production** (o
Rollback, según la versión del panel). El sitio vuelve a esa versión en
segundos. Tranquiliza al usuario: esto existe justo para esto.

Después, con calma, arregla el código: `git log --oneline` para ver el
historial y `git revert <id>` para deshacer el commit que rompió, creando uno
nuevo. Nunca `git reset --hard` ni `git push --force` con alguien que no
programa.

La checklist imprimible completa y la tabla de costos están en
`${CLAUDE_SKILL_DIR}/references/checklist-despliegue.md`. Léela cuando toque
entregar a un cliente o cuando el usuario pida el detalle de precios.
