#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Sensor v2.0 MQTT flavour
# (c) Electrosense Project
#
#  [TODO] License text
#
# Héctor Cordobés - hcordobes@imdea.org - 2017
# Markus Fuchs - fuchs@sero-systems.de - 2019
#

import sys
import random
import logging
import netifaces

# internals
from controller_config import config
from mqtt.mqttengine import MqttEngine
from mqtt.avro_parser import AvroParser
from mqtt_sensor.sensor_manager import SensorManager, create_cmd_mapper


cfgs = ["sensor.cfg", "/etc/electrosense/sensor.cfg"]
conf = config.read(cfgs)
env_config = conf.section("environment")

log_config = conf.section("log")
log_level = getattr(logging, log_config["level"].upper(), None)
if not isinstance(log_level, int):
    raise ValueError('Invalid log level: %s' % log_config["level"])

logger = logging.getLogger("sensor")
logger.setLevel(log_level)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

# Console handler
if "console" in log_config.keys():
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

# File handler --> currently not used in prod due to ro file system
if "file" in log_config.keys():
    fh = logging.FileHandler(filename=log_config["file"])
    fh.setFormatter(formatter)
    logger.addHandler(fh)


def get_mac_address(iface):
    try:
        if_addr = netifaces.ifaddresses(iface)
        return str(if_addr[netifaces.AF_LINK][0]['addr'])
    except ValueError:
        logger.error("Could not read MAC address for interface {}".format(iface))
        sys.exit(1)


if __name__ == "__main__":
    # apply serial number from config if present, otherwise take MAC address
    if "serialnumber" in env_config.keys():
        mac_address = env_config["serialnumber"]
        logger.info("Using 'serialnumber' from config file as MAC address: {}".format(str(mac_address)))
    else:
        mac_address = get_mac_address(env_config["interface"])

    mqtt_config = conf.section("mqtt")
    with_sudo = env_config["sudo"] == "true"
    translation = str.maketrans('', '', ":.- ")
    serial_number = int(mac_address.translate(translation), 16)

    # If userid is defined it overrides the detected value
    client_id = mqtt_config["userid"] if "userid" in mqtt_config.keys() else str(serial_number)
    topics = ["control/sensor/all", "control/sensor/id/" + client_id]

    # ensure this is set
    mqtt_config["userid"] = client_id

    logger.info("******* Controller Starting *******")
    logger.info("MAC Address: {}".format(mac_address))
    logger.info("Client ID:   {}".format(client_id))

    avro_parser = AvroParser(conf.section("avro"))
    mqtt_engine = MqttEngine(mqtt_config, avro_parser, topics)
    cmd_mapper = create_cmd_mapper(with_sudo, conf.section("parameters"))
    sensor_manager = SensorManager(mqtt_engine, serial_number, cmd_mapper, with_sudo, client_id)

    # TODO why is this?
    random.seed()

    mqtt_engine.start()
    sensor_manager.start()