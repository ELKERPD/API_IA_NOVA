from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import logging
from datetime import datetime
import os

# ============================================================
# CONFIG GENERAL
# ============================================================

app = Flask(__name__)
CORS(app)

MODEL_NAME = "qwen2.5:0.5b"
OLLAMA_URL = "http://localhost:11434/api/generate"

# ============================================================
# LOGS (para NOVA)
# Crea archivo logs/app.log y guarda errores, peticiones, etc.
# ============================================================

LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/api_nova.log"

# Crear carpeta si no existe
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_event(tipo, mensaje):
    """Guardar evento en el archivo de logs"""
    if tipo == "error":
        logging.error(mensaje)
    else:
        logging.info(mensaje)

# ============================================================
# ENDPOINT DE ESTADO (ROM / HEALTHCHECK)
# ============================================================

@app.route("/status", methods=["GET"])
def status():
    """Endpoint simple para que NOVA verifique si la API está viva"""
    return jsonify({
        "status": "ok",
        "message": "API IA de NOVA funcionando correctamente 🚀"
    })

# ============================================================
# ENDPOINT PRINCIPAL
# ============================================================

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()

        if not prompt:
            log_event("error", "Solicitud sin prompt recibido")
            return jsonify({"error": "Se requiere el campo 'prompt'"}), 400

        log_event("info", f"Prompt recibido: {prompt}")

        # Llamar a Ollama
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code != 200:
            log_event("error", f"Error desde Ollama: {response.text}")
            return jsonify({"error": "Error al comunicarse con Ollama"}), 500

        reply = response.json().get("response", "")

        log_event("info", f"Respuesta del modelo: {reply}")

        return jsonify({
            "success": True,
            "model": MODEL_NAME,
            "response": reply
        })

    except Exception as e:
        log_event("error", f"Excepción: {str(e)}")
        return jsonify({"error": "Error interno en la API", "details": str(e)}), 500

# ============================================================
# HOME
# ============================================================

@app.route("/", methods=["GET"])
def home():
    return "API IA de NOVA corriendo en Flask 🚀"


# ============================================================
# INICIO
# ============================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
