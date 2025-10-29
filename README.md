<h1 align="center">📡 Monitor FIWARE ESP32</h1>

<p align="center">
  <b>Projeto IoT com ESP32, MQTT, Flask e Socket.IO</b><br>
  <i>Monitoramento em tempo real de temperatura, umidade e luminosidade</i>
</p>

<p align="center">
  <img src="./ffe3d022-2931-4b45-8d2e-6ab01cec1129.png" width="80%" alt="Dashboard do projeto"/>
</p>

---

<h2>🧠 Sobre o Projeto</h2>

Este projeto implementa um sistema IoT completo para monitorar em tempo real **temperatura, umidade e luminosidade**, utilizando o **ESP32**, o protocolo **MQTT** e uma interface web moderna feita com **Flask**, **Socket.IO** e **Chart.js**.

Os dados capturados pelos sensores são enviados via MQTT para o servidor, que repassa tudo ao navegador em tempo real. O resultado é um **dashboard responsivo e dinâmico**, perfeito para aplicações de monitoramento IoT.

---

<h2>👨‍💻 Integrantes</h2>

<ul>
  <li>Kauai Rosa</li>
  <li>Bruno Gama</li>
  <li>Murilo Bastos</li>
  <li>Lucas Pedro</li>
</ul>

---

<h2>🎯 Objetivos</h2>

✅ Medir temperatura e umidade com o sensor <b>DHT11</b><br>
✅ Medir luminosidade com o sensor <b>LDR</b><br>
✅ Transmitir os dados via <b>MQTT</b><br>
✅ Utilizar o <b>ESP32</b> para integração via Wi-Fi<br>
✅ Visualizar tudo em tempo real via <b>Dashboard Web</b>

---

<h2>🧩 Arquitetura do Sistema</h2>

┌──────────────┐ Wi-Fi ┌─────────────┐
│ Sensores │ ─────────────────▶ │ ESP32 │
│ DHT11 / LDR │ │ Publica no │
└──────────────┘ │ Broker MQTT│
└─────────────┘
│
MQTT (paho-mqtt)
│
┌─────────────┐
│ Flask + │
│ Socket.IO │
└─────────────┘
│
WebSocket (tempo real)
│
┌─────────────┐
│ Dashboard │
│ (HTML/JS) │
└─────────────┘

yaml
Copiar código

---

<h2>⚙️ Tecnologias Utilizadas</h2>

| Camada | Tecnologia | Descrição |
|--------|-------------|-----------|
| Microcontrolador | **ESP32** | Captura e envia dados dos sensores |
| Sensores | **DHT11** / **LDR** | Medem temperatura, umidade e luminosidade |
| Protocolo | **MQTT** | Comunicação leve entre ESP32 e servidor |
| Backend | **Flask + Socket.IO + paho-mqtt** | Recebe e envia dados em tempo real |
| Frontend | **HTML + CSS + Chart.js** | Interface moderna e responsiva |
| Broker | **FIWARE / MyMQTT / Mosquitto** | Responsável por distribuir as mensagens |

---

<h2>🧠 Estrutura de Arquivos</h2>

📁 Projeto-Monitor-FIWARE-ESP32
├── app.py # Servidor Flask + MQTT + Socket.IO
├── index.html # Dashboard Web
├── requirements.txt # Dependências Python
└── README.md # Este arquivo

yaml
Copiar código

---

<h2>🚀 Como Executar o Projeto</h2>

<h3>1️⃣ Instalar Dependências</h3>

```bash
pip install flask flask-socketio paho-mqtt eventlet
<h3>2️⃣ Configurar o Broker MQTT</h3>
Edite o arquivo app.py:

python
Copiar código
MQTT_BROKER = "44.223.0.185"   # Endereço do seu broker
MQTT_PORT = 1883
💡 Caso o broker exija login:

python
Copiar código
client.username_pw_set("usuario", "senha")
<h3>3️⃣ Executar o Servidor Flask</h3>
bash
Copiar código
python app.py
O servidor estará disponível em:<br>
👉 http://127.0.0.1:5000

<h3>4️⃣ Configurar o ESP32</h3>
No seu código (Arduino IDE):

cpp
Copiar código
const char* mqtt_server = "44.223.0.185";
const int mqtt_port = 1883;

client.publish("/TEF/device001/attrs/temp", String(temperatura).c_str());
client.publish("/TEF/device001/attrs/umid", String(umidade).c_str());
client.publish("/TEF/device001/attrs/luz", String(luminosidade).c_str());
<h3>5️⃣ Visualizar o Dashboard</h3>
Abra o navegador e veja as leituras em tempo real!
🌡️ Temperatura 💧 Umidade 💡 Luminosidade 📊 Histórico e Distribuição

<h2>📊 Interface Web</h2> <p align="center"> <img src="./ffe3d022-2931-4b45-8d2e-6ab01cec1129.png" width="85%" alt="Dashboard Monitor FIWARE ESP32"/> </p> <h3>Principais Componentes:</h3>
Cartões de métricas (temperatura, umidade, luminosidade, total de leituras)

Gráfico de linha (histórico das últimas leituras)

Gráfico de pizza (distribuição atual das medidas)

<h2>🛠️ Possíveis Erros e Soluções</h2>
Erro	Causa	Solução
TimeoutError: timed out	Broker MQTT inacessível	Verifique IP e conexão
OSError: [WinError 10048]	Porta 5000 em uso	Feche outra instância ou use port=5001
RuntimeError: Werkzeug web server...	Flask em produção	Use allow_unsafe_werkzeug=True
Dashboard não atualiza	MQTT sem dados	Verifique tópicos e publicações

<h2>🧾 Exemplo de Log (Terminal)</h2>
bash
Copiar código
[MQTT] Conectado. rc = 0
[MQTT] Subscribed: /TEF/device001/attrs/temp
[MQTT] Subscribed: /TEF/device001/attrs/umid
[MQTT] Subscribed: /TEF/device001/attrs/luz
[MQTT] Mensagem em /TEF/device001/attrs/temp: 23.4
[MQTT] Mensagem em /TEF/device001/attrs/umid: 58
[MQTT] Mensagem em /TEF/device001/attrs/luz: 81
<h2>❤️ Agradecimentos</h2> <p align="center"> Projeto desenvolvido por <b>©Company 404</b><br> Agradecemos sua atenção e interesse em recriar este projeto! 👋<br> <i>Sinta-se à vontade para expandir o sistema com novos sensores e recursos.</i> </p> ```
