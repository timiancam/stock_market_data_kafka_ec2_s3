# Stock Market Data - Kafka, EC2, S3

## 1. Poetry Installation Instructions

https://python-poetry.org/docs/#installation

## 2. AWS Command Line Interfaction Installation

https://aws.amazon.com/cli/

## 3. EC2 Setup

### 3.1. Zookeeper Server

1. Login in to AWS and select a region.
2. Launch an EC2 instance.
    * AMI: Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type.
    * Instance Type: t2.micro.
    * Create a key pair (RSA, .pem) (Store the .pem in your local directory).
3. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient).
    * First run: `chmod 400 key_name.pem`.
4. `wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz`.
5. `tar -xvf kafka_2.12-3.3.1.tgz`.
6. `sudo yum install java-1.8.0-openjdk`.
7. `cd kafka_2.12-3.3.1/`.
8. `sudo nano config/server.properties`.
9. Remove the `#` from `#advertised.listeners=PLAINTEXT://your.host.name:9092`
10. Replace `your.host.name` with the public IPv4 address of the ec2 machine `65.2.168.105:9092`. 
11. `control-x`, `y`.
12. `bin/zookeeper-server-start.sh config/zookeeper.properties`.
13. The Zookeeper server is now running. 

### 3.2. Kafka Server

1. Create a new terminal window, ensure the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient).
3. `export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"`.
4. `cd kafka_2.12-3.3.1/`.
5. `bin/kafka-server-start.sh config/server.properties`.
6. The Kafka server is now running.
7. Edit the EC2 instance's security groups inbound rules.
    * `Add rule`.
    * Type - All Traffic.
    * Source - Anywhere-IPv4.
    * `Save rules`.

### 3.3. Create a Topic

1. Create a new terminal window, ensuring the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient)
3. `cd kafka_2.12-3.3.1/`.
4. `bin/kafka-topics.sh --create --topic demo_test --bootstrap-server ec2_public_ipv4_address:9092 --replication-factor 1 --partitions 1`.

### 3.4. Create a Producer

1. `bin/kafka-console-producer.sh --topic demo_test --bootstrap-server ec2_public_ipv4_address:9092`.

### 3.5. Create a Consumer

1. Create a new terminal window, ensuring the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient)
3. `cd kafka_2.12-3.3.1/`.
4. `bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server ec2_ublic_ipv4_address:9092`.
5. You can now type within the producer shell and it will be outputted to the consumer shell.

## 4. S3 Setup

1. Login in to AWS and select a region.
2. [Create an S3 bucket.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
    * Bucket name: kafka-stock-market-demo
    * AWS Region: _Closest to you_

## 5. Athena Crawler/Glue Setup
1. Go to AWS Glue.
2. Go to Crawlers.
3. Create Crawler.
    * Name: stock_market_kafka_crawler
    * Is your data already mapped to Glue tables?: Not yet
    * Add data source:
        * Location of S3 data: In this account
        * S3 path: kafka-stock-market-demo
4. `Add an S3 data source`.
5. Select an IAM role.
6. `Next`.
7. `Add database`. 
    * Name: stock-market-kafka-database.
8. Select the newly created database.
9. `Next`. 
10. `Create Crawler`. 
11. Select the crawler and press `Run`. 

## Python Setup

1. create a kafka producer
2. create a kafka consumer
3. pip install kafka-python==2.02
    * pandas

## 6. Usage Instructions
1. Setup the data environment as per above.

## 7. To do:

* Add doc-strings / comments.
* Finalize repository metadeta and settings.
* Check LICENSE.
* Final check.
* Repository metadata.
* Update .toml.
* Removal of personal pronouns and use professional language.
* Numbered headings

## Temporary Notes 1:

* Video: https://www.youtube.com/watch?v=KerNf0NANMo
* Jupyter Notebook start: 31:40
* Stock market data simulation start: 37:40
* S3 Bucket data upload: 45:20
* Athena, crawler video start: 52:36
* IAM role setup: 55:00
* Current time in video: 