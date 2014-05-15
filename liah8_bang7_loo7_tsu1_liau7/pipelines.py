# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class Bang7Loo7Pipeline(object):
    def process_item(self, item, spider):
        print('XD',item['url'])
        return item
