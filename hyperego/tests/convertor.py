#from hyperego.scrapers.linkedin import LinkedinScraper

#linkd_scraper = LinkedinScraper()

#results = linkd_scraper.scrape("https://www.linkedin.com/in/tim-loh-632a7919/",max_results=10)

#for r in results:
#    print(r.to_json())

from hyperego.scrapers.googlesearch import GoogleSearchScraper

googl_scraper = GoogleSearchScraper()

results = googl_scraper.scrape("George Simion",10)

print(results)