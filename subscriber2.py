from paho.mqtt.client import Client

def on_message(client, userdata, message):
    print("Subscriber 2 received:", message.payload.decode())

client = Client(client_id="sub2", protocol=3)  # No need for callback_api_version
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("iot/topic")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber 2 stopped.")
    client.disconnect()
