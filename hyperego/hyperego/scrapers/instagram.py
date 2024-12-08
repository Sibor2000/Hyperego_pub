from .scraper_interface import Scraper, ScrapeResult
from apify_client import ApifyClient

class InstagramScraper(Scraper):
    def __init__(self):
        self.instas = ApifyClient
        self.apify_client = ApifyClient("getyourown")

    def scrape(self, query, max_results):
        run_input = {
            "directUrls": [query],
            "resultsType": "posts",
            "resultsLimit": max_results,
            "searchType": "hashtag",
            "searchLimit": 1,
            "addParentData": False,
        }

        run = self.apify_client.actor("RB9HEZitC8hIUXAha").call(run_input=run_input)

        return self.pretty_print(self.apify_client.dataset(run["defaultDatasetId"]))

    def pretty_print(self, data):
        result_list = []

        for f in data.iterate_items():
            result = {
                "source":"Instagram",
                "content":f["caption"],
                "type":"image",
                "url":f["url"],
            }

            if(f["type"]=="Sidecar"):
                for i in f["images"]:
                    result["image"]=i
                    result_list.append(ScrapeResult(result["source"], result["url"], "No title", result["content"], result["image"]))
                continue
            elif(f["type"]=="Image"):
                result["image"]=f["displayUrl"]
                result_list.append(ScrapeResult(result["source"], result["url"], "No title", result["content"], result["image"]))

        return result_list

    def get_source(self):
        return "instagram"
