import paho.mqtt.client as mqtt

from app.core import logger

_mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def on_connect(client, userdata, flags, reason_code, properties):
    logger.info(f"Connected with result code {reason_code}")
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    logger.info(msg.topic+" "+str(msg.payload))

def start_consume():
    logger.info("Starting to consume devices telemetries")
    _mqttc.on_connect = on_connect
    _mqttc.on_message = on_message
    _mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
    _mqttc.loop_start()

def stop_consume():
    logger.info("Stop to consume devices telemetries")
    _mqttc.disconnect()