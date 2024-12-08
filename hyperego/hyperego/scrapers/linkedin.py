from .scraper_interface import Scraper, ScrapeResult
from apify_client import ApifyClient

class LinkedinScraper(Scraper):
    def __init__(self):
        self.lins = ApifyClient
        self.apify_client = ApifyClient("getyourown")

    def get_source(self):
        return "linkedin"

    def scrape(self, query, max_results):
        run_input = {
        "urls": [
            query
        ],
        "limitPerSource":max_results,
        "deepScrape": True,
        "rawData": False,
        "minDelay": 2,
        "maxDelay": 5,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyCountry": "US",
        },
        }

        run = self.apify_client.actor("kfiWbq3boy3dWKbiL").call(run_input=run_input)
        return self.pretty_print(self.apify_client.dataset(run["defaultDatasetId"]))


    def pretty_print(self, data):
        result_list = []

        for f in data.iterate_items():
            result={"source":"Linkedin"}
            if f["isRepost"]:
                continue
            result["content"]=f["text"]

            if "type" in f:
                if(f["type"]=="image"):
                    result["image"]=f["images"][0]
                else:
                    result["image"]=None
            else:
                result["image"]=None

            result["url"]=f["url"]

            result_list.append(ScrapeResult(result["source"], result["url"], "No title", result["content"], result["image"]))

        return result_list