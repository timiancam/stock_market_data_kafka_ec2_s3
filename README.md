# Stock Market Data - Kafka, EC2, S3

## 1. Poetry Installation Instructions

https://python-poetry.org/docs/#installation

## 2. AWS Command Line Interfaction Installation

https://aws.amazon.com/cli/

## 3. EC2 Kafka Setup

### 3.1. Zookeeper Server

1. Login in to AWS and select a region.
2. Launch an EC2 instance.
    * Name: kafka-stock-market-ec2
    * AMI: Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type.
    * Instance Type: t2.micro.
    * Create a key pair (RSA, .pem) (Store the .pem in your local directory).
3. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient).
    * First run: `chmod 400 key_name.pem`.
4. `wget https://downloads.apache.org/kafka/3.6.2/kafka_2.12-3.6.2.tgz`.
    * The version may no longer be available.
    * Visit https://downloads.apache.org/kafka/ if so.
    * Subsequent code will need to be updated to the latest Kafka version.
5. `tar -xvf kafka_2.12-3.6.2.tgz`.
6. `sudo yum install java-1.8.0-openjdk`.
7. `cd kafka_2.12-3.6.2/`.
8. `sudo nano config/server.properties`.
9. Remove the `#` from `#advertised.listeners=PLAINTEXT://your.host.name:9092`
10. Replace `your.host.name` with the public IPv4 address of the EC2 machine `EC2_IPv4_public_address:9092`. 
11. `control-x`, `y`, `enter`.
12. `bin/zookeeper-server-start.sh config/zookeeper.properties`.
13. The Zookeeper server is now running. 

### 3.2. Kafka Server

1. Create a new terminal window, ensure the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient).
3. `export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"`.
4. `cd kafka_2.12-3.6.2/`.
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
3. `cd kafka_2.12-3.6.2/`.
4. `bin/kafka-topics.sh --create --topic demo_test --bootstrap-server EC2_IPv4_public_address:9092 --replication-factor 1 --partitions 1`.

### 3.4. Create a Producer

1. `bin/kafka-console-producer.sh --topic demo_test --bootstrap-server EC2_IPv4_public_address:9092`.

### 3.5. Create a Consumer

1. Create a new terminal window, ensuring the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient)
3. `cd kafka_2.12-3.6.2/`.
4. `bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server EC2_IPv4_public_address:9092`.
5. You can now type within the producer shell and it will be outputted to the consumer shell.

## 4. S3 Setup

1. Login in to AWS and select a region.
2. [Create an S3 bucket.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
    * Bucket name: kafka-stock-market-s3-_your-name_
    * AWS Region: _Closest to you_
3. Go to the IAM dashboard and create a new IAM user.
4. `Add users`.
    * User name: _your name_-stock-market-data.
    * AWS credential type: Access key - Programmatic access.
    * `Attach existing policies directly`: AdminstratorAccess.
5. Download the .csv for the Access key ID and the Secret access key.
6. Open a new terminal window.
7. `aws configure`.
8. Input your Access key ID and Secret access key. 
9. Select the default region closest to you.
10. You can now send data from your local PC to the S3 bucket.

## 5. Usage Instructions
1. Setup the project as per sections 1 - 4.
2. Create a new terminal and type the following:
3. `git clone https://github.com/timiancam/stock_market_data_kafka_ec2_s3.git`.
4. `cd stock_market_data_kafka_ec2_s3`.
5. `poetry shell`. 
6. `poetry install`.
7. Edit the following lines of code in stock_market_script.py:
    * Line 17 - Bootstrap Server EC2 Public IPv4 address
    * Line 37 - S3 URL address

## 6. To do:

* Finalize repository metadeta and settings.
* Final check.
