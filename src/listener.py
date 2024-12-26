import logging

from bus_queue import EventBus
from bus_queue.backend.rabbit.bus import RabbitEventBus as Bus

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

for l in ['pika', ]:
    logging.getLogger(l).setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def callback(topic, msg):
    logger.info(f"Received: topic: {topic} msg: {msg}")


def main():
    backend = Bus("amqp://guest:guest@localhost:5672/")
    bus = EventBus(backend)

    bus.subscribe("test", callback)
    bus.wait()


if __name__ == "__main__":
    main()
