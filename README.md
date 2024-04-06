# Heading

## Poetry Installation Instructions

https://python-poetry.org/docs/#installation

## EC2 Setup

### Zookeeper Server

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

### Kafka Server

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

### Create a Topic

1. Create a new terminal window, ensuring the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient)
3. `cd kafka_2.12-3.3.1/`.
4. `bin/kafka-topics.sh --create --topic demo_test --bootstrap-server ec2_public_ipv4_address:9092 --replication-factor 1 --partitions 1`.

### Create a Producer

1. `bin/kafka-console-producer.sh --topic demo_test --bootstrap-server ec2_public_ipv4_address:9092`.

### Create a Consumer

1. Create a new terminal window, ensuring the working directory contains the .pem file.
2. [SSH client connect to the EC2 instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html#connect-linux-inst-sshClient)
3. `cd kafka_2.12-3.3.1/`.
4. `bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server ec2_ublic_ipv4_address:9092`.
5. You can now type within the producer shell and it will be outputted to the consumer shell.

## Python Setup

1. create a kafka producer
2. create a kafka consumer
3. pip install kafka-python==2.02
    * pandas

## Usage Instructions
1. Setup the data environment as per above.

## To do:

* Add doc-strings / comments.
* Finalize repository metadeta and settings.
* Check LICENSE.
* Final check.
* Repository metadata.
* Update .toml.
* Removal of personal pronouns and use professional language.

## Temporary Notes 1:

* Video: https://www.youtube.com/watch?v=KerNf0NANMo
* Jupyter Notebook start: 31:40
* Stock market data simulation start: 37:40
* Current time in video: 43:22