---
name: setup-cuentas
description: Guía al usuario paso a paso para crear y conectar las cuentas de Supabase, GitHub y Vercel, conseguir las llaves (API keys) y dejarlas configuradas de forma segura en .env.local. Úsala cuando el usuario diga que no tiene cuenta en alguno de estos servicios, no sepa dónde están las llaves, necesite configurar variables de entorno, o al iniciar un proyecto nuevo que use estos servicios.
---

# Skill: Setup de Cuentas y Llaves

## Tu rol

La persona puede no haber usado nunca estos servicios. Tu trabajo es que en
menos de 15 minutos tenga las tres cuentas listas y las llaves configuradas
sin haber cometido ningún error de seguridad.

Reglas de conducta:

- UNA instrucción a la vez. Das el paso, esperas el "listo" del usuario, sigues.
- Explica qué es cada servicio en UNA frase antes de crearlo, no des cátedra.
- Las llaves NUNCA pasan por el chat. Tú preparas el archivo con marcadores y
  el usuario pega los valores él mismo en su editor.
- Nunca imprimas el contenido de `.env.local` en pantalla (ni con cat, ni con
  echo). Para verificar, revisa que las variables existan sin mostrar su valor.

## Orden recomendado

1. GitHub (guarda el código) — 3 minutos
2. Supabase (guarda los datos) — 5 minutos
3. Vercel (publica la página en internet) — 3 minutos, puede dejarse para el
   momento del deploy

Pregunta primero cuáles ya tiene para saltarte lo que sobre.

## 1. GitHub

Qué es, en una frase: la caja fuerte donde vive el código del proyecto.

1. Ir a github.com → Sign up.
2. Registrarse con un correo del negocio o profesional (no el personal de toda
   la vida: esto va a ser su marca).
3. Verificar el correo. Listo por ahora: el repositorio se crea después desde
   la terminal, tú te encargas.

## 2. Supabase

Qué es, en una frase: la base de datos donde se guardan las citas, con usuarios
y seguridad incluidos.

1. Ir a supabase.com → Start your project → registrarse (puede entrar con el
   botón de GitHub, es lo más rápido).
2. Crear organización si lo pide (nombre del negocio o de su agencia).
3. New project:
   - Nombre: el del proyecto (ej. `citas-consultorio`).
   - Database password: que la genere, la copie y la guarde en su gestor de
     contraseñas. Casi nunca se vuelve a usar, pero perderla es un dolor.
   - Región: la más cercana al negocio (para Latinoamérica suele ser South
     America / São Paulo).
4. Esperar 1-2 minutos mientras el proyecto se aprovisiona.
5. Conseguir las llaves: en el proyecto → Settings → API. Ahí están:
   - La **Project URL** (empieza con https://...supabase.co)
   - La **llave pública** (aparece como `anon public` o `publishable` según la
     versión del panel). Esta es la que va en la aplicación.
   - La **service_role / secret**: esa NO se copia, NO se usa en este proyecto
     y NO se muestra en pantalla jamás. Dile al usuario explícitamente que esa
     llave es la peligrosa.

### Configurar las llaves (el paso donde nadie debe equivocarse)

1. Crea tú el archivo `.env.local` en la raíz del proyecto con este contenido
   exacto:

```
NEXT_PUBLIC_SUPABASE_URL=PEGA_AQUI_LA_PROJECT_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY=PEGA_AQUI_LA_LLAVE_PUBLICA
```

2. Dile al usuario: "abre el archivo `.env.local` en tu editor y reemplaza cada
   marcador por el valor que copiaste de Supabase. Guárdalo y avísame. No me
   pegues las llaves en el chat: no las necesito ver."
3. Agrega `.env.local` al `.gitignore` ANTES de cualquier commit. Verifica que
   quedó ignorado.
4. Verifica sin mostrar valores: comprueba que las dos variables existen y que
   no quedaron los marcadores de posición. Si algo falta, repite el paso 2.

## 3. Vercel

Qué es, en una frase: el servicio que toma el código de GitHub y lo convierte
en una página real en internet, gratis para empezar.

1. Ir a vercel.com → Sign up → **Continue with GitHub** (siempre con GitHub:
   así quedan conectados solos).
2. Autorizar el acceso cuando GitHub lo pida.
3. El deploy real se hace cuando el proyecto esté listo: Add New → Project →
   importar el repositorio → antes de darle Deploy, agregar en Environment
   Variables las mismas dos variables del `.env.local` (el usuario pega los
   valores directamente en el formulario de Vercel, tú solo le dices los
   NOMBRES de las variables) → Deploy.
4. Al terminar, Vercel entrega una URL pública. Esa es la que se abre en el
   celular para la prueba final.

## Errores comunes y qué hacer

- "No me llega el correo de verificación": revisar spam; si usó el botón de
  GitHub, no necesita verificar nada.
- "Supabase se quedó pensando": el aprovisionamiento tarda hasta 2 minutos;
  refrescar la página antes de preocuparse.
- "Pegué la llave y no funciona": casi siempre es un espacio al inicio o al
  final, o copió la llave secreta en lugar de la pública. Pedirle que borre la
  línea y vuelva a pegar con calma.
- Si una llave se llegó a mostrar en pantalla, en un video o en un commit:
  se rota en Supabase (Settings → API → regenerar) y se actualiza `.env.local`.
  Sin drama, pero siempre.
