import asyncio
from typing import Annotated
from fastapi import Depends
import paho.mqtt.client as mqtt

from app.core import logger
from app.core.settings import settings
from app.engine import rule_engine
from app.enumerations.device_type import DeviceType

_mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)


def on_connect(client, userdata, flags, reason_code, properties):
    logger.info(f"Connected to MQTT broker with result code {reason_code}")
    client.subscribe("devices/telemetry/#")


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    logger.debug(f"Arrived message from topic {msg.topic}")

    topic_levels = msg.topic.split('/')
    if DeviceType.UPS.name in topic_levels:
        if settings.ups_module_enabled == False:
            logger.warning(
                "Arrived UPS telemetry, but the module is not active")
            return
        else:
            device_name = msg.payload.decode("utf-8")
        asyncio.run(
            rule_engine.run_rules(DeviceType.UPS, device_name)
        )


def start_consume():
    logger.info("Starting to consume devices telemetries")
    _mqttc.on_connect = on_connect
    _mqttc.on_message = on_message
    _mqttc.connect(settings.mqtt_broker_host, 1883, 60)
    _mqttc.loop_start()


def stop_consume():
    logger.info("Stop to consume devices telemetries")
    _mqttc.disconnect()
