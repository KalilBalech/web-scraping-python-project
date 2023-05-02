import scrapy
from bookscraper.items import BookscraperItem 

# run spider - scrapy crawl [FILE NAME]
# scrapy crawl bookspider

# run spider and save result in a csv file - scrapy crawl [FILE NAME] -O [CSV FILE NAME]
# scrapy crawl bookspider -O bookspider.csv

# run spider and save result in a json file - scrapy crawl [FILE NAME] -O [JSON FILE NAME]
# scrapy crawl bookspider -O bookspider.json

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')
        book_item = BookscraperItem()
        for book in books:
            book_item['name'] = book.css('h3 a::text').get(), # we can remove, if exists, any commas in the title, so we can easily separate the fields in a csv file in excel
            book_item['price'] = book.css('div.product_price p.price_color::text').get(), # we can exchange the currency if convenient
            book_item['url'] = books.css('h3 a').attrib['href']
            yield book_item
        
        nextLink = response.css('li.next a').attrib['href']
        if nextLink is not None:
            if 'catalogue' in nextLink:
                nextLink = 'https://books.toscrape.com/' + nextLink
            else:
                nextLink = 'https://books.toscrape.com/' + 'catalogue/' + nextLink
        
            yield response.follow(nextLink, callback = self.parse) # vai pro link nextLink e chama self.parse com response nessa url atual