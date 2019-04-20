# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class veriler(scrapy.Item):
	baslik = scrapy.Field()
	aciklama = scrapy.Field()
	fiyat = scrapy.Field()
	kategori = scrapy.Field()	#Checking-Values

class Veri(scrapy.Item):
	"""docstring for veri"""
	def __init__(self,baslik,aciklama,fiyat,kategori):
		self.baslik = baslik
		self.aciklama = aciklama
		self.fiyat = fiyat
		self.kategori = kategori
		
	def baslik(self,baslik,SecondValue= None):
		return self.baslik
	def aciklama(self,aciklama,SecondValue = None):
		return self.aciklama
	def fiyat(self,fiyat,SecondValue = None):
		return self.fiyat
	def kategori(self,kategori,SecondValue = None):
		return self.kategori