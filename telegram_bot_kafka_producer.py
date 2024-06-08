import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from confluent_kafka import Producer

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka server address if necessary
}

kafka_producer = Producer(kafka_conf)
kafka_topic = 'telegram_bot_messages'


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, I am your Telegram bot with Kafka integration!")


def process_message(update: Update, context: CallbackContext):
    message = update.message.text
    kafka_producer.produce(kafka_topic, key=str(update.message.chat_id), value=message)
    kafka_producer.flush()
    update.message.reply_text("Message sent to Kafka!")


def main():
    token = "6157102159:AAE1T1fvBcGif_SxlZleDxBCZuioMxECPYw"
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    updater = Updater(token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
