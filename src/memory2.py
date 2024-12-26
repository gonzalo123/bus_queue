import asyncio
import logging

from bus_queue.backend.memory.assync_bus import AsyncMemoryEventBus as Bus
from bus_queue import AsyncEventBus

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

for l in ['asyncio', ]:
    logging.getLogger(l).setLevel(logging. WARNING)

logger = logging.getLogger(__name__)


async def callback(topic, msg):
    logger.info(f"Received: topic: {topic} msg: {msg}")


async def main():
    backend = Bus()
    bus = AsyncEventBus(backend)

    await bus.subscribe("test", callback)

    await bus.publish("test", dict(hola="Gonzalo"))
    await bus.wait()


if __name__ == "__main__":
    asyncio.run(main())
