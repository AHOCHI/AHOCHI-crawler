from scrapy import cmdline
import nltk;
# nltk.download('punkt')
cmdline.execute("scrapy crawl location".split())
