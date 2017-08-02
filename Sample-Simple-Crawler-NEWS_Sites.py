#! /usr/bin/env python
#! -*- coding : utf-8 -*-


import re
import mechanize
import urllib
import urllib2
from bs4 import BeautifulSoup
import time
import feedparser

#Programming Language : Python 2.7
#Task : Crawler(Web Spider)
#Availeble Options :   #ekonomi #siyaset #spor #magazin 	

def anadolu(gir):
	if gir == "siyaset":
		gir = "politika"
	d = feedparser.parse('http://aa.com.tr/tr/rss/default?cat=%s' %gir)
	count = 0
	while count < len(d['entries']):
		print d['entries'][count]['title']
		#print d['entries'][count]['link'] #Linkler
		count += 1
		#print len(d['entries']) #Konu Sayisi


def milliyet(gir):
	f = feedparser.parse("http://www.milliyet.com.tr/rss/rssNew/%sRss.xml" %gir)
	count1 = 0
	while count1 < len(f['entries']):
		print f['entries'][count1]['title']
		count1 += 1

def hurriyet(gir):
	f = feedparser.parse("http://www.hurriyet.com.tr/rss/%s" %gir)
	count2 = 0
	while count2 < len(f['entries']):
		print f["entries"][count2]["title"]
		count2 += 1
def sabah(gir):
	f1 = feedparser.parse("http://www.sabah.com.tr/rss/%s.xml" %gir)
	count3 = 0
	while count3 < len(f1["entries"]):
		print f1["entries"][count3]["title"]
		count3 += 1
 

gir = raw_input("gir\n")
print "\n \n \n ANADOLU \n \n \n"
anadolu(gir)
print "\n \n \n MILLIYET \n \n \n"
milliyet(gir)
print "\n \n HURRIYET \n \n"
hurriyet(gir)
print "\n \n SABAH \n \n"
sabah(gir)
