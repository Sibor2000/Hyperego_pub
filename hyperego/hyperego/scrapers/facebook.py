from .scraper_interface import Scraper, ScrapeResult
from apify_client import ApifyClient

class FacebookScraper(Scraper):
    def __init__(self):
        self.instas = ApifyClient
        self.apify_client = ApifyClient("getyourown")

    def get_source(self):
        return "facebook"

    def scrape(self, query, max_results):
        run_input = {
            "urls": [{
                "url": query,
                "method": "GET"
            }],
            "max_posts": max_results,
            "max_retries": 5,
            "proxy": {"useApifyProxy": True,
                "apifyProxyGroups": [
                "RESIDENTIAL"
                ],
                "apifyProxyCountry": "HU",
            }
        }

        run = self.apify_client.actor("OkuDbWbIxkgSRhppo").call(run_input=run_input)

        data = []
        for item in self.apify_client.dataset(run["defaultDatasetId"]).iterate_items():
            image = None
            if item.get("image", None) is not None:
                image = item["image"]["uri"]
            data.append(ScrapeResult(
                source="facebook",
                url=item["url"],
                content=item["message"],
                image=image,
                title="<not supported>"
            ))
        return data