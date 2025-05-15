import paho.mqtt.client as mqtt

class MqttSubscriber:
    def __init__(self, mqtt_broker="localhost", mqtt_port=1883, mqtt_topic="opcua/data"):
        self.mqtt_client = mqtt.Client()
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_topic = mqtt_topic

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Subscriber connected to the broker.")
            client.subscribe(self.mqtt_topic)
        else:
            print(f"Connection failed with code {rc}")

    def on_message(self, client, userdata, msg):
        print(f"Message received on topic '{msg.topic}': {msg.payload.decode()}")

    def connect(self):
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
        self.mqtt_client.loop_forever()

# Run the MQTT subscriber
if __name__ == "__main__":
    subscriber = MqttSubscriber()
    subscriber.connect()
