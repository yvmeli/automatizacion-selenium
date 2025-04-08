# Proyecto: Prueba automatizada con Selenium - Formulario HTML

**Nombre:** Yameli Martínez Taveras  
**Matrícula:** 2023-1390  

---

## 📝 Descripción

Este proyecto consiste en una automatización sencilla con **Python y Selenium** para validar un formulario web. Se simula el llenado de un formulario HTML con los campos de nombre, correo y mensaje, y se verifica que se muestre una alerta de "Mensaje enviado con éxito".

Además, se incluyen capturas de pantalla automáticas de cada paso del proceso y un reporte HTML generado con `pytest-html`.

---

## 📂 Estructura del proyecto

auto/
├── form.html # Formulario HTML a automatizar
├── test_form.py # Script de pruebas con Selenium
├── requirements.txt # Dependencias del proyecto
├── screenshots/ # Capturas de pantalla automáticas
├── reports/ # Reportes HTML generados
├── docs/
│ └── historias_usuario.md # Documentación de requerimientos
└── README.md # Archivo principal de documentación

---

## ✅ Tecnologías utilizadas

- Python 3.13
- Selenium
- Pytest
- pytest-html
- Google Chrome + WebDriver

---

## 🚀 Cómo ejecutar

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta la prueba automatizada y genera el reporte:

```bash
python -m pytest test_form.py --html=reports/report.html
```

# 📋 Revisa:

- **📷 Capturas de pantalla** en `screenshots/`
- **📊 Reporte detallado** en `reports/report.html`

---

## 📚 Historias de Usuario
Las historias de usuario están disponibles en:  
📄 `docs/historias_usuario.md`

---

## 🎥 Video

👉 Aquí puedes enlazar el video de demostración cuando esté listo.

---

## 📬 Contacto

Cualquier duda o comentario, puedes escribirme directamente.


---

¿Te gustaría que también te genere el archivo `requirements.txt` con las dependencias exactas que usaste? Puedo dejarte todo listo para subirlo a GitHub.