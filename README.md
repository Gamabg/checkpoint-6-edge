📡 Monitor FIWARE ESP32

Projeto IoT com ESP32, MQTT, Flask e Socket.IO

🧠 Sobre o Projeto

Este projeto implementa um sistema IoT completo para monitoramento em tempo real de temperatura, umidade e luminosidade, utilizando um ESP32, o protocolo MQTT e uma interface web dinâmica desenvolvida com Flask e Chart.js.

Os dados captados pelos sensores são enviados para um broker MQTT e recebidos pelo servidor Python, que transmite as atualizações em tempo real para o navegador via Socket.IO, exibindo os valores e gráficos interativos.

👨‍💻 Integrantes

Kauai Rosa

Bruno Gama

Murilo Bastos

Lucas Pedro

🎯 Objetivos

📶 Coletar dados de temperatura e umidade com o sensor DHT11.

💡 Medir a luminosidade com o sensor LDR.

☁️ Transmitir as leituras via MQTT, usando o MyMQTT ou outro cliente compatível.

🌐 Utilizar o ESP32 como nó principal, conectado ao Wi-Fi, publicando os dados periodicamente.

💻 Visualizar as informações em tempo real por meio de uma interface web interativa.

🧩 Arquitetura do Sistema
┌──────────────┐        Wi-Fi         ┌─────────────┐
│   Sensores   │  ─────────────────▶  │    ESP32    │
│ DHT11 / LDR  │                     │  Publica no │
└──────────────┘                     │   Broker MQTT│
                                     └─────────────┘
                                             │
                                   MQTT (paho-mqtt)
                                             │
                                     ┌─────────────┐
                                     │   Flask +   │
                                     │  Socket.IO  │
                                     └─────────────┘
                                             │
                                     WebSocket (tempo real)
                                             │
                                     ┌─────────────┐
                                     │  Dashboard  │
                                     │   (HTML/JS) │
                                     └─────────────┘

⚙️ Tecnologias Utilizadas
Camada	Tecnologia	Descrição
Microcontrolador	ESP32	Captura e envia dados dos sensores via MQTT
Sensores	DHT11 / LDR	Medem temperatura, umidade e luminosidade
Protocolo	MQTT	Comunicação leve e rápida entre ESP32 e servidor
Backend	Flask + Socket.IO + paho-mqtt	Recebe dados e envia em tempo real para o navegador
Frontend	HTML + CSS + Chart.js	Exibe os dados e gráficos interativos
Broker MQTT	FIWARE / MyMQTT / Mosquitto	Responsável por receber e distribuir as mensagens MQTT
🧠 Estrutura de Arquivos
📁 Projeto-Monitor-FIWARE-ESP32
├── app.py                # Servidor Flask + Socket.IO + MQTT
├── index.html            # Interface Web (Dashboard)
├── requirements.txt      # Dependências Python
└── README.md             # Documentação do projeto

🚀 Como Executar o Projeto
🧩 1. Instalar Dependências

No terminal, execute:

pip install flask flask-socketio paho-mqtt eventlet

⚙️ 2. Configurar o Broker MQTT

No arquivo app.py, altere:

MQTT_BROKER = "44.223.0.185"   # Endereço do seu broker
MQTT_PORT = 1883


💡 Se o broker exigir autenticação, descomente a linha:

client.username_pw_set("usuario", "senha")

🧠 3. Executar o Servidor Flask

Execute o comando:

python app.py


O servidor estará disponível em:
👉 http://127.0.0.1:5000

📲 4. Configurar o ESP32 (publicador)

No código do ESP32, configure:

const char* mqtt_server = "44.223.0.185";
const int mqtt_port = 1883;
client.publish("/TEF/device001/attrs/temp", String(temperatura).c_str());
client.publish("/TEF/device001/attrs/umid", String(umidade).c_str());
client.publish("/TEF/device001/attrs/luz", String(luminosidade).c_str());

🌐 5. Visualizar no Navegador

Abra o dashboard e veja as leituras sendo atualizadas em tempo real:

🌡️ Temperatura

💧 Umidade

💡 Luminosidade

📊 Histórico de leituras e gráfico de distribuição

📊 Interface Web (Dashboard)

O dashboard exibe os dados de forma clara e moderna, com:

Cartões de indicadores (temperatura, umidade, luminosidade, total de leituras)

Gráfico de linha (histórico das últimas 12 leituras)

Gráfico de pizza (distribuição atual)

🛠️ Possíveis Erros e Soluções
Erro	Causa	Solução
TimeoutError: timed out	Broker MQTT inacessível	Verifique IP, porta e conexão à internet
OSError: [WinError 10048]	Porta 5000 já em uso	Feche a aba antiga ou mude a porta (port=5001)
RuntimeError: Werkzeug web server...	Flask detecta uso em produção	Use allow_unsafe_werkzeug=True no socketio.run()
Dashboard sem atualização	MQTT não está enviando dados	Verifique se o ESP32 está publicando nos tópicos corretos
🧾 Exemplo de Log (Terminal)
[MQTT] Conectado. rc = 0
[MQTT] Subscribed: /TEF/device001/attrs/temp
[MQTT] Subscribed: /TEF/device001/attrs/umid
[MQTT] Subscribed: /TEF/device001/attrs/luz
[MQTT] Mensagem em /TEF/device001/attrs/temp: 23.4
[MQTT] Mensagem em /TEF/device001/attrs/umid: 58
[MQTT] Mensagem em /TEF/device001/attrs/luz: 81

❤️ Agradecimentos

Projeto desenvolvido por ©Company 404
Agradecemos sua atenção e interesse em recriar este projeto! 👋
Sinta-se à vontade para expandir o sistema com novos sensores ou armazenar os dados em banco de dados.
