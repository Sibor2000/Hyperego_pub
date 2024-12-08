from dataclasses import dataclass
import logging
import sys
from typing import Optional
import asyncio
import uuid
from hyperego.ai import ImageCaptioner, PostAnalyzer

from hyperego.scrapers import ScrapeResult, Scraper, LinkedinScraper, FacebookScraper, InstagramScraper

@dataclass
class HyperegoRunConfig:
    name: str
    age: int
    profession: str
    email: Optional[str] = None
    location: Optional[str] = None

    instagram: Optional[str] = None
    facebook: Optional[str] = None
    linkedin: Optional[str] = None

    def validate(self):
        if not self.instagram and not self.facebook and not self.linkedin:
            raise ValueError("At least one social media source must be provided")

        if self.instagram and not self.instagram.startswith("https://www.instagram.com/"):
            raise ValueError("Instagram URL must start with 'https://www.instagram.com/'")

        if self.facebook and not self.facebook.startswith("https://www.facebook.com/"):
            raise ValueError("Facebook URL must start with 'https://www.facebook.com/'")

        if self.linkedin and not self.linkedin.startswith("https://www.linkedin.com/"):
            raise ValueError("LinkedIn URL must start with 'https://www.linkedin.com/'")

        if self.name == "":
            raise ValueError("Name must be provided")
        
        if not 18 <= self.age <= 120:
            raise ValueError("Age must be between 18 and 120")

        if self.profession == "":
            raise ValueError("Profession must be provided")
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "profession": self.profession,
            "email": self.email,
            "location": self.location,
            "instagram": self.instagram,
            "facebook": self.facebook,
            "linkedin": self.linkedin,
        }

class HyperegoRun:
    def __init__(self, config: HyperegoRunConfig, progress_callback=None):
        self.config = config
        self.progress_callback = progress_callback
        self.logger = logging.getLogger("hyperego")
        self.logger.setLevel(logging.DEBUG)
        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger.info("HyperegoCore initialized")

    def progress(self, message):
        self.logger.debug("Progress: %s", message)
        if self.progress_callback:
            self.progress_callback(message)

    async def scraping_task(self, query: str,  scraper: Scraper, queue: asyncio.Queue):
        source = scraper.get_source()

        self.logger.info("Scraping %s", source)
        posts = scraper.scrape(query, 3)

        for post in posts:
            post_dict = post.to_dict()
            post_dict["id"] = str(uuid.uuid4())
            self.logger.info("Scraped post: %s", post_dict["id"])
            await queue.put(post_dict)
            self.progress({"status": "scraped", "source": source, "post": post_dict})

    async def fake_scraping_task(self, source: str, queue: asyncio.Queue):
        posts = [
            # ScrapeResult(
            #     source=source,
            #     url=f"https://www.{source}.com/p/1234",
            #     title="Happy Birthday",
            #     content="Happy birthday to my best friend! I hope you have a great day, Becky!",
            # ),
            ScrapeResult(
                source=source,
                url=f"https://www.{source}.com/p/5678",
                title="Uwu",
                content="0mg we got so waaasteeeeeeeeeeeeed last night! #girlsnightout #party #drunkashell",
                image="https://d28mt5n9lkji5m.cloudfront.net/i/XS_Oey1sQgi.jpg",
            ),
            ScrapeResult(
                source=source,
                url=f"https://www.{source}.com/p/91011",
                title="New Job",
                content="I'm so excited to announce that I've accepted a new job at XYZ Corp! From now on, I'll be working as a corporate attorney.",
            ),
        ]

        self.logger.info("Scraping Instagram")
        for post in posts:
            post_dict = post.to_dict()
            post_dict["id"] = str(uuid.uuid4())
            self.logger.info("Scraped post: %s", post_dict["id"])
            await queue.put(post_dict)
            self.progress({"status": "scraped", "source": source, "post": post_dict})
            await asyncio.sleep(3)

    async def image_analysis_task(self, input_queue: asyncio.Queue, next_queue: asyncio.Queue):
        try:
            self.logger.info("Starting image analysis task")
            model = ImageCaptioner()

            while True:
                post = await input_queue.get()
                if post.get("image"):
                    self.logger.info("Analyzing image for post: %s", post["id"])
                    caption = model.label(post["image"])
                    self.logger.debug("Image caption: %s", caption)
                    post["image"] = caption
                else:
                    self.logger.info("No image to analyze for post: %s", post["id"])
                await next_queue.put(post)
                input_queue.task_done()
        except Exception as e:
            self.logger.error("Error analyzing image: %s", e)
    
    async def post_analysis_task(self, input_queue: asyncio.Queue, result_queue: asyncio.Queue):
        try:
            self.logger.info("Starting post analysis task")
            judge = PostAnalyzer()

            while True:
                post = await input_queue.get()
                self.logger.info("Analyzing post: %s", post["id"])
                data = judge.analyze({
                    "personal": {
                        "name": self.config.name,
                        "age": self.config.age,
                        "profession": self.config.profession,
                        "location": self.config.location,
                    },
                    "post": post
                })
                self.logger.debug("Post analysis: %s", data)
                data_dict = data.model_dump(mode='json')
                data_dict["id"] = post["id"]
                result_queue.put_nowait(data_dict)
                input_queue.task_done()
        except Exception as e:
            self.logger.error("Error analyzing post: %s", e)

    async def collect_results(self, results, result_queue: asyncio.Queue):
        results.clear()
        while True:
            result = await result_queue.get()
            results.append(result)
            self.progress({"status": "result", "result": result})
            result_queue.task_done()

    async def run(self):
        self.logger.info("Starting Hyperego run for %s", self.config.name)
        await asyncio.sleep(6)
        self.progress({"status": "started"})

        scrape_queue = asyncio.Queue()
        image_analysis_queue = asyncio.Queue()
        post_analysis_queue = asyncio.Queue()

        # Start scraping
        scraping_tasks = []
        if self.config.instagram:
            scraping_tasks.append(asyncio.create_task(self.scraping_task(
                self.config.instagram,
                InstagramScraper(),
                scrape_queue
            )))
        if self.config.facebook:
            scraping_tasks.append(asyncio.create_task(self.scraping_task(
                self.config.facebook,
                FacebookScraper(),
                scrape_queue
            )))
        if self.config.linkedin:
            scraping_tasks.append(asyncio.create_task(self.scraping_task(
                self.config.linkedin,
                LinkedinScraper(),
                scrape_queue
            )))
        
        # Start image analysis
        image_analysis_task = asyncio.create_task(self.image_analysis_task(scrape_queue, image_analysis_queue))

        # Start post analysis
        post_analysis_task = asyncio.create_task(self.post_analysis_task(image_analysis_queue, post_analysis_queue))

        # Start collecting results
        results = []
        results_task = asyncio.create_task(self.collect_results(results, post_analysis_queue))

        # Wait for all scraping tasks to finish
        await asyncio.gather(*scraping_tasks)
        self.logger.info("Scraping tasks finished")

        # Wait for the queues to finish
        await scrape_queue.join()
        await image_analysis_queue.join()
        await post_analysis_queue.join()
        self.logger.debug("Queues finished")

        # Cancel the running tasks
        for task in scraping_tasks:
            task.cancel()
        image_analysis_task.cancel()
        post_analysis_task.cancel()
        results_task.cancel()

        self.progress({"status": "finished"})
        self.logger.info("Hyperego run finished")

        return results