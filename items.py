# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhigaodianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BrandItem(scrapy.Item):
    img_src = scrapy.Field()
    title = scrapy.Field()
    number = scrapy.Field()
    status = scrapy.Field()
    strat_time = scrapy.Field()
    type = scrapy.Field()
    apply_time = scrapy.Field()
    reg_time = scrapy.Field()
    shop_server = scrapy.Field()
    apply_person = scrapy.Field()
    apply_href = scrapy.Field()
    agent = scrapy.Field()
    image_path = scrapy.Field()

    def save(self, cursor):
        sql = "INSERT INTO brand (img_src, title, number, status, strat_time, type, apply_time, reg_time, shop_server, apply_person, apply_href, agent, image_path) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (self['img_src'], self['title'], self['number'], self['status'], self['strat_time'],
                             self['type'], self['apply_time'], self['reg_time'], self['shop_server'],
                             self['apply_person'], self['apply_href'], self['agent'], self['image_path']))


class EnterpriseInformationItem(scrapy.Item):
    com_name = scrapy.Field()
    faren = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    status = scrapy.Field()
    establish = scrapy.Field()
    business = scrapy.Field()
    code = scrapy.Field()
    registration = scrapy.Field()
    organization = scrapy.Field()
    check_time = scrapy.Field()
    type_enterprise = scrapy.Field()
    registration_organ = scrapy.Field()
    trade = scrapy.Field()
    registered_capital = scrapy.Field()
    scale = scrapy.Field()
    business_scope = scrapy.Field()
    shareholder = scrapy.Field()
    manager = scrapy.Field()
    monitor = scrapy.Field()
    change = scrapy.Field()
    change_ago = scrapy.Field()
    change_end = scrapy.Field()

    def save(self, cursor):

        sql = "INSERT INTO enterpriseinformation (com_name, faren, phone, address, status, establish, business, code, registration, organization, check_time, type_enterprise, registration_organ, trade, registered_capital, scale, business_scope, shareholder,  manager, monitor, change_time, change_ago, change_end) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self['com_name'], self['faren'], self['phone'], self['address'], self['status'],self['establish'], self['business'], self['code'], self['registration'],self['organization'], self['check_time'], self['type_enterprise'], self['registration_organ'], self['trade'], self['registered_capital'], self['scale'], self['business_scope'], self['shareholder'], self['manager'], self['monitor'], self['change'], self['change_ago'], self['change_end'])
        print(sql)
        cursor.execute(sql)

