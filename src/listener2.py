import asyncio
import logging

from bus_queue import AsyncEventBus
from bus_queue.backend.rabbit.assync_bus import AsyncRabbitEventBus as Bus

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

for l in ['asyncio', 'aio-pika']:
    logging.getLogger(l).setLevel(logging. WARNING)

logger = logging.getLogger(__name__)


async def callback(topic, msg):
    logger.info(f"Received: topic: {topic} msg: {msg}")


async def main():
    backend = Bus("amqp://guest:guest@localhost:5672/")
    bus = AsyncEventBus(backend)

    await bus.subscribe("test", callback)
    await bus.wait()


if __name__ == "__main__":
    asyncio.run(main())
