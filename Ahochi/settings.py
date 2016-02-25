# Scrapy settings for location_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html

BOT_NAME = 'location_crawler'
SPIDER_MODULES = ['Ahochi.spiders']
NEWSPIDER_MODULE = 'Ahochi.spiders'
DEFAULT_ITEM_CLASS = 'Ahochi.items.LocationCrawlerItem'

#To stop it from getting stuck on an infinite loop
DEPTH_LIMIT = 64 
