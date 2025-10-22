import json
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])

print("Consumer Is Running & Subscribed To Orders")

try:
    while True:
        msg = consumer.poll(5.0)
        if msg is None:
            continue
        if msg.error():
            print("Error Reading Msg : {msg.error()}")
            continue
        if msg is not None:
            order_bytes = msg.value().decode("utf-8")
            order = json.loads(order_bytes)
            print(
                f"Received Order From {order["user"]} : {order["item"]} Of Quantity {order["quantity"]}"
            )

except KeyboardInterrupt:
    print("Shutting Down Tracker")
finally:
    consumer.close()
