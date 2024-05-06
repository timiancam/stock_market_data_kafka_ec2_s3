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

RUN_TIME = 20 # Unit = seconds
BOOTSTRAP_SERVERS = ':9092' # EC2 instance public IPv4 address

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

def send_data(producer, data):
   # Simulates sending random data to the consumer
   
    while True:
        data_entry = data.sample(1).to_dict(orient='records')[0]
        producer.send('demo_test', value=data_entry)
        sleep(1) # EC2 instance unable to handle data rate
    
def receive_data(consumer):
    s3_address = ''
    s3 = S3FileSystem()
    
    for count, i in enumerate(consumer):
        with s3.open(s3_address.format(count), 'w') as file:
            json.dump(i.value, file)

def main():
    data = get_csv_data()
    
    producer = create_producer()
    consumer = create_consumer()
    
    receive_data_thread = Thread(target=receive_data,args=[consumer])
    send_data_thread = Thread(target=send_data,args=[producer, data])
    
    receive_data_thread.daemon = True
    send_data_thread.daemon = True
    
    receive_data_thread.start()
    send_data_thread.start()
    
    sleep(RUN_TIME)
    
    print('Misdata managed!')
        
main()