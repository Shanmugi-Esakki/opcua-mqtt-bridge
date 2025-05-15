import paho.mqtt.client as mqtt
from opcua import Client
import time

class OpcUaMqttPublisher:
    def __init__(self, opcua_url="opc.tcp://DESKTOP-174ECVL:53530/OPCUA/SimulationServer", mqtt_broker="localhost", mqtt_port=1883, mqtt_topic="opcua/data"):
        # OPC UA server details with your specific endpoint URL
        self.opcua_client = Client(opcua_url)
        
        # MQTT broker details
        self.mqtt_client = mqtt.Client()
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_topic = mqtt_topic

    def connect_opcua(self):
        try:
            self.opcua_client.connect()
            print("Connected to OPC UA Server.")
        except Exception as e:
            print(f"Failed to connect to OPC UA Server: {e}")

    def connect_mqtt(self):
        try:
            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
            print("Connected to MQTT Broker.")
        except Exception as e:
            print(f"Failed to connect to MQTT Broker: {e}")

    def publish_data(self, data):
        self.mqtt_client.publish(self.mqtt_topic, data)
        print(f"Published: '{data}' to MQTT topic '{self.mqtt_topic}'")

    def collect_and_publish(self):
        try:
            node = self.opcua_client.get_node("ns=3;i=1002")  # Replace with your OPC UA node ID if different
            value = node.get_value()
            print(f"Collected data from OPC UA: {value}")
            self.publish_data(str(value))
        except Exception as e:
            print(f"Failed to collect data from OPC UA: {e}")

    def run(self):
        self.connect_opcua()
        self.connect_mqtt()
        self.mqtt_client.loop_start()

        try:
            while True:
                self.collect_and_publish()
                time.sleep(5)  # Adjust the delay as necessary
        except KeyboardInterrupt:
            print("Interrupted, disconnecting...")
        finally:
            self.opcua_client.disconnect()
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            print("Disconnected from OPC UA and MQTT.")

# Run the OPC UA to MQTT publisher
if __name__ == "__main__":
    publisher = OpcUaMqttPublisher()
    publisher.run()
