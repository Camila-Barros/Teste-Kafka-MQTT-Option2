import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client('MQTTBridge')
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics['temperature4']
kafka_producer = kafka_topic.get_sync_producer()

def on_message(client, userdata, message):
    msg_payload = str(message.payload)
    print('Received MQTT message: ', msg_payload)
    kafka_producer.produce(str(msg_payload).encode('ascii'))
    print('KAFKA: Just published ' + str(msg_payload) + ' to topic temperature4')

mqtt_client.loop_start()
mqtt_client.subscribe('temperature4')
mqtt_client.on_message = on_message
time.sleep(300)
mqtt_client.loop_stop()
