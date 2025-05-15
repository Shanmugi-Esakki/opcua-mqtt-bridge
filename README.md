# OPC UA to MQTT Data Bridge

## 🚀 Project Overview

This project demonstrates a real-time data publishing system using **OPC UA** for industrial data collection and **MQTT** for lightweight data transmission. It connects to a simulated OPC UA server (Prosys Simulation Server), collects sensor-like data, and publishes it to an MQTT broker. This setup is ideal for Industrial IoT (IIoT), monitoring systems, and educational purposes.

## 📌 Features

- Connects to an OPC UA simulation server (Prosys)
- Collects data from simulated nodes like `Sinusoid1`, `RandomInt32`, etc.
- Publishes data to an MQTT topic using the Paho MQTT client
- Subscriber script listens to MQTT topic and prints real-time messages
- Clean separation of publisher and subscriber components
- Easily configurable and extendable for real-world devices or cloud integration

---

## 🛠️ Technology Stack

- **Python**
- **OPC UA (via `opcua` library)**
- **MQTT (via `paho-mqtt` library)**
- **Prosys OPC UA Simulation Server**
- Tools: UaExpert (for browsing OPC UA nodes), MQTT Explorer (for monitoring MQTT messages)

---

## 🔧 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/opcua-mqtt-bridge.git
cd opcua-mqtt-bridge
```

### 2. Install Dependencies

Ensure you have Python 3.7+ installed.

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
paho-mqtt
opcua
```

### 3. Start the Prosys OPC UA Simulation Server

- Download and install from: https://www.prosysopc.com/products/opc-ua-simulation-server/
- Start the server and use the default endpoint:  
  `opc.tcp://localhost:53530/OPCUA/SimulationServer`
- Allow anonymous access during testing.

### 4. Run the Publisher

```bash
python publisher.py
```

This will:
- Connect to the OPC UA server
- Read data from node `ns=3;i=1002` (default simulated value)
- Publish it every 5 seconds to MQTT topic `opcua/data`

### 5. Run the Subscriber 

In a separate terminal:

```bash
python subscriber.py
```

This will subscribe to the `opcua/data` topic and print the received data in real time.

---

## 🧪 Testing the Integration

- Use **MQTT Explorer** to visually confirm data flow.
- Use **UaExpert** to browse and monitor OPC UA nodes.
- Modify the node ID in `publisher.py` to test different simulated sensors.

---

## 🧱 Folder Structure

```
opcua-mqtt-bridge/
│
├── publisher.py        # OPC UA to MQTT publisher script
├── subscriber.py       # MQTT subscriber script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ✅ Limitations Overcome

1. **No Physical Sensors Needed** – Used Prosys Simulation Server to mimic real-world data.  
2. **Simplified Complex Protocols** – Handled OPC UA complexity with anonymous access and default settings.  
3. **Real-Time Performance** – Tuned the data collection and MQTT publishing to work asynchronously.  
4. **Node Validation** – Used UaExpert to validate node IDs and avoid runtime errors.  
5. **Protocol Integration** – Bridged the gap between OPC UA and MQTT using Python.  
6. **Better Debugging** – Used logging and tools like MQTT Explorer to track data in real-time.

---

