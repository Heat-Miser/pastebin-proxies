import re
import logging
import scrapy
from geoip import geolite2
from scrapy.http import Request


class ProxiesListSpider(scrapy.Spider):
    name = "pastebin"

    def __init__(self):
        self.start_urls = [
            'https://pastebin.com/u/spys1',
        ]
        logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
        logger.setLevel(logging.WARNING)

    def start_requests(self):
        urls1 = [
            'https://pastebin.com/u/spys1',
        ]
        urls2 = [
            'https://pastebin.com/u/proxy_boy',
            'https://pastebin.com/u/tisocks'
        ]
        for url in urls1:
            yield scrapy.Request(url=url, callback=self.parse_spys1)

        for url in urls2:
            yield scrapy.Request(url=url, callback=self.parse_proxy_boy)

    def parse_spys1(self, response):
        pasties = response.css("table.maintable")[0].xpath("tr/td[1]/a/@href")[:2]
        for pastie in pasties:
            yield Request("https://pastebin.com/raw%s" % (pastie.extract()), callback=self.extract_http_proxies)

    def parse_proxy_boy(self, response):
        pasties = response.css("table.maintable")[0].xpath("tr/td[1]/a[contains(text(),'HTTP')]/@href")[:2]
        for pastie in pasties:
            yield Request("https://pastebin.com/raw%s" % (pastie.extract()), callback=self.extract_http_proxies)
        pasties = response.css("table.maintable")[0].xpath("tr/td[1]/a[contains(text(),'SOCKS')]/@href")[:2]
        for pastie in pasties:
            yield Request("https://pastebin.com/raw%s" % (pastie.extract()), callback=self.extract_socks_proxies)

    def extract_http_proxies(self, response):
        ip_regex = re.compile(r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[0-9]{1,5}")
        for line in response.text.splitlines():
            for match in re.finditer(ip_regex, line):
                ip = match.group().split(":")[0]
                country = geolite2.lookup(ip)
                yield{
                        "proxy": match.group(),
                        "type": "http",
                        "country": country.country if country else "UNKNOWN",
                    }

    def extract_socks_proxies(self, response):
        ip_regex = re.compile(r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[0-9]{1,5}")
        for line in response.text.splitlines():
            for match in re.finditer(ip_regex, line):
                ip = match.group().split(":")[0]
                country = geolite2.lookup(ip)
                yield{
                        "proxy": match.group(),
                        "type": "socks",
                        "country": country.country if country else "UNKNOWN",
                    }