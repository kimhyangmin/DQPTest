import random
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from awscrt import mqtt

# AWS IoT Core
#ENDPOINT = 'a2fohdr218kpa4-ats.iot.ap-northeast-1.amazonaws.com'
ENDPOINT = 't3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com'
CLIENT_ID = 'eviot'
TOPIC = 'topic_1'
PORT = 443

#Create an MQTT client
mqttc = AWSIoTMQTTClient(CLIENT_ID)
mqttc.configureEndpoint(ENDPOINT,PORT)
#Create credentials by locating your certificates and private key
mqttc.configureCredentials("./certs/Amazon-root-CA-1.pem","./certs/private.pem.key","./certs/device.pem.crt")

mqttc.configureAutoReconnectBackoffTime(1, 32, 20)
mqttc.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
mqttc.configureDrainingFrequency(2)  # Draining: 2 Hz
mqttc.configureConnectDisconnectTimeout(10)  # 10 sec
mqttc.configureMQTTOperationTimeout(5) 

def on_message_received(client, userdata, message):
    print("received message")
    print(message.payload)

#Connect to the MQTT broker
try:
    mqttc.connect()
    print("AWS IoT Core Connected")
except Exception as e:
    print(f"Failed to connect to AWS IoT Core: {e}")
    exit()  # Terminate the script if connection fails

i=0
#while(mqttc.connect()==0):
#    print("retry '{}'",i)
#    i=i+1
#    if(i>10):
#        break
    

for i in range(24 * 60):
    if i % 12 == 0:  # Print every 12 iterations, which corresponds to every 1 minute  
        try:
            mqttc.subscribe(TOPIC,mqtt.QoS.AT_LEAST_ONCE,on_message_received)
            print("subscriebe")
        except Exception as e:
            print(f"Failed to subscribe: {e}")
            exit()
    time.sleep(5)
mqttc.disconnect()                
