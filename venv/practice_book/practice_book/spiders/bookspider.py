import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            yield{
                'name' : book.css('h3 a::attr(title)').get(),
                'price' :book.css('.product_price .price_color::text').get(),
                'url' : book.css('h3 a::attr(href)').get(),
            }
        
        next_page = response.css('li.next a ::attr(href)').get()

        if next_page is not None:
            next_page_url = 'https://books.toscrape.com/' + next_page
