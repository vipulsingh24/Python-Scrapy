# -*- coding: utf-8 -*-
import scrapy

class MyItem(scrapy.Item):
	Name_of_Company = scrapy.Field()
	Contact_Person = scrapy.Field()
	Designation = scrapy.Field()
	Email = scrapy.Field()
	Phone_Number = scrapy.Field()
	Mobile = scrapy.Field()
	Address = scrapy.Field()
	City = scrapy.Field()
	State = scrapy.Field()
	Pincode = scrapy.Field()
	Country = scrapy.Field()

class PrintWeekSpider(scrapy.Spider):
	name = 'printweek'
	allowed_domains = ['pwidirectory.haymarketsac.in']
	
	def start_requests(self):
		urls = ['http://pwidirectory.haymarketsac.in/page/%d/?s' % page for page in range(1, 179)]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse_more_details)

	def parse_more_details(self, response):
		for i in range(1, 13):
			url = response.xpath('//*[@id="core_middle_column"]/div/div[3]/div[1]/div[{0}]/div/div[2]/h4/a/@href'.format(i)).get()
			yield scrapy.Request(url=url, callback=self.parse_detail_table)

	def parse_detail_table(self, response):
		item = MyItem()
		if response.css('.rowwnameofcompany2 p::text'):
			item['Name_of_Company'] = response.css('.rowwnameofcompany2 p::text').extract()[0]
		else:
			item['Name_of_Company'] = ''
		if response.css('.val_contactperson2 p::text'):
			item['Contact_Person'] = response.css('.val_contactperson2 p::text').extract()[0]
		else:
			item['Contact_Person'] = ''
		if response.css('.val_designation ::text'):
			item['Designation'] = response.css('.val_designation ::text').extract()[0]
		else:
			item['Designation'] = ''
		if response.css('.val_email2 ::text'):
			item['Email'] = response.css('.val_email2 ::text').extract()[0]
		else:
			item['Email'] = ''
		if response.css('.val_Phonemumber2 ::text'):
			item['Phone_Number'] = response.css('.val_Phonemumber2 ::text').extract()[0]
		else:
			item['Phone_Number'] = ''
		if response.css('.val_mobile1 ::text'):
			item['Mobile'] = response.css('.val_mobile1 ::text').extract()[0]
		else:
			item['Mobile'] = ''
		if response.css('.val_address2 ::text'):
			item['Address'] = response.css('.val_address2 ::text').extract()[0]
		else:
			item['Address'] = ''
		if response.css('.val_city ::text'):
			item['City'] = response.css('.val_city ::text').extract()[0]
		else:
			item['City'] = ''
		if response.css('.val_state ::text'):
			item['State'] = response.css('.val_state ::text').extract()[0]
		else:
			item['State'] = ''
		if response.css('.val_pincode ::text'):
			item['Pincode'] = response.css('.val_pincode ::text').extract()[0]
		else:
			item['Pincode'] = ''
		if response.css('.val_country ::text'):
			item['Country'] = response.css('.val_country ::text').extract()[0]
		else:
			item['Country'] = ''

		#item['Name_of_Company'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[1]/td/p').extract()[0]
		#item['Contact_Person'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[2]/td/p/text()').extract()[0]
		#item['Designation'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[3]/td/text()').extract()[0]
		#item['Email'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[4]/td/a/text()').extract()[0]
		#item['Phone_Number'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[5]/td/text()').extract()[0]
		#item['Mobile'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[6]/td/text()').extract()[0]
		#item['Address'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[7]/td/p/text()').extract()[0]	  
		#item['City'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[8]/td/text()').extract()[0]
		#item['State'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[9]/td/text()').extract()[0]
		#item['Pincode'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[10]/td/text()').extract()[0]
		#item['Country'] = response.xpath('//*[@id="TableCustomFieldsBig"]/tbody/tr[11]/td/text()').extract()[0]
		yield item
		

	

