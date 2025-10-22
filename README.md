# Kafka Producer-Consumer Example

A simple example demonstrating Apache Kafka's producer-consumer pattern using Docker and Python. This project shows how to set up Kafka locally and implement basic event streaming with an order management system.

## Prerequisites

- Docker and Docker Compose installed
- Python 3.x installed
- `confluent-kafka` Python library

## Installation

1. Install the required Python package:
```bash
pip install -r requirements.txt
```

2. Start Kafka using Docker Compose:
```bash
docker compose up
```

## Project Structure

```
.
├── docker-compose.yaml   # Kafka configuration
├── producer.py           # Produces order events
├── tracker.py            # Consumes order events
├── requirements.txt      # Python packages
└── README.md
```

## Usage

### Start Kafka
```bash
docker compose up
```

### Run the Consumer (Terminal 1)
```bash
python3 tracker.py
```
The consumer will listen for incoming order events.

### Run the Producer (Terminal 2)
```bash
python3 producer.py
```
The producer will send an order event to Kafka.

## How It Works

1. **Producer** creates an order object and publishes it to the `orders` topic
2. **Kafka** stores the message and makes it available to consumers
3. **Consumer** reads the message from the `orders` topic and processes it

## Configuration

- **Kafka Broker**: `localhost:9092`
- **Topic**: `orders`
- **Consumer Group**: `order-tracker`

## Stopping Kafka

To stop and remove containers:
```bash
docker compose down
```

To also remove the Kafka volume:
```bash
docker compose down -v
```

## Learn More

Check out the full tutorial: [Getting Started with Kafka: A Practical Guide](https://kafka-python.hashnode.dev/kafka-tutorial-build-your-first-producer-and-consumer-with-python)