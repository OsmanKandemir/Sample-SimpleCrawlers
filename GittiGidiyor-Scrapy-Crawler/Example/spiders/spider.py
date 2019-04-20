#! -*- Windows -*-
#! -*- coding = utf-8 -*-
#!Crawler

import re
import scrapy
import os
import sys
from scrapy.spiders import Spider
from ..items import veriler

class GittiGidiyorSpider(Spider):
	"""docstring for ClassName"""
	name = 'Example'
	start_urls = [
				'https://urun.gittigidiyor.com/otomobil-motor-aksesuar/4x4-off-road-sticker-30-x-21-cm-1999-43011756%s' %page for page in range(20)
		]
	def RegexHTMLCODE(self,string,secondFile = None):
		return re.sub("<.*?>","",str(string))
	def parse(self,response):

		veri = veriler()
		ht = response.xpath("//div[@class='overflow-content']").extract()
		results = self.RegexHTMLCODE(ht)
		aciklama = results.replace("\\n","").replace("\\xa0","")
		baslik = self.RegexHTMLCODE(response.xpath("//title").extract())
		fiyat = self.RegexHTMLCODE(response.xpath("//div[@class='low-price extra-price all-price robotobold one-price']").extract())
		kategori = self.RegexHTMLCODE(response.xpath("//ul[@class='clearfix hidden-m hidden-breadcrumb robot-productPage-breadcrumb-hiddenBreadCrumb']").extract()).replace("\\n","")
		if not 'Tüm Kategoriler - GittiGidiyor' in baslik:
			veri['baslik'] = baslik
			veri['aciklama'] = aciklama
			veri['fiyat'] = fiyat
			veri['kategori'] = kategori
		
		yield veri

		#yield {
			#'BASLIK' : baslik,
			#'ACIKLAMA' : aciklama,
			#'FIYAT' : fiyat,
			#'KATEGORI' : kategori
			
			#}

	

