import logging
from hyperego.core import HyperegoRun, HyperegoRunConfig
import asyncio

Logger = logging.getLogger(__name__)

def test_hyperego_run():
    config = HyperegoRunConfig(
        name="Laura Wasser",
        age=52,
        profession="Family Law Attorney",
        email="lauraw4sser@gmail.com",
        location="Los Angeles, CA",

        instagram="https://www.instagram.com/laurawasserofficial",
    )

    run = HyperegoRun(config)
    asyncio.run(run.run())

    assert False, "Test failed"