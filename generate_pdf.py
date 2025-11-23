#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar PDF de la documentación README.md
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime

# Crear documento PDF
pdf_file = "NOVA_API_IA_Documentacion.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=0.5*inch, leftMargin=0.5*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Estilos
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1f77b4'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading1_style = ParagraphStyle(
    'CustomHeading1',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.HexColor('#1f77b4'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

heading2_style = ParagraphStyle(
    'CustomHeading2',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#2ca02c'),
    spaceAfter=10,
    spaceBefore=10,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=10
)

code_style = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    textColor=colors.HexColor('#333333'),
    leftIndent=20,
    rightIndent=20,
    spaceAfter=10,
    backColor=colors.HexColor('#f0f0f0')
)

# Contenido del PDF
story = []

# Título
story.append(Paragraph("🚀 NOVA API IA", title_style))
story.append(Paragraph("Documentación Completa del Proyecto", styles['Normal']))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph(f"Generado: {datetime.now().strftime('%d de %B de %Y')}", styles['Normal']))
story.append(Spacer(1, 0.3*inch))

# Introducción
story.append(Paragraph("Descripción del Proyecto", heading1_style))
story.append(Paragraph(
    "NOVA API IA es una API REST construida con Flask que proporciona acceso a modelos de inteligencia artificial "
    "locales mediante Ollama. Esta API permite que la aplicación NOVA realice consultas a modelos de IA sin depender "
    "de servicios en la nube.",
    body_style
))
story.append(Spacer(1, 0.1*inch))

# Características
story.append(Paragraph("Características Principales:", heading2_style))
features = [
    "✓ API REST con endpoints simples y claros",
    "✓ Integración con Ollama (ejecución local de modelos IA)",
    "✓ Modelo Qwen 2.5 0.5B (ligero y rápido)",
    "✓ Sistema completo de logs y monitoreo",
    "✓ CORS habilitado para compatibilidad multi-origen",
    "✓ Health check automático",
    "✓ Manejo robusto de errores"
]
for feature in features:
    story.append(Paragraph(feature, body_style))
story.append(Spacer(1, 0.2*inch))

# Requisitos del Sistema
story.append(Paragraph("Requisitos del Sistema", heading1_style))

story.append(Paragraph("Software Requerido:", heading2_style))
requirements = [
    "Python 3.8 o superior",
    "Ollama (para ejecutar modelos de IA)",
    "pip (gestor de paquetes de Python)",
    "Windows PowerShell o CMD"
]
for req in requirements:
    story.append(Paragraph("• " + req, body_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Requisitos Mínimos de Hardware:", heading2_style))
hw = [
    "Procesador: Intel i5 / AMD Ryzen 5 o superior",
    "RAM: 4 GB mínimo, 8 GB recomendado",
    "Almacenamiento: 5 GB libres (para modelos)",
    "Conexión a Internet (solo para descargas iniciales)"
]
for h in hw:
    story.append(Paragraph("• " + h, body_style))
story.append(Spacer(1, 0.2*inch))

# Instalación
story.append(Paragraph("Instalación y Configuración", heading1_style))

story.append(Paragraph("Paso 1: Navegar a la Carpeta del Proyecto", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>cd C:\\xampp\\htdocs\\NOVA_ASISTENTE\\API_IA</font>",
    code_style
))

story.append(Paragraph("Paso 2: Crear Entorno Virtual", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>python -m venv venv</font>",
    code_style
))

story.append(Paragraph("Paso 3: Activar Entorno Virtual", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>.\\venv\\Scripts\\activate</font>",
    code_style
))

story.append(Paragraph("Paso 4: Instalar Dependencias", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>pip install -r requirements.txt</font>",
    code_style
))

story.append(Spacer(1, 0.2*inch))

# Ollama
story.append(Paragraph("Configuración de Ollama e IA", heading1_style))

story.append(Paragraph("Paso 1: Descargar e Instalar Ollama", heading2_style))
story.append(Paragraph(
    "1. Ir a https://ollama.ai<br/>"
    "2. Descargar la versión para Windows<br/>"
    "3. Ejecutar el instalador y seguir las instrucciones",
    body_style
))

story.append(Paragraph("Paso 2: Descargar Modelo Qwen 2.5 0.5B", heading2_style))
story.append(Paragraph(
    "Ejecutar en PowerShell (sin venv activado):",
    body_style
))
story.append(Paragraph(
    "<font face='Courier' size='9'>ollama pull qwen2.5:0.5b</font>",
    code_style
))
story.append(Paragraph(
    "Esto descargará aproximadamente 300-400 MB. Tiempo estimado: 2-5 minutos.",
    body_style
))

story.append(Paragraph("Paso 3: Iniciar Ollama en Modo Servidor", heading2_style))
story.append(Paragraph(
    "En una terminal nueva ejecutar:",
    body_style
))
story.append(Paragraph(
    "<font face='Courier' size='9'>ollama serve</font>",
    code_style
))
story.append(Paragraph(
    "Mantén esta terminal abierta mientras ejecutas la API.",
    body_style
))

story.append(PageBreak())

# Endpoints
story.append(Paragraph("Endpoints de la API", heading1_style))

story.append(Paragraph("1. GET /status - Health Check", heading2_style))
story.append(Paragraph(
    "Verifica si la API está funcionando correctamente.",
    body_style
))
story.append(Paragraph(
    "URL: <font face='Courier'>http://localhost:5002/status</font>",
    code_style
))

story.append(Paragraph("2. POST /chat - Consulta a la IA", heading2_style))
story.append(Paragraph(
    "Envía un prompt a la IA y recibe una respuesta.",
    body_style
))
story.append(Paragraph(
    "URL: <font face='Courier'>http://localhost:5002/chat</font>",
    code_style
))
story.append(Paragraph(
    "Body esperado:<br/>"
    "<font face='Courier' size='9'>{\"prompt\": \"Tu pregunta aquí\"}</font>",
    code_style
))

story.append(Paragraph("3. GET / - Home", heading2_style))
story.append(Paragraph(
    "Endpoint raíz para verificar que la API está respondiendo.",
    body_style
))

story.append(Spacer(1, 0.2*inch))

# Ejecución
story.append(Paragraph("Ejecutar la API", heading1_style))

story.append(Paragraph("Terminal 1 - Iniciar Ollama:", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>ollama serve</font>",
    code_style
))

story.append(Paragraph("Terminal 2 - Iniciar API Flask:", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>cd C:\\xampp\\htdocs\\NOVA_ASISTENTE\\API_IA<br/>"
    ".\\venv\\Scripts\\activate<br/>"
    "python api_ia.py</font>",
    code_style
))

story.append(Spacer(1, 0.2*inch))

# Logs
story.append(Paragraph("Logs y Monitoreo", heading1_style))

story.append(Paragraph(
    "Los logs se guardan en: <font face='Courier'>logs/api_nova.log</font>",
    body_style
))

story.append(Paragraph("Ver últimas 50 líneas del log:", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>Get-Content logs\\api_nova.log -Tail 50</font>",
    code_style
))

story.append(Paragraph("Buscar errores:", heading2_style))
story.append(Paragraph(
    "<font face='Courier' size='9'>Select-String \"ERROR\" logs\\api_nova.log</font>",
    code_style
))

story.append(PageBreak())

# Solución de Problemas
story.append(Paragraph("Solución de Problemas", heading1_style))

story.append(Paragraph("Problema 1: Connection refused", heading2_style))
story.append(Paragraph(
    "Causa: Ollama no está ejecutándose<br/>"
    "Solución: Abrir una nueva terminal y ejecutar <font face='Courier'>ollama serve</font>",
    body_style
))

story.append(Paragraph("Problema 2: Module not found", heading2_style))
story.append(Paragraph(
    "Causa: El entorno virtual no está activado<br/>"
    "Solución: Ejecutar <font face='Courier'>.\\venv\\Scripts\\activate</font>",
    body_style
))

story.append(Paragraph("Problema 3: Puerto 5002 ya está en uso", heading2_style))
story.append(Paragraph(
    "Solución: Ejecutar <font face='Courier'>netstat -ano | findstr :5002</font> "
    "para encontrar el proceso y matarlo con <font face='Courier'>taskkill /PID [PID] /F</font>",
    body_style
))

story.append(Paragraph("Problema 4: Modelo no encontrado", heading2_style))
story.append(Paragraph(
    "Solución: Ejecutar <font face='Courier'>ollama pull qwen2.5:0.5b</font>",
    body_style
))

story.append(Spacer(1, 0.3*inch))

# Footer
story.append(Paragraph(
    f"Documentación generada: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | "
    "NOVA API IA v1.0",
    styles['Normal']
))

# Construir PDF
doc.build(story)
print(f"[OK] PDF generado exitosamente: {pdf_file}")
print(f"[PDF] Ubicacion: C:\\xampp\\htdocs\\NOVA_ASISTENTE\\API_IA\\{pdf_file}")
