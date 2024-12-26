import logging

from bus_queue.backend.memory.bus import MemoryEventBus as Bus
from bus_queue import EventBus

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

logger = logging.getLogger(__name__)


def callback(topic, msg):
    logger.info(f"Received: topic: {topic} msg: {msg}")


def main():
    backend = Bus()
    bus = EventBus(backend)

    bus.subscribe("test", callback)

    bus.publish("test", dict(hola="Gonzalo"))
    bus.wait()


if __name__ == "__main__":
    main()
