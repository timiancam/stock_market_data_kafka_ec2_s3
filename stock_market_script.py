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
# run the servers for 10 seconds
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

def main():
    data = get_csv_data()
    
    thread_producer = Thread(target=create_producer)
    thread_consumer = Thread(target=create_consumer)
    
    thread_producer.daemon = True
    thread_consumer.daemon = True
    
    thread_producer.start()
    thread_consumer.start()
    
    sleep(RUN_TIME)
        
main()

# read the data
# create the producer
# create the consumer
# for 11 seconds, the consumer needs to recieve data
# for 10 seconds the producer needs to send data 
    # producer.send in a while True loop
    # for loop with consumer