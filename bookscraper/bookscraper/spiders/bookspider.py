import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        categories = response.css('ul.nav.nav-list li ul li a')

        for category in categories:
            category_page = category.css('a::attr(href)').get()
            category_url = 'https://books.toscrape.com/' + category_page
            yield response.follow(category_url, callback=self.parse_category_page)

    def parse_category_page(self, response):
        yield {
            'category' : response.css('div.page-header.action h1::text').get(),
            'qty_books' : response.xpath("//form[@class='form-horizontal']/strong[1]/text()").get(),
        }
