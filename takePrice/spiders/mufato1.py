# -*- coding: utf-8 -*-
import scrapy


class MufatoSpider(scrapy.Spider):
    name = 'mufato1'
    
    start_urls = [
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/arroz',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/feijao',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/massas',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/bomboniere',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/acucares-e-adocantes',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/farinaceos-e-amidos',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/oleos-e-azeites',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/biscoitos',
                'https://delivery.supermuffato.com.br/mercearia-e-alimentos/',
                'https://delivery.supermuffato.com.br/carnes-aves-e-peixes/carnes-bovinas',
                'https://delivery.supermuffato.com.br/carnes-aves-e-peixes/carnes-suinas',
                'https://delivery.supermuffato.com.br/carnes-aves-e-peixes/frango',
                'https://delivery.supermuffato.com.br/carnes-aves-e-peixes',
                'https://delivery.supermuffato.com.br/bazar/casa-e-cozinha',
                'https://delivery.supermuffato.com.br/bazar/churrasco',
                'https://delivery.supermuffato.com.br/bazar/automotivo',
                'https://delivery.supermuffato.com.br/bazar',
                'https://delivery.supermuffato.com.br/congelados/pratos-prontos',
                'https://delivery.supermuffato.com.br/congelados/petiscos-e-empanados',
                'https://delivery.supermuffato.com.br/congelados/sorvetes',
                'https://delivery.supermuffato.com.br/congelados',
                'https://delivery.supermuffato.com.br/frios-e-laticinios/queijos',
                'https://delivery.supermuffato.com.br/frios-e-laticinios/embutidos',
                'https://delivery.supermuffato.com.br/frios-e-laticinios/laticinios',
                'https://delivery.supermuffato.com.br/frios-e-laticinios',
                'https://delivery.supermuffato.com.br/higiene-e-beleza/cabelo',
                'https://delivery.supermuffato.com.br/higiene-e-beleza/sabonetes',
                'https://delivery.supermuffato.com.br/higiene-e-beleza/higiene-oral',
                'https://delivery.supermuffato.com.br/higiene-e-beleza',
                'https://delivery.supermuffato.com.br/hortifruti/frutas',
                'https://delivery.supermuffato.com.br/hortifruti/verduras',
                'https://delivery.supermuffato.com.br/hortifruti/ovos',
                'https://delivery.supermuffato.com.br/hortifruti',
                'https://delivery.supermuffato.com.br/limpeza/limpadores',
                'https://delivery.supermuffato.com.br/limpeza/inseticidas',
                'https://delivery.supermuffato.com.br/limpeza/purificadores-de-ar',
                'https://delivery.supermuffato.com.br/limpeza',

    ]

    def parse(self, response):
        
        """ Pegando os Produto """

        produtos = response.css("div.prd-list-item-holder.has-stock.clearfix")

        for produto in produtos:
            prod_name = produto.css("h3.prd-list-item-name::text").extract_first()
            prod_price = produto.css("span.prd-list-item-price-sell::text").extract_first()
            print(prod_name.strip()+ " " + prod_price.strip())