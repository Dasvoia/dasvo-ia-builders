---
name: seguridad-web
description: Revisión de seguridad obligatoria antes de entregar un proyecto a un cliente o publicarlo. Cubre llaves y secretos, políticas RLS de Supabase, validación en el servidor, datos personales y privacidad, y grabación segura de pantalla. Úsala cuando el usuario vaya a entregar o publicar un proyecto, mencione seguridad, llaves, API keys, datos personales, o antes de grabar la pantalla para un video o demo.
---

# Skill: Seguridad Web para Proyectos de Clientes

## Cuándo se ejecuta

Siempre antes de: entregar a un cliente, publicar en producción, o grabar la
pantalla para un video. Si el usuario no la pide pero está por hacer una de
esas tres cosas, ofrécela: "antes de esto, hagamos la revisión de seguridad,
toma 5 minutos".

## Cómo la ejecutas

Recorre las cinco secciones EN ORDEN. En cada punto: verifica tú mismo lo que
puedas verificar con comandos o leyendo el código, marca [OK] o [FALLA], corrige lo
que falle, y muestra al final el resumen completo. No preguntes "¿quieres que
revise X?": revisa.

## 1. Llaves y secretos

- [ ] Ninguna llave, contraseña o token escrito en el código. Busca patrones
      como llaves de Supabase, cadenas largas sospechosas y URLs con
      credenciales en todos los archivos del proyecto.
- [ ] Todas las llaves viven en `.env.local` (local) y en las variables de
      entorno del hosting (producción).
- [ ] `.env.local` está en `.gitignore` y NUNCA ha sido commiteado. Verifica el
      historial de git; si alguna vez entró, la llave se considera quemada: se
      rota en el servicio y se actualiza.
- [ ] La llave service_role / secreta de Supabase no aparece en NINGÚN lugar
      del proyecto. Este sistema no la necesita.
- [ ] Nunca imprimas valores de llaves en pantalla al verificar. Comprueba
      existencia, no contenido.

## 2. Base de datos (Supabase)

- [ ] RLS (Row Level Security) está ACTIVO en todas las tablas. Una tabla sin
      RLS es una tabla pública: cualquiera con la URL puede leerla.
- [ ] Política de citas: cualquiera puede CREAR una cita; solo el usuario
      autenticado puede leerlas, actualizarlas o borrarlas.
- [ ] Política de bloqueos: solo el usuario autenticado los administra. La
      lectura pública solo si el cálculo de disponibilidad lo exige, y en ese
      caso limitada a lo mínimo.
- [ ] Prueba real: sin sesión iniciada, intenta leer citas desde el navegador o
      con una petición directa. Debe fallar.

## 3. Reglas de negocio en el servidor

- [ ] Toda validación importante ocurre en el servidor, no solo en el
      formulario: fechas pasadas, anticipación mínima, horario de atención,
      bloqueos y solapamientos.
- [ ] El caso crítico: dos personas confirmando el mismo horario al mismo
      tiempo. Solo una lo consigue; la otra recibe un mensaje claro y la lista
      de horarios se actualiza.
- [ ] Los mensajes de error hacia el usuario final son amables y sin
      información técnica (nada de códigos, rutas ni nombres de tablas).

## 4. Datos personales y privacidad

- [ ] Se pide el mínimo: nombre, contacto y motivo general. Nada más.
- [ ] Cero datos sensibles: nada de historia clínica, diagnósticos ni
      información de salud. Si el negocio los pide, la respuesta es no: este
      sistema agenda citas, no gestiona historias clínicas.
- [ ] Casilla de autorización de tratamiento de datos ANTES de confirmar la
      cita, con enlace a una política de privacidad visible (en Colombia:
      Ley 1581 de 2012; en otros países, la norma local).
- [ ] Recomienda por escrito al cliente que su abogado revise la política de
      privacidad. Eso también es protegerte a ti.

## 5. Si se va a grabar la pantalla (video, demo, tutorial)

- [ ] Perfil de navegador limpio, solo para grabar: sin marcadores, sesiones ni
      historial personal.
- [ ] Cuentas y proyectos demo, nunca los del cliente real. A los dashboards se
      entra por la URL directa del proyecto demo, nunca por la vista general
      donde se listan otros clientes.
- [ ] Notificaciones apagadas en computador y celular.
- [ ] `.env.local` jamás abierto legible en cámara: se difumina en edición
      aunque el proyecto sea desechable. Es la costumbre lo que se enseña.
- [ ] Datos de prueba ficticios: nombres y teléfonos inventados.
- [ ] Al publicar el video: borrar el proyecto demo o rotar sus llaves.

## El resumen final

Al terminar entrega esto, siempre:

```
REVISIÓN DE SEGURIDAD — [nombre del proyecto] — [fecha]
Llaves y secretos:      [OK] / [FALLA] (detalle)
Base de datos (RLS):    [OK] / [FALLA] (detalle)
Validación en servidor: [OK] / [FALLA] (detalle)
Datos personales:       [OK] / [FALLA] (detalle)
Grabación segura:       [OK] / [FALLA] / no aplica
Veredicto: LISTO PARA ENTREGAR / CORREGIR ANTES DE ENTREGAR
```

Un proyecto no se entrega con un [FALLA] en las secciones 1 a 4. Sin excepciones:
la reputación del que lo entrega vale más que la prisa.
