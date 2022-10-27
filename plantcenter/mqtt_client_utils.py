import os
import yaml
import json
import logging
logger = logging.getLogger('file')


from .utils.check import check_key
from .models import PlantStatus

from threading import Thread
import paho.mqtt.client as mqtt_client

def start_mqtt(config_file):
    def on_connect(client: mqtt_client.Client, userdata, flags, rc):
        print("Connected with result code: " + str(rc))
    

    def on_message(client: mqtt_client.Client, userdata, message: mqtt_client.MQTTMessage):
        try:
            json_message = json.loads(message.payload.decode())
        except:
            print('error decode json', message.payload.decode())
        else:
            require_keys = ['device', 'date', 'time']
            if check_key(dict(json_message), require_keys):
                plant_status = PlantStatus()
                plant_status.device = json_message['device']
                plant_status.date = json_message['date']
                plant_status.time = json_message['time']
                # is_valid_light=json_message['light']
                if 'data' in json_message:
                    plant_data = json_message['data']
                    if 'light' in plant_data:
                        plant_status.light = plant_data['light']
                    if 'temperature' in plant_data:
                        if plant_data['temperature'] < 500:
                            plant_status.temperature = plant_data['temperature']
                    if 'humidity' in plant_data:
                        if plant_data['humidity'] < 500:
                            plant_status.humidity = plant_data['humidity']
                    plant_status.save()
                    logger.debug('plant status info write to database : %s'%json_message)
                else:
                    logger.warning('not get "data" in %s'%(json_message))
            else:
                logger.warning('not in %s'%(require_keys))

    with open(config_file, 'r') as f:

        project_config_dict = yaml.load(f, Loader=yaml.FullLoader)
        username: str = project_config_dict['mqtt']['username']
        password: str = project_config_dict['mqtt']['password']
        host: str = project_config_dict['mqtt']['host']
        port: int = project_config_dict['mqtt']['port']
        topic: str = project_config_dict['mqtt']['topic']
        # {'mqtt': {'username': 'plantsmate', 'password': 20221018, 'host': 'henryzhuhr.xyz', 'post': 1883}}
    client = mqtt_client.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    # client.on_disconnect = on_disconnect
    client.connect(host, port, 60)
    client.subscribe(topic, qos=0)
    # client.loop_misc()
    client.loop_forever()

