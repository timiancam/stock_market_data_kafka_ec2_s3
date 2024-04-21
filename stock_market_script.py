"""

"""

import pandas as pd
from kafka import KafkaProducer
from kafka import KafkaConsumer
import time
from time import sleep
from threading import Thread
from json import dumps, loads
import json
from s3fs import S3FileSystem

# put error catching message for the producer and consumer
# if the connection to the ec2 instance didn't work

# pandas read the .csv
# create the producer server
# create the consumer server
# run the server for 10 seconds
# producer flush the data from the kafka server
# stop the producer and consumer server
# Thank you for running the script

# unit = seconds
RUN_TIME = 10
BOOTSTRAP_SERVERS = ''

def get_csv_data():
    return pd.read_csv('simulated_raw_data.csv')

def create_producer():
    return KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVERS],
                         value_serializer=lambda x: dumps(x).encode('utf-8')
                        )
    
def create_consumer():
    return KafkaConsumer('demo_test',
                         bootstrap_servers=[BOOTSTRAP_SERVERS],
                         value_serializer=lambda x: loads(x.decode('utf-8'))
                         )

def send_data(x):
    while True:
        print(x)
        print('send_data')
        x += 1
        sleep(1)

def receive_data():
    while True:
        print('receive_data\n')
        sleep(1)

def main():
    data = get_csv_data()
    
    #producer = create_producer()
    #consumer = create_consumer()
    
    t1 = Thread(target=send_data(0))
    t2 = Thread(target=receive_data())
    
    t1.daemon = True
    t2.daemon = True
    
    t1.start()
    t2.start()
    
    sleep(RUN_TIME)
        
main()