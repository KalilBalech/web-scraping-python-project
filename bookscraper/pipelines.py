# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# this is the file we can process the information we are going to return, like removing commas, removing dollar sign or replace it 
# by another currency sign, check if the field value is valid, turn a string value into a integer value, removing uncesary strings
# that comes with the info we are interested, and so on

# remeber to uncomment the pipeline funcionality in setting.py... somewhere around line 65 until line 67

class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        bookName = adapter.get('name') # remove commas from name field
        adapter['name'] = bookName[0].replace(",", "") # the zero index is needed since adapter['name] and adapter['price'] returns a tuple

        bookPrice = adapter.get('price')
        adapter['price'] = bookPrice[0].replace(bookPrice[0][0], "")
        adapter['price'] = float(adapter['price'])



        return item
