# -*- coding: utf-8 -*-
import scrapy


class MufatoSpider(scrapy.Spider):
    name = 'mufato'
    
    start_urls = [
                'https://delivery.supermuffato.com.br/',
    ]
    

    def parse(self, response):
        
        #Pegando todos os links de cada url

        
        urls = response.css(".header-md-nav-content-item a::attr(href)").extract()

        print('Dentro do Item '+ response.url)
                
        produtos = response.css("div.prd-list-item-holder.has-stock.clearfix")
        with open('mufato.txt', 'a') as f:
            f.write('\n******* Dentro do Item ' + response.url + "\n \n")
            f.close()
        count = 0
        for produto in produtos:
            prod_name = produto.css("h3.prd-list-item-name::text").extract_first()
            prod_price = produto.css("span.prd-list-item-price-sell::text").extract_first()
            prod_complite = prod_name.strip()+ " " + prod_price.strip()

            count =  count + 1

            with open('mufato.txt', 'a') as f:
                f.write(prod_complite + "\n")
                f.close()

        with open('mufato.txt', 'a') as f:
            f.write('\nQtde...: ' + str(count) + '\n')
            f.close()
    
        for url in urls:
            yield response.follow(url, callback=self.parse)
                
                