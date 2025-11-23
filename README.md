<<<<<<< HEAD
# 🚀 NOVA API IA - Documentación Completa

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación y Configuración](#instalación-y-configuración)
4. [Configuración de Ollama e IA](#configuración-de-ollama-e-ia)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Endpoints de la API](#endpoints-de-la-api)
7. [Logs y Monitoreo](#logs-y-monitoreo)
8. [Ejecutar la API](#ejecutar-la-api)
9. [Pruebas de la API](#pruebas-de-la-api)
10. [Solución de Problemas](#solución-de-problemas)

---

## Descripción del Proyecto

**NOVA API IA** es una API REST construida con **Flask** que proporciona acceso a modelos de inteligencia artificial locales mediante **Ollama**. Esta API permite que la aplicación NOVA realice consultas a modelos de IA sin depender de servicios en la nube.

### Características Principales:
- ✅ API REST con endpoints simples y claros
- ✅ Integración con Ollama (ejecución local de modelos IA)
- ✅ Modelo Qwen 2.5 0.5B (ligero y rápido)
- ✅ Sistema completo de logs y monitoreo
- ✅ CORS habilitado para compatibilidad multi-origen
- ✅ Health check automático
- ✅ Manejo robusto de errores

---

## Requisitos del Sistema

### Software Requerido:
- **Python** 3.8 o superior
- **Ollama** (para ejecutar modelos de IA)
- **pip** (gestor de paquetes de Python)
- Windows PowerShell o CMD

### Requisitos Mínimos de Hardware:
- Procesador: Intel i5 / AMD Ryzen 5 o superior
- RAM: 4 GB mínimo, 8 GB recomendado
- Almacenamiento: 5 GB libres (para modelos)
- Conexión a Internet (solo para descargas iniciales)

---

## Instalación y Configuración

### Paso 1: Clonar o Descargar el Proyecto

```powershell
# Navegar a la carpeta del proyecto
cd C:\xampp\htdocs\NOVA_ASISTENTE\API_IA
```

### Paso 2: Crear Entorno Virtual

```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\activate

# Verificar que esté activado (deberá mostrar (venv) en el prompt)
```

### Paso 3: Instalar Dependencias

```powershell
# Instalar las dependencias del proyecto
pip install -r requirements.txt

# Las dependencias instaladas son:
# - flask: Framework web
# - flask-cors: Soporte CORS
# - requests: Cliente HTTP
# - sseclient-py: Soporte para Server-Sent Events
```

### Paso 4: Verificar Instalación

```powershell
# Verificar que Python tiene las dependencias correctas
pip list

# Deberá mostrar todas las librerías instaladas con sus versiones
```

---

## Configuración de Ollama e IA

### Paso 1: Descargar e Instalar Ollama

1. **Descargar Ollama:**
   - Ir a https://ollama.ai
   - Descargar la versión para Windows
   - Ejecutar el instalador y seguir las instrucciones

2. **Verificar la instalación:**
   ```powershell
   # En una terminal nueva (sin venv activado)
   ollama --version
   ```

### Paso 2: Descargar el Modelo Qwen 2.5 0.5B

El modelo utilizado es **Qwen 2.5 0.5B**, optimizado para ser ligero y rápido.

```powershell
# En una terminal nueva (sin venv activado o en otra ventana)
ollama pull qwen2.5:0.5b

# Esto descargará el modelo (~300-400 MB)
# Tiempo estimado: 2-5 minutos (depende de tu conexión)
```

### Paso 3: Verificar que el Modelo está Descargado

```powershell
# Listar modelos disponibles
ollama list

# Deberá mostrar: qwen2.5:0.5b
```

### Paso 4: Iniciar Ollama en Modo Servidor

Antes de ejecutar la API, necesitas tener Ollama corriendo como servidor:

```powershell
# En una terminal nueva
ollama serve

# Salida esperada:
# 2025-11-21T10:30:00.000000Z INFO [llm] starting up the LLM...
# 2025-11-21T10:30:05.000000Z INFO [llm] loaded model qwen2.5:0.5b
# Listening on 127.0.0.1:11434
```

**Nota:** Mantén esta terminal abierta mientras ejecutas la API.

### Paso 5: Prueba Rápida de Ollama

```powershell
# En otra terminal, puedes probar Ollama directamente
ollama run qwen2.5:0.5b "Hola, ¿quién eres?"

# El modelo responderá con un saludo
```

---

## Estructura del Proyecto

```
C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\
│
├── api_ia.py              # Archivo principal de la API
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Esta documentación
│
├── venv/                 # Entorno virtual (creado automáticamente)
│   ├── Scripts/
│   │   ├── activate      # Script para activar venv
│   │   ├── python.exe
│   │   └── pip.exe
│   └── Lib/
│
└── logs/                 # Carpeta de logs (creada automáticamente)
    └── api_nova.log      # Archivo de registro de eventos
```

### Descripción de Archivos:

| Archivo | Descripción |
|---------|-------------|
| `api_ia.py` | Código principal de la API Flask con todos los endpoints |
| `requirements.txt` | Lista de dependencias Python necesarias |
| `README.md` | Documentación del proyecto (este archivo) |
| `venv/` | Entorno virtual aislado con todas las dependencias |
| `logs/api_nova.log` | Registro de todas las operaciones, errores y eventos |

---

## Endpoints de la API

### 1. **GET /status** - Health Check

Verifica si la API está funcionando correctamente.

**URL:** `http://localhost:5002/status`

**Método:** `GET`

**Respuesta Exitosa (200):**
```json
{
  "status": "ok",
  "message": "API IA de NOVA funcionando correctamente 🚀"
}
```

**Uso:**
```powershell
# Desde PowerShell
Invoke-WebRequest -Uri "http://localhost:5002/status" -Method GET
```

---

### 2. **POST /chat** - Consulta a la IA

Envía un prompt a la IA y recibe una respuesta.

**URL:** `http://localhost:5002/chat`

**Método:** `POST`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "prompt": "Tu pregunta o consulta aquí"
}
```

**Respuesta Exitosa (200):**
```json
{
  "success": true,
  "model": "qwen2.5:0.5b",
  "response": "Respuesta de la IA aquí"
}
```

**Respuesta con Error (400 o 500):**
```json
{
  "error": "Descripción del error",
  "details": "Información adicional del error"
}
```

**Ejemplos de Uso:**

```powershell
# Usando PowerShell
$body = @{
    prompt = "¿Cuál es la capital de Francia?"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5002/chat" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

```bash
# Usando curl (en otra terminal/bash)
curl -X POST http://localhost:5002/chat \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"¿Cuál es 2+2?\"}"
```

```python
# Usando Python
import requests

response = requests.post(
    "http://localhost:5002/chat",
    json={"prompt": "Explica qué es la inteligencia artificial"}
)
print(response.json())
```

---

### 3. **GET /** - Home

Endpoint raíz para verificar que la API está respondiendo.

**URL:** `http://localhost:5002/`

**Método:** `GET`

**Respuesta:** `API IA de NOVA corriendo en Flask 🚀`

---

## Logs y Monitoreo

### Ubicación del Archivo de Logs

```
C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\logs\api_nova.log
```

### Tipos de Eventos Registrados

1. **INFO:** Solicitudes recibidas, respuestas exitosas
2. **ERROR:** Errores en la comunicación, excepciones, fallos

### Ejemplo de Contenido del Log

```
2025-11-21 10:30:15,123 [INFO] Prompt recibido: ¿Cuál es tu nombre?
2025-11-21 10:30:18,456 [INFO] Respuesta del modelo: Mi nombre es Qwen...
2025-11-21 10:31:02,789 [ERROR] Error desde Ollama: Connection refused
```

### Cómo Revisar los Logs

```powershell
# Ver últimas 50 líneas del log
Get-Content C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\logs\api_nova.log -Tail 50

# Ver logs en tiempo real
Get-Content -Path C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\logs\api_nova.log -Tail 10 -Wait

# Buscar errores en los logs
Select-String "ERROR" C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\logs\api_nova.log
```

---

## Ejecutar la API

### Opción 1: Ejecución Manual Paso a Paso

**Terminal 1 - Iniciar Ollama:**
```powershell
# Sin activar venv
ollama serve
```

**Terminal 2 - Iniciar API Flask:**
```powershell
# Navegar al proyecto
cd C:\xampp\htdocs\NOVA_ASISTENTE\API_IA

# Activar entorno virtual
.\venv\Scripts\activate

# Ejecutar la API
python api_ia.py

# Salida esperada:
# * Serving Flask app 'api_ia'
# * Debug mode: on
# * Running on http://0.0.0.0:5002
```

### Opción 2: Script de Ejecución Automática

Crea un archivo `run.ps1`:

```powershell
# Iniciar Ollama (en background)
Start-Process -FilePath "ollama" -ArgumentList "serve"

# Esperar a que Ollama esté listo
Start-Sleep -Seconds 3

# Navegar a la carpeta del proyecto
cd C:\xampp\htdocs\NOVA_ASISTENTE\API_IA

# Activar venv
.\venv\Scripts\activate

# Ejecutar API
python api_ia.py
```

Para ejecutar: `.\run.ps1`

---

## Pruebas de la API

### Prueba 1: Verificar Conexión

```powershell
# Abrir PowerShell y ejecutar:
Invoke-WebRequest -Uri "http://localhost:5002/status" -Method GET | ConvertTo-Json
```

**Resultado Esperado:**
```
{
  "status": "ok",
  "message": "API IA de NOVA funcionando correctamente 🚀"
}
```

---

### Prueba 2: Consulta Básica a la IA

```powershell
$body = @{
    prompt = "¿Cuál es la capital de España?"
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://localhost:5002/chat" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

$response.Content | ConvertFrom-Json
```

**Resultado Esperado:**
```json
{
  "success": true,
  "model": "qwen2.5:0.5b",
  "response": "La capital de España es Madrid..."
}
```

---

### Prueba 3: Prueba de Rendimiento

```powershell
# Script para medir tiempo de respuesta
$prompts = @(
    "¿Qué es Python?",
    "Cuéntame un chiste",
    "¿Cuál es 2+2?"
)

foreach ($prompt in $prompts) {
    $body = @{ prompt = $prompt } | ConvertTo-Json
    
    $start = Get-Date
    $response = Invoke-WebRequest -Uri "http://localhost:5002/chat" `
        -Method POST `
        -ContentType "application/json" `
        -Body $body
    $end = Get-Date
    
    $time = ($end - $start).TotalSeconds
    Write-Host "Prompt: $prompt | Tiempo: ${time}s"
}
```

---

## Solución de Problemas

### Problema 1: "Connection refused" al conectar con Ollama

**Causa:** Ollama no está ejecutándose

**Solución:**
```powershell
# Abrir una nueva terminal y ejecutar:
ollama serve

# Mantener esta terminal abierta
```

---

### Problema 2: Error "Module not found" al ejecutar la API

**Causa:** El entorno virtual no está activado o las dependencias no están instaladas

**Solución:**
```powershell
# Activar venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar de nuevo
python api_ia.py
```

---

### Problema 3: Puerto 5002 ya está en uso

**Causa:** Otra aplicación está usando el puerto

**Solución:**

```powershell
# Encontrar proceso usando puerto 5002
netstat -ano | findstr :5002

# Matar el proceso (reemplazar PID por el número encontrado)
taskkill /PID <PID> /F

# O cambiar puerto en api_ia.py (línea 108)
# Cambiar: app.run(host="0.0.0.0", port=5003, debug=True)
```

---

### Problema 4: Modelo no encontrado "qwen2.5:0.5b"

**Causa:** El modelo no está descargado

**Solución:**
```powershell
# Descargar el modelo
ollama pull qwen2.5:0.5b

# Esperar a que termine la descarga
```

---

### Problema 5: API lenta o congelada

**Causa:** Ollama está procesando una solicitud grande o el hardware es insuficiente

**Solución:**
- Aumentar tiempo de espera en cliente
- Usar prompts más cortos
- Asegurar disponibilidad de RAM
- Revisar logs: `Get-Content C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\logs\api_nova.log -Tail 50`

---

## Información Técnica

### Dependencias del Proyecto

```
flask==3.0.0                    # Framework web
flask-cors==4.0.0               # Soporte CORS
requests==2.31.0                # Cliente HTTP
sseclient-py==1.7               # Server-Sent Events
```

### Configuración de la API

```python
# Host: 0.0.0.0 (Accesible desde cualquier interfaz)
# Puerto: 5002
# Debug Mode: Activado (desarrollo)
# Modelo IA: qwen2.5:0.5b
# URL Ollama: http://localhost:11434/api/generate
```

### Versiones Probadas

- Python: 3.10, 3.11
- Windows: 10, 11
- Ollama: v0.1.0+
- Flask: 3.0.0

---

## Guía Rápida de Referencia

```powershell
# ========== PRIMER INICIO ==========

# 1. Abrir Terminal 1 - Iniciar Ollama
ollama serve

# 2. Abrir Terminal 2 - Iniciar API
cd C:\xampp\htdocs\NOVA_ASISTENTE\API_IA
.\venv\Scripts\activate
python api_ia.py

# 3. Abrir Terminal 3 - Hacer pruebas
Invoke-WebRequest -Uri "http://localhost:5002/status" -Method GET

# ========== INICIOS POSTERIORES ==========

# Terminal 1: Ollama
ollama serve

# Terminal 2: API
cd C:\xampp\htdocs\NOVA_ASISTENTE\API_IA
.\venv\Scripts\activate
python api_ia.py

# ========== ACTUALIZAR DEPENDENCIAS ==========
.\venv\Scripts\activate
pip install -r requirements.txt --upgrade

# ========== VER LOGS ==========
Get-Content C:\xampp\htdocs\NOVA_ASISTENTE\API_IA\logs\api_nova.log -Tail 50
```

---

## Contacto y Soporte

Para problemas o preguntas sobre la API:
1. Revisar los logs: `logs/api_nova.log`
2. Verificar que Ollama está ejecutándose
3. Confirmar que el modelo está descargado: `ollama list`
4. Revisar la sección "Solución de Problemas"

---

**Última actualización:** Noviembre 21, 2025

✅ Documentación Completa - Proyecto NOVA API IA
=======
# API_IA_NOVA
PROYECTO  DE CASA INTELIGENTE UNIVERCIDAD
>>>>>>> 99533923c0a605f9c34a65e8aaedb3a7bf22f289
