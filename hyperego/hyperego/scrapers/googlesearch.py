from .scraper_interface import Scraper
from apify_client import ApifyClient

class GoogleSearchScraper(Scraper):
    def __init__(self):
        self.googs = ApifyClient
        self.apify_client= ApifyClient("getyourown")

    def get_source(self):
        return "google_search"

    def scrape(self, query, max_results):
        run_input = {
            "queries": query,
            "resultsPerPage": max_results,
            "maxPagesPerQuery": 1,
            "languageCode": "",
            "forceExactMatch": False,
            "wordsInTitle": [],
            "wordsInText": [],
            "wordsInUrl": [],
            "mobileResults": False,
            "includeUnfilteredResults": False,
            "saveHtml": False,
            "saveHtmlToKeyValueStore": True,
            "includeIcons": False,
        }

        run = self.apify_client.actor("nFJndFXA5zjCTuudP").call(run_input=run_input)

        related_querys =[]
        top_results = []

        data=[]

        for item in self.apify_client.dataset(run["defaultDatasetId"]).iterate_items():
            for rq in item["relatedQueries"]:
                related_querys.append(rq["title"])
            for orgr in item["organicResults"]:
                top_results.append({
                    "title":orgr["title"],
                    "description":orgr["description"],
                    "position":orgr["position"],
                    "url":orgr["url"]
                })
        return {"related_q":related_querys, "top_results":top_results}