mkdir ~/certs/test_mqtt
aws iot create-keys-and-certificate \
--set-as-active \
--certificate-pem-outfile "~/certs/test_mqtt/device.pem.crt" \
--public-key-outfile "~/certs/test_mqtt/public.pem.key" \
--private-key-outfile "~/certs/test_mqtt/private.pem.key"

"endpointAddress": "a2fohdr218kpa4-ats.iot.ap-northeast-1.amazonaws.com"
"certificateArn": "arn:aws:iot:ap-northeast-1:153506519627:cert/bf8a7feb7b96b55d2baf936ca6d6e129fb86cb2a1499ccd91c7c1f71f75ab778"

test_mqtt
"certificateArn": "arn:aws:iot:ap-northeast-1:153506519627:cert/777e96a84e4ec49b92765a9a40969567a714bcc5bea6e3b61cfa3b810a1016e8"

chmod 745 ~
chmod 700 ~/certs/test_mqtt
chmod 644 ~/certs/test_mqtt/*
chmod 600 ~/certs/test_mqtt/private.pem.key

ls -l ~/certs/test_mqtt

aws iot create-thing --thing-name "MoistSensorTestThing"

-정책 생성
nano sensor_test_thing_policy.json
"
"Effect": "Allow",
         "Action": "iot:Publish",
         "Resource": [
            "arn:aws:iot:region:account:topic/$aws/things/RaspberryPi/shadow/get"
         ]
"

aws iot create-policy \
--policy-name "MoistureSensorPolicy" \
--policy-document "file://~/policies/sensor_test_thing_policy.json"


-certificate연결
aws iot attach-policy \
--policy-name "TestDevice1Policy" \
--target  "arn:aws:iot:ap-northeast-1:153506519627:cert/777e96a84e4ec49b92765a9a40969567a714bcc5bea6e3b61cfa3b810a1016e8"

pip3 install awsiotpythonsdk 


--endpoint a2fohdr218kpa4-ats.iot.ap-northeast-1.amazonaws.com

python3 pubsub.py \
--endpoint tf4a9d0ac3t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com \
--rootCA ~/certs/AmazonRootCA1.pem \
--cert ~/certs/test_mqtt/device.pem.crt \
--key ~/certs/test_mqtt/private.pem.key \
--thingName TestDevice1Thing \
--clientId TestDevice1


--endpoint t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com \

python3 pubsub.py \
--endpoint tf4a9d0ac3t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com \
--cert ~/certs/test_mqtt/device.pem.crt \
--key ~/certs/test_mqtt/private.pem.key \

--ca_file ~/certs/AmazonRootCA1.pem \
--client_id TestDevice1 


aws iotdeviceadvisor get-endpoint --certificate-arn arn:aws:iot:ap-northeast-1:153506519627:cert/7a0c44ffc2c93fcfa98c3ea492754b6682caab6efc86a97ab460fa279d02e4d2

deviceadvisor endpoint
"endpoint": "ta5b22a879t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com"

ta5b22a879t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com



python3 pubsub.py \
--endpoint tf4a9d0ac3t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com \
--cert ~/certs/test_mqtt/device.pem.crt \
--key ~/certs/test_mqtt/private.pem.key \
--ca_file ~/certs/AmazonRootCA1.pem 


python3 pubsub.py \
--endpoint a2fohdr218kpa4-ats.iot.ap-northeast-1.amazonaws.com \
--cert ~/certs/test_mqtt/device.pem.crt \
--key ~/certs/test_mqtt/private.pem.key \
--ca_file ~/certs/AmazonRootCA1.pem 



python3 pubsub.py --topic topic_1 --ca_file ~/certs/AmazonRootCA1.pem  --cert ~/certs/test_mqtt/device.pem.crt --key ~/certs/test_mqtt/private.pem.key --endpoint t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com

python3 pubsub.py --topic topic_1 --ca_file ~/certs/Amazon-root-CA-1.pem --cert ~/certs/device.pem.crt --key ~/certs/private.pem.key --endpoint a2fohdr218kpa4-ats.iot.ap-northeast-1.amazonaws.com

python pubsub.py --topic topic_1 --ca_file ~/certs/Amazon-root-CA-1.pem --cert ~/certs/device.pem.crt --key ~/certs/private.pem.key --endpoint t9f2ce41b3t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com


python pubsub.py --topic topic_1 --ca_file ~/certs/Amazon-root-CA-1.pem --cert ~/certs/device.pem.crt --key ~/certs/private.pem.key --endpoint a2fohdr218kpa4-ats.iot.ap-northeast-1.amazonaws.com

python ~/conn_t*/*v2/samples/pubsub.py --ca_file ~/certs/Amazon-root-CA-1.pem --cert ~/certs/device.pem.crt --key ~/certs/private.pem.key --endpoint  t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com --client_id eviot --topic topic_1


ping  t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com

python ~/conn_t*/*v2/samples/pubsub.py --ca_file ~/certs/Amazon-root-CA-1.pem --cert ~/certs/device.pem.crt --key ~/certs/private.pem.key --endpoint  t3fouod00d8aka.deviceadvisor.iot.ap-northeast-1.amazonaws.com --client_id eviot --topic topic_1 --count 1000000


mqttc.configureAutoReconnectBackoffTime(1, 32, 20)
mqttc.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
mqttc.configureDrainingFrequency(2)  # Draining: 2 Hz
mqttc.configureConnectDisconnectTimeout(10)  # 10 sec
mqttc.configureMQTTOperationTimeout(5) 
