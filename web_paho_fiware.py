from flask import Flask, render_template_string
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

# ==== MQTT ====
MQTT_BROKER = "44.223.0.185"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_TOPICS = [
    "/TEF/device001/attrs/temp",
    "/TEF/device001/attrs/luz",
    "/TEF/device001/attrs/umid"
]

# ==== Flask / SocketIO ====
app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading", cors_allowed_origins="*")

# Dicionário para armazenar últimos valores
dados_atuais = {"temp": 0, "luz": 0, "umid": 0}

# ---- Callbacks MQTT ----
def on_connect(client, userdata, flags, rc):
    print("[MQTT] Conectado. rc =", rc)
    for topic in MQTT_TOPICS:
        client.subscribe(topic)
        print(f"[MQTT] Subscribed: {topic}")

def on_message(client, userdata, msg):
    raw = msg.payload
    valor = None
    try:
        decoded = raw.decode("utf-8", errors="replace").strip()
        try:
            obj = json.loads(decoded)
            if isinstance(obj, dict):
                for k in ("value", "l", "valor", "data", "v"):
                    if k in obj:
                        valor = obj[k]
                        break
                if valor is None:
                    valor = obj
            else:
                valor = obj
        except json.JSONDecodeError:
            try:
                valor = float(decoded)
            except ValueError:
                valor = decoded
    except Exception as e:
        print("[MQTT] Erro ao processar payload:", e)
        valor = None

    # Identifica qual sensor chegou
    if "temp" in msg.topic:
        dados_atuais["temp"] = valor
    elif "luz" in msg.topic:
        dados_atuais["luz"] = valor
    elif "umid" in msg.topic:
        dados_atuais["umid"] = valor

    socketio.emit("novo_dado", {"topico": msg.topic, "valor": valor, "dados": dados_atuais})
    print(f"[MQTT] Mensagem em {msg.topic}: {valor}")

# ---- Configura MQTT ----
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
client.loop_start()

# ---- Página HTML ----
@app.route("/")
def index():
    return render_template_string(open("index.html").read())

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
