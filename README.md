# MQTT Mosquitto Publisher-Subscriber Setup

This project demonstrates how to run a local MQTT-based pub/sub system using the Mosquitto broker, with **1 publisher** and **2 subscribers**, built using Python.

---

## 🧠 Requirements

- Python 3.x
- Mosquitto (MQTT broker)
- Paho-MQTT library

---

## ⚙️ Installation Steps

### 1. Install Mosquitto (Broker)

- **Windows:**
  Download and install from: [https://mosquitto.org/download](https://mosquitto.org/download)

- **Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
```

Make sure Mosquitto is running before you test pub/sub.

---

### 2. Install Python Dependencies

```bash
pip install paho-mqtt
```

---

## 🚀 How to Run the Project

Open **3 separate terminals** and run the following scripts:

### ✅ Terminal 1 – Subscriber 1

```bash
python subscriber1.py
```

### ✅ Terminal 2 – Subscriber 2

```bash
python subscriber2.py
```

### ✅ Terminal 3 – Publisher

```bash
python publisher.py
```

You should see the message sent from the publisher being received by both subscribers.

---

## 📁 Project Structure

```text
MqttBrokerSetup/
├── publisher.py       # Publishes a message to a topic
├── subscriber1.py     # Subscribes and listens to messages
├── subscriber2.py     # Another subscriber
├── README.md          # This file
```

---

## ✍️ Author

**Fraz Yousaf**  
PhD Student, University of Parma  
📧 fraz.yousaf@unipr.it  
🔗 GitHub: [FrazYousaf](https://github.com/FrazYousaf)
