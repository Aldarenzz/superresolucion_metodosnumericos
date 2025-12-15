# Proyecto final 

**Autores:** Renzo Rodriguez, Ronield Sanchez, Valeria Fernandez, Joseph Damian
**Asignatura:** Electivo II de informatica
**Carrera:** Ingeniería Civil Informática  
**Universidad:** Universidad Alberto Hurtado  

---

## Descripción del Proyecto

Este proyecto implementa un sistema de super-resolución de imágenes 2D utilizando técnicas de optimización numérica.  
El objetivo es reconstruir una imagen de mayor resolución a partir de una imagen de baja resolución, formulando el problema como uno de minimización con regularización.

La solución se desarrolla en Python y se presenta mediante una aplicación web construida con Flask, que permite al usuario cargar una imagen y ejecutar el método con distintos parámetros.

---

## Estructura del Proyecto

superres_project/
│── app.py
│── requirements.txt
│── README.md
│
├── superres/
│   ├── operators.py
│   ├── regularizers.py
│   ├── gd.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── results/

---

## Ejecución del Proyecto

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows (CMD)
venv\Scripts\activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
