'''
	Jeff Henry's Bing Search Bot
	V1.0
	Last Modified: 5/19/2014
	
	This bot uses the selenium library to search for items using bing.
	Accumulates rewards points for bing rewards.
	Web browsers can only get 15 points a day.
	
	How to use:
		- Install selenium using pip 'pip install -U selenium'
		- Register an email with live.com and with bing rewards prior to using the bot
		- Run and enjoy the benefits 'python bing.py'
		
	Feel free to change the search_terms or add to the code.
  
	Edit email and password to appropriate login

'''

import os,sys,random,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

search_terms = ["titanfall","xbox","videogame deals","how to","cars","exotic","microsoft","coupons","poems","twitch.tv","playstation","left for dead"," instagram", "python", "love","instagood","me","cute","photooftheday","tbt","instamood","iphonesia","picoftheday","igers","girl","beautiful","instadaily","tweegram","summer","instagramhub","follow","bestoftheday","iphoneonly","igdaily","happy","picstitch","webstagram","fashion","sky","nofilter","followme","fun","smile","sun","pretty","instagramers","food","like","friends","lol","hair","nature","bored","funny","life","cool","beach","blue","dog","pink","art","hot","my","family","sunset","photo","versagram","instahub","amazing","statigram","girls","cat","awesome","throwbackthursday","repost","clouds","music","black","instalove","night","textgram","facebook","twitter","yummy","white","yum","yoga","green","school","jamba juice","eyes","sweet","government","2013","style","2012","beauty","boy","nice","halloween","college"]

email = 'email'
password = 'password'

class account(object):
	def __init__(self, email, password):
		super(account, self).__init__()
		self.email = email
		self.password = password
		self.current_points = 0
		self.earned_points = 0
		
	def login(self):
		#--- Create instance of Firefox 
		driver = webdriver.Firefox()
		driver.set_window_size(10,10)
		driver.set_window_position(-1000,-1000)
		
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
	
		repeat = True
		while(repeat):
			#--- Find the search bar
			searchbar = driver.find_element_by_id('sb_form_q')
			#--- Select everything in the search bar and delete it
			searchbar.send_keys(Keys.CONTROL,'a')
			searchbar.send_keys(Keys.DELETE)
			time.sleep(3)
			
			#--- Find current points:
			rewards = driver.find_element_by_id('id_rc')
			if int(rewards.text) > self.current_points:
				self.current_points = int(rewards.text)
				self.earned_points += 1
				print 'Current Points:\t',self.current_points
			
			if self.earned_points == 16:
				driver.quit()
			
			#--- Generate a random term to search for:
			term = search_terms[random.randrange(0,len(search_terms))]
			print 'Searching for:\t', term
			
			try:
				#--- Enter the search term:
				searchbar.send_keys(term,Keys.ENTER)
				time.sleep(random.randint(25,30))
			
				try:
					#--- Find a link on the page and click it
					link = driver.find_element_by_partial_link_text(term[1:3])
					print 'Clicking link:\t',link.text
					link.click()
					time.sleep(random.randint(10,12))
					#--- Return to previous screen
					driver.back()
				except:
					print "No Links"
		
			except:
				print 'Problem searching for the term'
				
			assert 'Bing' in driver.title
			
		driver.quit()
			
if __name__ == "__main__":
	bot = account(email,password)
	bot.login()
