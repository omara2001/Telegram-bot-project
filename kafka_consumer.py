from confluent_kafka import Consumer, OFFSET_BEGINNING

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka server address if necessary
    'group.id': 'telegram_bot_consumer',
    'auto.offset.reset': 'earliest',
}

kafka_consumer = Consumer(kafka_conf)
kafka_topic = 'telegram_bot_messages'

def on_assign(consumer, partitions):
    for p in partitions:
        p.offset = OFFSET_BEGINNING
    consumer.assign(partitions)

kafka_consumer.subscribe([kafka_topic], on_assign=on_assign)

try:
    while True:
        msg = kafka_consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
        else:
            print(f"Received message: {msg.key().decode('utf-8')} - {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Shutting down Kafka consumer...")
finally:
    kafka_consumer.close()
