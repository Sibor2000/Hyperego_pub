from abc import ABC, abstractmethod
import yaml
import json

class Scraper(ABC):
    @abstractmethod
    def scrape(self, query, max_results):
        """Fetch the data from the website and return the results"""
        pass

    @abstractmethod
    def get_source(self):
        """Return the source of the scraper"""
        return "unknown"

class ScrapeResult:
    def __init__(self, source, url, title, content, image=None):
        self.source = source        #Insta, linkedin, face
        self.url = url              #Post url
        self.title = title          #(OPT) title
        self.content = content      #ex. description
        self.image = image          #(OPT) link to image

    def to_yaml(self):
        return yaml.dump(self.__dict__)

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__

    def has_image(self):
        return self.image is not None
