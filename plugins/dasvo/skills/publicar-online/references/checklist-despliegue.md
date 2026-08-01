# Checklist de despliegue — imprimible

Proyecto: ______________________  Cliente: ______________________
Fecha: ____________  Responsable: ______________________

Marca cada casilla solo cuando lo hayas comprobado tú mismo. Una casilla sin
comprobar es un problema que aparece frente al cliente.

---

## PARTE 1 — Antes de publicar

### Seguridad

- [ ] La revisión completa de la skill `seguridad-web` se corrió y salió LISTO
- [ ] `.env.local` está listado en `.gitignore`
- [ ] `.env.local` nunca fue subido a git (revisado en el historial)
- [ ] Ninguna llave, contraseña o token escrito dentro del código
- [ ] La llave `service_role` / secreta de Supabase no aparece en el proyecto
- [ ] RLS activo en todas las tablas
- [ ] Política de citas: crear público, leer/editar/borrar solo autenticado
- [ ] Prueba real: sin sesión iniciada NO se pueden leer las citas
- [ ] Casilla de autorización de tratamiento de datos antes de confirmar la cita
- [ ] Política de privacidad publicada y enlazada

### Técnico

- [ ] `npm run build` termina sin errores
- [ ] No quedan datos de prueba ni textos de relleno visibles
- [ ] Los mensajes de error hacia el cliente final son amables y sin jerga
- [ ] La zona horaria del negocio está definida en un solo lugar
- [ ] Se probó en móvil (vista responsive) y no se sale de pantalla
- [ ] Los datos de contacto y el nombre del negocio están correctos
- [ ] Título de la página y favicon puestos (es lo primero que ve el cliente)

### Cuentas y plan

- [ ] Cuenta de GitHub creada y con sesión iniciada
- [ ] Repositorio creado en **privado**
- [ ] Cuenta de Vercel conectada con GitHub
- [ ] Decidido el plan: Hobby solo si es práctica personal; **Pro si el sitio es
      de un cliente que paga**
- [ ] Decidido el plan de Supabase: **Pro para producción** (Free se pausa)
- [ ] El costo mensual está incluido en lo que se le cobra al cliente

---

## PARTE 2 — Despliegue

- [ ] `git status` revisado: `.env.local` NO aparece entre los archivos a subir
- [ ] `git add .` / `git commit` / `git push` completados sin errores
- [ ] El repositorio se ve en GitHub con todos los archivos
- [ ] Proyecto importado en Vercel desde el repositorio
- [ ] Variables de entorno cargadas EN VERCEL **antes** del primer Deploy:
  - [ ] `NEXT_PUBLIC_SUPABASE_URL`
  - [ ] `NEXT_PUBLIC_SUPABASE_ANON_KEY`
  - [ ] Ambas marcadas para Production
- [ ] Deploy ejecutado y terminado en estado **Ready**
- [ ] La URL `.vercel.app` abre correctamente
- [ ] URL anotada: ______________________________________

### Dominio (si aplica)

- [ ] Dominio comprado a nombre del **cliente**, con su cuenta y su tarjeta
- [ ] Dominio agregado en Vercel → Settings → Domains
- [ ] Registros DNS creados tal como los indicó Vercel
  - [ ] Registro A del dominio raíz
  - [ ] CNAME de `www` (o CNAME del subdominio si se usó la opción B)
- [ ] Esperada la propagación (10 min a 2 h típico, hasta 48 h)
- [ ] Certificado HTTPS emitido: el candado aparece en el navegador
- [ ] Dominio anotado: ______________________________________

---

## PARTE 3 — Después de publicar

- [ ] La URL abre en un **celular real** (no solo en el simulador)
- [ ] Reserva de prueba completa hecha de principio a fin desde el celular
- [ ] La reserva aparece en Supabase con todos los datos correctos
- [ ] La hora guardada coincide con la elegida (probar 8:00 a.m. y 8:00 p.m.)
- [ ] El horario ya reservado deja de ofrecerse como disponible
- [ ] Probado en un navegador distinto y en ventana de incógnito
- [ ] Probado con la red de datos del celular, no solo con el wifi de la casa
- [ ] Las confirmaciones (correo o mensaje) llegan y no caen en spam
- [ ] Reservas de prueba borradas de la base de datos
- [ ] El cliente abrió la URL y confirmó que la ve bien

### Entrega al cliente

- [ ] URL final entregada por escrito
- [ ] Explicado cómo entra a ver sus citas
- [ ] Explicado qué está incluido en la mensualidad y qué no
- [ ] Acordado a quién escribe si algo falla y en qué horario
- [ ] Acordado quién es dueño de las cuentas. Modelo A, el predeterminado:
      dominio del cliente; Vercel y Supabase de la agencia mientras dure el
      servicio, con las tres cláusulas escritas (copia de datos en 10 días
      hábiles, respaldo automático, procedimiento de salida). Modelo B, para
      Todo Incluido, sector salud, o si el cliente pregunta por la propiedad
      de los datos: todas las cuentas a su nombre. Ver `entregar-al-cliente`.

---

## Tabla de costos por cliente — verificado a julio de 2026

| Servicio | Plan gratis | Límites del gratis | Plan de producción | Costo |
|---|---|---|---|---|
| Vercel | Hobby | Gratis, pero **no permite uso comercial** | Pro | **20 USD/mes por asiento**, 1 TB de transferencia |
| Supabase | Free | 0 USD, 500 MB de base, 5 GB de egress, máx. 2 proyectos activos, **se pausa tras 1 semana sin actividad** | Pro | **25 USD/mes**, 8 GB de disco, 250 GB de egress, nunca se pausa |
| Proyecto Supabase adicional | — | — | Add-on | desde **10 USD/mes** |
| Dominio | — | — | Registrador externo | 10 a 15 USD **al año** |

**Costo base de un cliente en producción: 45 USD/mes** (Vercel Pro 20 +
Supabase Pro 25), más el dominio anual.

Si ya tienes Vercel Pro y Supabase Pro para tu agencia, el cliente número dos
en adelante suma únicamente el proyecto adicional de Supabase, desde 10 USD/mes.

### Cómo se cubre con la mensualidad

| Mensualidad cobrada | Infraestructura | Margen bruto |
|---|---|---|
| 80 USD | 45 USD | 35 USD |
| 100 USD | 45 USD | 55 USD |
| 150 USD | 45 USD | 105 USD |
| 200 USD | 45 USD | 155 USD |

Con la infraestructura compartida (varios clientes sobre la misma cuenta Pro),
a partir del segundo cliente el costo marginal baja a unos 10 USD/mes y el
margen sube en consecuencia.

### Las dos reglas que no se negocian

1. **Vercel Hobby no sirve para un cliente que paga.** Es uso comercial y la
   licencia de Hobby no lo permite. Una cuenta suspendida deja el sitio del
   negocio fuera de línea sin aviso previo.
2. **Supabase Free no sirve para producción.** El proyecto se pausa tras una
   semana sin actividad: el formulario de reservas deja de responder y nadie se
   entera hasta que un cliente se queja. Free es para practicar y para demos,
   nada más.

Estos 45 USD son costo, no ganancia. Van dentro del precio que le cobras al
negocio desde el primer mes.
