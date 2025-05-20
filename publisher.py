from paho.mqtt.client import Client
import time

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))

client = Client(client_id="pub", protocol=3)
client.on_connect = on_connect
client.connect("localhost", 1883)

try:
    while True:
        client.publish("iot/topic", "Hello from Publisher")
        print("Message published")
        time.sleep(5)
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()
