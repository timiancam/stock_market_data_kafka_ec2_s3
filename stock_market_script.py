"""
Creates a Kafka producer and consumer.
The producer simulates sending random market data, reading from a .csv file
The consumer uploads the sent data to a S3 bucket in the .json format
"""

import pandas as pd
from kafka import KafkaProducer
from kafka import KafkaConsumer
from time import sleep
from threading import Thread
from json import dumps, loads
import json
from s3fs import S3FileSystem

RUN_TIME = 20 # Unit = seconds
BOOTSTRAP_SERVERS = 'EC2_IPv4_public_address:9092' 

def get_csv_data():
    return pd.read_csv('simulated_raw_data.csv')

def create_producer():
    return KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVERS], value_serializer=lambda x: dumps(x).encode('utf-8'))
    
def create_consumer():
    return KafkaConsumer('demo_test', bootstrap_servers=[BOOTSTRAP_SERVERS], value_deserializer=lambda x: loads(x.decode('utf-8')))

def send_data(producer, data):
   # Simulates sending random data to the consumer
   
    while True:
        data_entry = data.sample(1).to_dict(orient='records')[0]
        producer.send('demo_test', value=data_entry)
        sleep(1) # EC2 instance unable to handle data rate
    
def receive_data(consumer):
    s3_address = 's3://s3_url_address/stock_market_{}.json' # Input your S3 address
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
    
    print('Your data has been uploaded to the S3 bucket!')
        
main()