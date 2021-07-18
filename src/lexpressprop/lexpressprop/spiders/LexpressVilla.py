import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import w3lib.html


class LexpressVillaSpider(scrapy.Spider):
    name = 'LexpressVilla'
    allowed_domains = ['www.lexpressproperty.com']
    start_urls = ['https://www.lexpressproperty.com/en/buy-mauritius/villa/']
    #rules = [Rule(LinkExtractor(allow = ('villa')), callback = 'parse', follow = True)]

    def parse(self, response):
        house_links = response.css('div.normal-add')
        links = [x.css('a::attr(href)')[-1].extract() for x in house_links]
        for url in links:
            print(url)
            yield scrapy.Request(url, callback=self.parse_page)

        next_page = response.css('div.pagination-block').css('a.button-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        price = response.css('div.price-box').css('strong.price::text').get().replace('Rs ','')
        short_desc = response.css('header.heading').css('h1::text').get().replace('\n','')
        long_desc = ''.join(response.css('div.description-box').css('p::text').getall())
        region = ''.join(response.css('header.heading').css('span.price-text::text').getall())
        updated = response.css('div.description-box').css('div.meta::text').get()

        details = response.css('section.property-details')[0].css('div.col-holder').css('div.col').getall()
        clean_details0 = ''.join([w3lib.html.remove_tags(x) for x in details]).split('\n\n')
        clean_details1 = [string for string in clean_details0 if string != ""]
        clean_details2 = ','.join(','.join(clean_details1).replace('\n','').split(','))

        features = response.css('section.property-details.char').css('div.col-holder').css('div.col').getall()
        dum = []
        for fts in features:
            dum.append(w3lib.html.remove_tags(fts,keep=('li',)).replace('\n','').replace('<li>',',').replace('</li>',''))
        clean_features = '###'.join(dum)
        scraped_info = {
            'url' : response.url,
            'htype' : 'villa',
            'price' : price,
            'short-desc' : short_desc,
            'long-desc' : long_desc.replace('\n',''),
            'region' : region.replace('\n',''),
            'update' : updated,
            'details' : clean_details2,
            'features' : clean_features}
        yield scraped_info


class LexpressDuplexSpider(scrapy.Spider):
    name = 'LexpressDuplex'
    allowed_domains = ['www.lexpressproperty.com']
    start_urls = ['https://www.lexpressproperty.com/en/buy-mauritius/townhouse_duplex/']
    #rules = [Rule(LinkExtractor(allow = ('townhouse_duplex')), callback = 'parse', follow = True)]

    def parse(self, response):
        house_links = response.css('div.normal-add')
        links = [x.css('a::attr(href)')[-1].extract() for x in house_links]
        for url in links:
            print(url)
            yield scrapy.Request(url, callback=self.parse_page)

        next_page = response.css('div.pagination-block').css('a.button-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        price = response.css('div.price-box').css('strong.price::text').get().replace('Rs ','')
        short_desc = response.css('header.heading').css('h1::text').get().replace('\n','')
        long_desc = ''.join(response.css('div.description-box').css('p::text').getall())
        region = ''.join(response.css('header.heading').css('span.price-text::text').getall())
        updated = response.css('div.description-box').css('div.meta::text').get()

        details = response.css('section.property-details')[0].css('div.col-holder').css('div.col').getall()
        clean_details0 = ''.join([w3lib.html.remove_tags(x) for x in details]).split('\n\n')
        clean_details1 = [string for string in clean_details0 if string != ""]
        clean_details2 = ','.join(','.join(clean_details1).replace('\n','').split(','))

        features = response.css('section.property-details.char').css('div.col-holder').css('div.col').getall()
        dum = []
        for fts in features:
            dum.append(w3lib.html.remove_tags(fts,keep=('li',)).replace('\n','').replace('<li>',',').replace('</li>',''))
        clean_features = '###'.join(dum)
        scraped_info = {
            'url' : response.url,
            'htype' : 'duplex',
            'price' : price,
            'short-desc' : short_desc,
            'long-desc' : long_desc.replace('\n',''),
            'region' : region.replace('\n',''),
            'update' : updated,
            'details' : clean_details2,
            'features' : clean_features}
        yield scraped_info


class LexpressApartSpider(scrapy.Spider):
    name = 'LexpressApart'
    allowed_domains = ['www.lexpressproperty.com']
    start_urls = ['https://www.lexpressproperty.com/en/buy-mauritius/apartment/']
    #rules = [Rule(LinkExtractor(allow = ('townhouse_duplex')), callback = 'parse', follow = True)]

    def parse(self, response):
        house_links = response.css('div.normal-add')
        links = [x.css('a::attr(href)')[-1].extract() for x in house_links]
        for url in links:
            print(url)
            yield scrapy.Request(url, callback=self.parse_page)

        next_page = response.css('div.pagination-block').css('a.button-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        price = response.css('div.price-box').css('strong.price::text').get().replace('Rs ','')
        short_desc = response.css('header.heading').css('h1::text').get().replace('\n','')
        long_desc = ''.join(response.css('div.description-box').css('p::text').getall())
        region = ''.join(response.css('header.heading').css('span.price-text::text').getall())
        updated = response.css('div.description-box').css('div.meta::text').get()

        details = response.css('section.property-details')[0].css('div.col-holder').css('div.col').getall()
        clean_details0 = ''.join([w3lib.html.remove_tags(x) for x in details]).split('\n\n')
        clean_details1 = [string for string in clean_details0 if string != ""]
        clean_details2 = ','.join(','.join(clean_details1).replace('\n','').split(','))

        features = response.css('section.property-details.char').css('div.col-holder').css('div.col').getall()
        dum = []
        for fts in features:
            dum.append(w3lib.html.remove_tags(fts,keep=('li',)).replace('\n','').replace('<li>',',').replace('</li>',''))
        clean_features = '###'.join(dum)
        scraped_info = {
            'url' : response.url,
            'htype' : 'apart',
            'price' : price,
            'short-desc' : short_desc,
            'long-desc' : long_desc.replace('\n',''),
            'region' : region.replace('\n',''),
            'update' : updated,
            'details' : clean_details2,
            'features' : clean_features}
        yield scraped_info



class LexpressVillaSpiderLinks(scrapy.Spider):
    name = 'LexpressVillaLinks'
    allowed_domains = ['www.lexpressproperty.com']
    start_urls = ['https://www.lexpressproperty.com/en/buy-mauritius/villa/?sort=-created_at&l=50']
    #rules = [Rule(LinkExtractor(allow = ('villa')), callback = 'parse', follow = True)]

    def parse(self, response):
        house_links = response.css('div.normal-add')
        links = [x.css('a::attr(href)')[-1].extract() for x in house_links]
        for url in links:
            yield {'url' : url}

        next_page = response.css('div.pagination-block').css('a.button-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)