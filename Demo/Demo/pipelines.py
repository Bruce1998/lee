# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline:
    def process_item(self, item, spider):
            with open("demo_weibo.txt",'w',encoding='utf-8')as f:
                f.write('title:'+str(item['title'])+'\n')
                f.write('title_url:'+str(item['title_url'])+'\n')
                #f.write('author'+str(item1['author'])+'\n')
                #f.write('time'+str(item1['item'])+'\n')
            return item
