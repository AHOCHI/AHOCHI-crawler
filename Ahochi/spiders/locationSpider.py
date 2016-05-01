from scrapy.spiders import Spider
from scrapy.selector import Selector
from google import search
from Ahochi.items import LocationCrawlerItem
from Ahochi.geographic_info import GeographicInfo
import usaddress
import re
import html2text

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

class LocationSpider(Spider):
    # name of the spider
    name = "location"

    # imports lists of data from GeographicInfo
    cities = GeographicInfo().get_cities()
    zip_codes = GeographicInfo().get_zips()
    keywordList = GeographicInfo().make_keywords()

    # uses google to search the string
    gsearch = search('boone county ky social services', stop=20)

    # builds an list of URLs from google search
    url_array = []
    for url in gsearch:
        url_array.append(url)

    # creates an array filled with the google result pages for the spider to start searching
    start_urls = url_array

    def parse(self, response):
        # Sets up selectors to search the google search pages for titles and urls
        sel = Selector(response)
        title = sel.xpath('//title/text()')
        sites = sel.xpath('//*/text()')
        # Creates a list to hold objects
        items = []

        # saves a regex statement searching for specific zip codes to a variable
        nky_zip_regex = re.compile(r'\b(' + '|'.join(LocationSpider.zip_codes) + r')', re.IGNORECASE)

        # LANGUAGE = "english"
        # SENTENCES_COUNT = 10
        # parser = HtmlParser.from_string(response.body, self.url, Tokenizer(LANGUAGE))
        # stemmer = Stemmer(LANGUAGE)
        # summarizer = Summarizer(stemmer)
        # summarizer.stop_words = get_stop_words(LANGUAGE)
        #
        # for sentence in summarizer(parser.document, SENTENCES_COUNT):
        #     print(sentence)

        # goes through a loop looking at each url found on google results
        for current in sites:
            # creates an object to store items
            item = LocationCrawlerItem()
            # looks for sites with specific zip codes
            zip_string = re.search(nky_zip_regex, current.extract())

            # print html2text.html2text(response.body)

            # Creates a regex statement stored as a variable and uses it
            keyword_regex = re.compile(r'\b(' + '|'.join(LocationSpider.keywordList) + r')', re.IGNORECASE)
            keyword_string = re.search(keyword_regex, current.extract())

            # For debugging
            # print keyword_regex.pattern
            # print keyword_string.group

            # If it finds a keyword, it stores it as a keyword in the item object
            if keyword_string:
                item["keyword"] = keyword_string.group()
                item["page_title"] = title.extract()
                item["url"] = response.request.url
                items.append(item)
            else:
                item["keyword"] = "nothing"

            # this loops looks and stores data if it finds a zip code
            if zip_string:
                # stores the URL, page title and zip code items into item object
                item["url"] = response.request.url
                item["page_title"] = title.extract()
                item["zip"] = zip_string.group()

                # saves a regex statement looking for states or state abbreviations to a variable
                state_abb_regex = re.compile(r'\bky[.,]? ', re.IGNORECASE)
                state_proper_regex = re.compile(r'\bkentucky ', re.IGNORECASE)

                # looks for state name or state abbreviation
                state_abb_string = re.search(state_abb_regex, current.extract())
                state_proper_string = re.search(state_proper_regex, current.extract())

                # if it finds a state abbreviation, it stores it as state in the item object
                if state_abb_string:
                    item["state"] = "Ky"
                    # print (item["state"])
                    temp_address_str = state_abb_string.group()
                    # print temp_address_str
                # if it finds a state name, it stores as state in the item object
                elif state_proper_string:
                    item["state"] = "Kentucky"
                    # print (item["state"])
                    temp_address_str = state_proper_string.group()
                    # print temp_address_str
                # if it doesn't find either it stores the state field with "none"
                else:
                    item["state"] = None
                    temp_address_str = None

                city_string = None
                if temp_address_str:
                    # saves a regex statement looking for cities to a variable and then runs it
                    city_regex = re.compile(
                        r'\b('
                        + '|'.join(LocationSpider.cities)
                        + '[,]? '
                        + re.escape(temp_address_str) + r')', re.IGNORECASE)
                    city_string = re.search(city_regex, current.extract())

                # for debugging purposes
                # print city_regex.pattern
                # print city_string.group()

                # Stores the city name into the city item
                if city_string:
                    item["city"] = city_string.group()
                    # print (item["city"])
                # Stores the item object into the items list
                items.append(item)
            else:
                item["zip"] = "nothing"
        # outputs the item list
        return items
