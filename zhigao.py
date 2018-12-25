# -*- coding: utf-8 -*-
import scrapy
import execjs
from urllib.request import urljoin
from zhigaodian.items import BrandItem, EnterpriseInformationItem

class ZhigaoSpider(scrapy.Spider):
    name = 'zhigao'
    allowed_domains = ['iptop.cn']
    start_urls = ['https://www.iptop.cn/trademark/s?queryString=1&page=1&pageSize=15&type=0']

    def parse(self, response):
        # print(response.text)
        result = response.xpath('//div[@class="search_result_data square_arrange_data"]/ul/li')
        # print(result)

        for res in result:
            # 图片地址
            img_src = res.xpath('div[1]/a/img/@src').extract_first('')
            #
            href = res.xpath('div[1]/a/@href').extract_first('')
            # 公司名称
            title = res.xpath('h2[1]/a/font/text()').extract_first('')
            # 注册号
            number = res.xpath('div[2]/p[1]/span[2]/text()').extract_first('')
            # 状态
            status = res.xpath('div[2]/p[2]/span[2]/text()').extract_first('')
            # 初审日期
            strat_time = res.xpath('div[2]/p[3]/span[2]/text()').extract_first('')
            # 类别
            type = res.xpath('div[3]/p[1]/span[2]/text()').extract_first('')
            # 申请日期
            apply_time = res.xpath('div[3]/p[2]/span[2]/text()').extract_first('')
            # 注册日期
            reg_time = res.xpath('div[3]/p[3]/span[2]/text()').extract_first('')
            # 商品服务
            shop_server = res.xpath('div[4]/p[1]/span[2]/text()').extract_first('')
            # 申请人
            apply_person = res.xpath('div[4]/p[2]/a/span/text()').extract_first('')
            # 详情链接
            apply_href = res.xpath('div[4]/p[2]/a/@href').extract_first('')
            # 代理机构
            agent = res.xpath('div[4]/p[3]/span[2]/text()').extract_first('')

            url = urljoin(response.url, apply_href)
            # print(url)
            # url = urljoin(response.url, href)
            # yield scrapy.Request(url=url, meta={'href': href} ,headers={
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
            #     'Upgrade-Insecure-Requests': '1',
            #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            #     'referer': 'https://www.iptop.cn/trademark/s?queryString=1&type=0&sort=0&asc=false&page=1&pageSize=15&lawStatus=&year=&sell=false&registerEnable=false'
            # }, callback=self.get_token)
            # return

            yield scrapy.Request(url=url,headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
                'Upgrade-Insecure-Requests': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'referer': 'https://www.iptop.cn/trademark/s?queryString=1&type=0&sort=0&asc=false&page=1&pageSize=15&lawStatus=&year=&sell=false&registerEnable=false'
            }, callback=self.parse_detail)

            img_src = urljoin(response.url, img_src)
            item = BrandItem()
            item['img_src'] = [img_src]
            item['title'] = title
            item['number'] = number
            item['status'] = status
            item['strat_time'] = strat_time
            item['type'] = type
            item['apply_time'] = apply_time
            item['reg_time'] = reg_time
            item['shop_server'] = shop_server
            item['apply_href'] = apply_href
            item['apply_person'] = apply_person
            item['agent'] = agent
            yield item

            return
    # def get_token(self, response):
    #     # print(response.text)
    #     href = response.meta.get('href')
    #     res = response.text
    #     resourceToken = res.split("resourceToken = '")[-1].split("';")[0]
    #     encryptKey = res.split("encryptKey = '")[-1].split("';")[0]
    #     exe = execjs.compile(open('token.js', 'r', encoding='utf-8').read())
    #     token = exe.call('appendToken', href, resourceToken, encryptKey).replace('info','item')
    #     url_detail = urljoin(response.url, token).replace('=?', '=&').replace('goodsId=&', '')+'&goodsId='
    #
    #     print(url_detail)
    #     yield scrapy.Request(url=url_detail, callback=self.parse_detail)
    #
    def parse_detail(self, response):
        # print(response.text)
        divs = response.xpath('//div[@class="cmin-content"]/div[1]')
        for div in divs:
            # 公司名称
            name = div.xpath('div[2]/table/tr[1]/td[2]/span/text()').extract_first('')
            # 法人
            faren = div.xpath('div[2]/table/tr[2]/td[2]/text()').extract_first('')
            # 公司电话
            phone = div.xpath('div[2]/table/tr[3]/td[2]/text()').extract_first('')
            # 地址
            address = div.xpath('div[2]/table/tr[4]/td[2]/text()').extract_first('')

        information = response.xpath('//div[@class="cmin-content"]/div[2]')
        for info in  information:
            # 状态
            status = info.xpath('div[2]/table/tr[1]/td[2]/text()').extract_first('')
            # 成立时间
            establish = info.xpath('div[2]/table/tr[1]/td[4]/text()').extract_first('')
            # 营业期限
            business = info.xpath('div[2]/table/tr[1]/td[6]/text()').extract_first('')
            # 统一社会信用代码
            code = info.xpath('div[2]/table/tr[2]/td[2]/text()').extract_first('')
            # 工商注册号
            registration = info.xpath('div[2]/table/tr[2]/td[4]/text()').extract_first('')
            # 组织机构代码
            organization = info.xpath('div[2]/table/tr[2]/td[6]/text()').extract_first('')
            # 核准日期
            check_time = info.xpath('div[2]/table/tr[3]/td[2]/text()').extract_first('')
            # 企业类型
            type_enterprise = info.xpath('div[2]/table/tr[3]/td[4]/text()').extract_first('')
            # 登记机关
            registration_organ = info.xpath('div[2]/table/tr[3]/td[6]/text()').extract_first('')
            # 所属行业
            trade = info.xpath('div[2]/table/tr[4]/td[2]/text()').extract_first('')
            # 注册资本
            registered_capital = info.xpath('div[2]/table/tr[4]/td[4]/text()').extract_first('')
            # 公司规模
            scale = info.xpath('div[2]/table/tr[4]/td[6]/text()').extract_first('')
        # 经营范围
        business_scope = response.xpath('//div[@class="cmin-content"]/div[3]/div[2]/p/text()').extract_first('').replace('\n', '').replace('\t', '')

        div4 = response.xpath('//div[@class="cmin-content"]/div[4]')
        for div in div4:
            # 股东
            shareholders = div.xpath('div[2]/table/tr[3]/td/ul/li//text()').extract()
            shareholder = ','.join(shareholders)

        # print(shareholder)

        div5 = response.xpath('//div[@class="cmin-content"]/div[5]')
        for div in div5:
            # 执行董事;经理：
            manager = div.xpath('div[2]/ul[1]/li/span/text()').extract_first('')
            # 监事：
            monitor = div.xpath('div[2]/ul[2]/li/span/text()').extract_first('')

        div6 = response.xpath('//div[@class="cmin-content"]/div[6]')
        for div in div6:
            # 变更记录
            change = div.xpath('div[2]/table/tr[2]/td[1]/text()').extract_first('')
            # 变更前
            change_ago = div.xpath('div[2]/table/tr[2]/td[2]/ul/li/text()').extract_first('')
            # 变更后
            change_end = div.xpath('div[2]/table/tr[2]/td[3]/ul/li/text()').extract_first('')

        item = EnterpriseInformationItem()
        item['com_name'] = name
        item['faren'] = faren
        item['phone'] = phone
        item['address'] = address
        item['status'] = status
        item['establish'] = establish
        item['business'] = business
        item['code'] = code
        item['registration'] = registration
        item['organization'] = organization
        item['check_time'] = check_time
        item['type_enterprise'] = type_enterprise
        item['registration_organ'] = registration_organ
        item['registered_capital'] = registered_capital
        item['trade'] = trade
        item['scale'] = scale
        item['business_scope'] = business_scope
        item['shareholder'] = shareholder
        item['manager'] = manager
        item['monitor'] = monitor
        item['change'] = change
        item['change_ago'] = change_ago
        item['change_end'] = change_end

        yield item
        return

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl zhigao'.split(' '))