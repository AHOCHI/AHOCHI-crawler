from scrapy.item import Item, Field


class LocationCrawlerItem(Item):
    url = Field()
    page_title = Field()
    city = Field()
    state = Field()
    zip = Field()
    keyword = Field()
