import json
import uuid
from confluent_kafka import Producer

producer_config = {"bootstrap.servers": "localhost:9092"}

producer = Producer(producer_config)

order = {
    "order_id": str(uuid.uuid4()),
    "user": "Sheldor",
    "item": "Chicken Burger",
    "quantity": 1,
}

order_bytes = json.dumps(order).encode("utf-8")


def delivery_report(err, msg):
    if err:
        print(f"Delivery Failed : {err}")
    else:
        print(f"Delivery Success : {msg.value().decode("utf-8")}")
        print(f"Delivered to {msg.topic()} : {msg.partition()} : {msg.offset()}")


producer.produce(topic="orders", value=order_bytes, callback=delivery_report)

producer.flush()
