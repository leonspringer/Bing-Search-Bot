#!/usr/bin/env python
# -*-coding:utf-8-*-


#	Jeff Henry's Bing Search Bot
#	V1.0
#	Last Modified: 2/24/2015
#	
#	This bot uses the selenium library to search for items using bing.
#	Accumulates rewards points for bing rewards.
#	Web browsers can only get 15 points a day.
#	Opens in a firefox window, you can see it work there.
#	
#	How to use:
#		- Install selenium using pip 'pip install -U selenium'
#		- Register an email with live.com and with bing rewards prior to using the bot
#		- Run and enjoy the benefits
#
#	Edit email and password to appropriate login
#	
#	V1.1 Updates:
#	- Handles if current weekday is tuesday of may, which means more points!
#       V1.2 Updates:
#	- Removed link clinking, switched to chromedriver in preparation for mobile search update.


import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


with open('./dictionary.txt') as f:
	search_terms = f.readlines()
#search_terms = ["titanfall","xbox","videogame deals","how to","cars","exotic","microsoft","coupons","poems","twitch.tv","playstation","left for dead"," instagram", "python", "love","instagood","me","cute","photooftheday","tbt","instamood","iphonesia","picoftheday","igers","girl","beautiful","instadaily","tweegram","summer","instagramhub","follow","bestoftheday","iphoneonly","igdaily","happy","picstitch","webstagram","fashion","sky","nofilter","followme","fun","smile","sun","pretty","instagramers","food","like","friends","lol","hair","nature","bored","funny","life","cool","beach","blue","dog","pink","art","hot","my","family","sunset","photo","versagram","instahub","amazing","statigram","girls","cat","awesome","throwbackthursday","repost","clouds","music","black","instalove","night","textgram","facebook","twitter","yummy","white","yum","yoga","green","school","jamba juice","eyes","sweet","government","2013","style","2012","beauty","boy","nice","halloween","college"]

email = 'email@somewhere.com'
password = 'P@ssw0rd!'


class account(object):
	def __init__(self, email, password):
		super(account, self).__init__()
		self.email = email
		self.password = password
		self.current_points = 0
		self.earned_points = 0
		self.page_searches = 0
		
	def login(self):
		#--- Determine max searches:
		now = datetime.datetime.now()
		if now.strftime('%A') == 'Tuesday' and now.strftime('%B') == 'May':
			print 'Day of week: ',now.strftime('%A')
			print 'Every Tuesday in May gets up to 30 searches rewarded.' 
			max_searches_pc = 60
		else:
			print 'Day of week: ',now.strftime('%A')
			print 'Up to 15 searches rewarded today.'
			max_searches_pc = 30
		
		#--- Create instance of Firefox 
		driver = webdriver.Chrome("./chromedriver")
		driver.set_window_size(300,300)
		driver.set_window_position(300,300)
		
		#--- Open live.com to login
		driver.get('http://www.live.com')
		email = driver.find_element_by_id("i0116")
		password = driver.find_element_by_id("i0118")
		
		#--- Enter login details and submit
		email.send_keys(self.email)
		password.send_keys(self.password)
		password.send_keys(Keys.ENTER)
		time.sleep(5)
		
		#--- Open Bing.com
		driver.get("http://www.bing.com")
		time.sleep(3)
		assert 'Bing' in driver.title
	
		repeat = True
		while(repeat):
			#--- Print current point count
			rewards = driver.find_element_by_id('id_rc')
			print 'Current Points: ',rewards.text

			#--- Find the search bar
			searchbar = driver.find_element_by_id('sb_form_q')
			
			#--- Select everything in the search bar and delete it
			searchbar.clear()
			time.sleep(3)
						
			#--- Generate a random term to search for:
			term = search_terms[random.randrange(0,len(search_terms))]
			print 'Searching for:\t', term
			
			try:
				#--- Enter the search term:
				searchbar.send_keys(term,Keys.ENTER)
				self.page_searches += 1
				time.sleep(random.randint(5,5))
			
				try:
					#--- Find a link on the page and click it
					link = driver.find_element_by_partial_link_text(term[1:3])
					#print 'Clicking link:\t',link.text
					#link.click()
					#time.sleep(random.randint(10,12))
					#--- Return to previous screen
					#driver.back()
				except:
					print "No Links"
		
			except:
				print 'Problem searching for the term'
			
			#--- Quit if we've done enough searches
			if self.page_searches >= max_searches_pc:
				print "Maximum searches of " + str(max_searches_pc) + " reached, exiting"
				driver.quit()
				sys.exit()
		driver.quit()
			
if __name__ == "__main__":
	bot = account(email,password)
	bot.login()
