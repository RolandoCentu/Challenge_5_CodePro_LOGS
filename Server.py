
rom flask import Flask, request, jsonify      # importamos flask para crear el servidor de logging
import sqlite3
from datetime import datetime

app = Flask(__name__)        # creamos una instancia de la clase Flask para nuestro servidor 

# Definimos tokens validos para autenticar los servicios que envían logs, 1 token es invalido
TOKENS_VALIDOS = {
    "token_service_a": "service_a",
    "token_service_b": "service_b",
    "token_service_c": "service_c"}
