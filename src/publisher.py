import logging

from bus_queue.backend.rabbit.bus import RabbitEventBus as Bus
from bus_queue import EventBus

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

for l in ['pika',]:
    logging.getLogger(l).setLevel(logging. WARNING)

logger = logging.getLogger(__name__)


def main():
    backend = Bus("amqp://guest:guest@localhost:5672/")
    bus = EventBus(backend)

    bus.publish("test", dict(hola="Gonzalo"))
    bus.broadcast("test", "Hola, broadcast")


if __name__ == "__main__":
    main()
