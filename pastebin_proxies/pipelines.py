# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import requests


class PastebinProxiesPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['proxy'] in self.ids_seen:
            raise DropItem("Duplicate proxy found: %s" % item)
        else:
            self.ids_seen.add(item['proxy'])
            return item


class RemoveSlowProxies(object):
    def process_item(self, item, spider):
        if item["type"] == "http":
            proxy = {'http': item['proxy'], 'https': item['proxy']}
            try:
                r = requests.get("http://ifconfig.co/ip", proxies=proxy, timeout=1)
                ip = item['proxy'].split(":")[0]
                if ip == r.text.strip():
                    return item
                else:
                    raise DropItem("Bad proxy: %s" % item)
            except:
                raise DropItem("Proxy too slow: %s" % item)
        if item["type"] == "socks":
            proxy = {'http': "socks4://%s" % (item['proxy']), 'https': "socks4://%s" % (item['proxy'])}
            try:
                r = requests.get("http://ifconfig.co/ip", proxies=proxy, timeout=1)
                ip = item['proxy'].split(":")[0]
                if ip == r.text.strip():
                    return item
                else:
                    raise DropItem("Bad proxy: %s" % item)
            except:
                raise DropItem("Proxy too slow: %s" % item)

