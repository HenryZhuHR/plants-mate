from pprint import pprint
import yaml
import json
import paho.mqtt.client as mqtt_client

PROJECT_CONFIG = 'configs/settings.yaml'
with open(PROJECT_CONFIG, 'r') as f:
    project_config_dict = yaml.load(f, Loader=yaml.FullLoader)
username: str = project_config_dict['mqtt']['username']
password: str = project_config_dict['mqtt']['password']
host: str = project_config_dict['mqtt']['host']
port: int = project_config_dict['mqtt']['port']
topic: str = project_config_dict['mqtt']['topic']


def on_connect(client: mqtt_client.Client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client: mqtt_client.Client, userdata, message: mqtt_client.MQTTMessage):
    try:
        json_message = json.loads(message.payload.decode())   
    except:
        print('error decode json',message.payload.decode())
    else:
        print(message.topic, json_message)
        

client = mqtt_client.Client()
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
# client.on_disconnect = on_disconnect
client.connect(host, port, 60)
client.subscribe(topic, qos=0)
# client.loop_misc()
client.loop_forever()