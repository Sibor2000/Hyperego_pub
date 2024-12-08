from .scraper_interface import Scraper
from duckduckgo_search import DDGS

class DuckDuckGoScraper(Scraper):
    def __init__(self):
        self.ddgs = DDGS()

    def scrape(self, query, max_results):
        return self.ddgs.text(query, max_results=max_results)