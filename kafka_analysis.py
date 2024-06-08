from kafka import KafkaConsumer
import matplotlib.pyplot as plt
from collections import defaultdict

# Kafka consumer configuration
bootstrap_servers = 'localhost:9092'
topic = 'telegram_bot_messages'

# Create Kafka consumer
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

# Initialize message count dictionary
message_count = defaultdict(int)

# Consume messages from Kafka
for message in consumer:
    # Increment count for each message
    message_count[message.value] += 1

    # Print the message count
    print(f'Message: {message.value}, Count: {message_count[message.value]}')

    # Visualize message count
    labels = message_count.keys()
    counts = message_count.values()

    plt.bar(labels, counts)
    plt.xlabel('Message')
    plt.ylabel('Count')
    plt.title('Kafka Message Count')
    plt.xticks(rotation=45)
    plt.show()

