# Historias de usuario - Prueba automatizada con Selenium

**Nombre:** Yameli Martínez Taveras
**Matrícula:** 2023-1390

---

### 🧾 Historia 1: Campo de nombre

**Como** usuario visitante,  
**quiero** llenar el campo de nombre en el formulario,  
**para** que el sistema pueda identificar quién envía el mensaje.

- ✅ **Criterio de aceptación:** El campo acepta texto correctamente.
- ❌ **Criterio de rechazo:** El sistema permite enviar el formulario con el campo de nombre vacío.

---

### 🧾 Historia 2: Campo de correo

**Como** usuario visitante,  
**quiero** ingresar mi correo electrónico,  
**para** que puedan contactarme.

- ✅ **Criterio de aceptación:** Se acepta un correo válido con formato usuario@dominio.com.
- ❌ **Criterio de rechazo:** El sistema acepta un texto sin el formato correcto de email (sin @ o sin dominio).

---

### 🧾 Historia 3: Campo de teléfono

**Como** usuario visitante,  
**quiero** ingresar mi número de teléfono,  
**para** que puedan contactarme por ese medio.

- ✅ **Criterio de aceptación:** El campo acepta números telefónicos correctamente.
- ❌ **Criterio de rechazo:** El sistema permite enviar caracteres no numéricos en el campo de teléfono.

---

### 🧾 Historia 4: Envío de mensaje

**Como** usuario visitante,  
**quiero** enviar el formulario con mi información,  
**para** comunicarme con el equipo del sitio.

- ✅ **Criterio de aceptación:** Se muestra el mensaje de confirmación "Formulario enviado correctamente".
- ❌ **Criterio de rechazo:** No se muestra ninguna confirmación al enviar el formulario correctamente.

---

### 🧾 Historia 5: Validación de campos obligatorios

**Como** desarrollador del sitio,  
**quiero** validar que todos los campos estén completos,  
**para** asegurar que recibimos información completa.

- ✅ **Criterio de aceptación:** Se muestra alerta cuando hay campos vacíos.
- ❌ **Criterio de rechazo:** El formulario se envía con campos obligatorios vacíos.

---

### 🧾 Historia 6: Validación de formato de email

**Como** desarrollador del sitio,  
**quiero** validar que el email tenga formato correcto,  
**para** asegurar que podemos contactar al usuario.

- ✅ **Criterio de aceptación:** Se muestra alerta cuando el email tiene formato inválido.
- ❌ **Criterio de rechazo:** El sistema acepta emails con formato inválido como válidos.

---

### 🧾 Historia 7: Prueba automatizada del formulario

**Como** desarrolladora,  
**quiero** automatizar la prueba del formulario,  
**para** validar que los campos funcionan correctamente y que el mensaje se envía.

- ✅ **Criterio de aceptación:** El test llena los campos, envía y verifica el mensaje de confirmación.
- ❌ **Criterio de rechazo:** El test no captura correctamente las alertas del sistema.

---

### 🧾 Historia 8: Evidencia de ejecución

**Como** desarrolladora,  
**quiero** guardar capturas de pantalla durante la ejecución,  
**para** tener evidencia visual del proceso automatizado.

- ✅ **Criterio de aceptación:** Se generan imágenes legibles en cada paso clave de la prueba.
- ❌ **Criterio de rechazo:** Las capturas de pantalla no muestran claramente el estado del formulario o las alertas.

---

> ✅ Todas las historias han sido **implementadas y verificadas** en el proyecto.