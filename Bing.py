<<<<<<< HEAD
=======
#!/usr/bin/env python
# -*-coding:utf-8-*-


# Bing Search Bot
# V1.0
# Last Modified: 3/12/2015
# 
# This bot uses the selenium library to search for items using bing.
# Accumulates rewards points for bing rewards.
# Web browsers can only get 15 points a day.
# Opens in a firefox window, you can see it work there.
# 
# How to use:
#   - Install python
#   - Install selenium using pip 'pip install -U selenium'
#   - Register an email with live.com and with bing rewards prior to using the bot
#   - Run and enjoy the benefits
#
# Edit email and password to appropriate login
# 
# V1.1 Updates:
# - Handles if current weekday is tuesday of may, which means more points!
# V1.2 Updates:
# - Removed link clinking, switched to chromedriver in preparation for mobile search update.
# V1.3 Updates:
# - Added the abilty to have email and password outside of file in accounts.txt
# V1.4 Updates:
# - Added mobile search emulation! 
# - Moved search options for future parameterization.

>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
import os,sys,random,time,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
<<<<<<< HEAD
import argparse

#--- Options
normal_searches_pc = 31
most_searches_pc = normal_searches_pc * 2

normal_searches_mobile = 21
most_searches_mobile = normal_searches_mobile * 2

#--- default arguments
=======

#--- Options
normal_searches_pc = 30
most_searches_pc = normal_searches_pc * 2

normal_searches_mobile = 20
most_searches_mobile = normal_searches_mobile * 2

>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
accounts_location = './accounts.txt'
dictionary_location = './dictionary.txt'
chromedriver_location = './chromedriver'

<<<<<<< HEAD

parser = argparse.ArgumentParser(description='This bot uses the selenium library to search for items using bing.')
parser.add_argument('-a','--accounts', dest="accounts_location", default = accounts_location, help='')
parser.add_argument('-d','--dictionary', dest="dictionary_location", default = dictionary_location, help='')
parser.add_argument('-c','--chrome-driver', dest="chromedriver_location", default = chromedriver_location, help='')
parser.add_argument('-p','--pc-searches', dest="normal_searches_pc", type = int, default = normal_searches_pc, help='')
parser.add_argument('-m','--mobile-searches', dest="normal_searches_mobile", type = int, default = normal_searches_mobile, help='')
args = parser.parse_args()

accounts_location = args.accounts_location
dictionary_location = args.dictionary_location
chromedriver_location = args.chromedriver_location
normal_searches_pc = args.normal_searches_pc
normal_searches_mobile = args.normal_searches_mobile
most_searches_pc = args.normal_searches_pc * 2
most_searches_mobile = args.normal_searches_mobile * 2

=======
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
#--- Use email@somewhere.com:P@ssWord format for each line in accounts.txt
with open(accounts_location) as f:
  credentials = [x.strip().split(':') for x in f.readlines()]

#--- Dictionary stored here
with open(dictionary_location) as f:
  search_terms = f.readlines()



<<<<<<< HEAD



=======
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
class account(object):
  def __init__(self, email, password):
    super(account, self).__init__()
    self.email = email
    self.password = password
    self.current_points = 0
    self.earned_points = 0
<<<<<<< HEAD
    self.page_searches = 0
    
  def desktop(self):
    #--- Determine max searches:
    now = datetime.datetime.now()
    if now.strftime('%A') == 'Tuesday' and now.strftime('%B') == 'May':
      print ("Running "  + str(most_searches_pc) +  " desktop searches...")
      if most_searches_pc == 0:
        return
      print ('Day of week: ',now.strftime('%A'))
      print ('Every Tuesday in May gets up to 30 searches rewarded.')
      max_searches_pc = most_searches_pc
    else:
      print ("Running "  + str(normal_searches_pc) +  " desktop searches...")  
      if normal_searches_pc == 0:
        return
      print ('Day of week: ',now.strftime('%A'))
      print ('Up to 15 searches rewarded today.')
=======
    self.page_searches_pc = 0
    self.page_searches_mobile = 0
    
  def desktop(self):
    print ('Running desktop searches...')
    #--- Determine max searches:
    now = datetime.datetime.now()
    if now.strftime('%A') == 'Tuesday' and now.strftime('%B') == 'May':
      print 'Day of week: ',now.strftime('%A')
      print 'Every Tuesday in May gets up to 30 searches rewarded.' 
      max_searches_pc = most_searches_pc
    else:
      print 'Day of week: ',now.strftime('%A')
      print 'Up to 15 searches rewarded today.'
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
      max_searches_pc = normal_searches_pc
    
    #--- Create instance of Chrome
    driver = webdriver.Chrome(chromedriver_location)
    driver.set_window_size(300,300)
    driver.set_window_position(300,300)
    
    #--- Open live.com to login
    driver.get('http://www.live.com')
    email = driver.find_element_by_id("i0116")
    password = driver.find_element_by_id("i0118")
    
    #--- Enter login details and submit
<<<<<<< HEAD
    print ('Account: ', self.email)
=======
    print 'Account: ', self.email
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
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
<<<<<<< HEAD
      print ('Current Points: ',rewards.text)
=======
      print 'Current Points: ',rewards.text
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0

      #--- Find the search bar
      searchbar = driver.find_element_by_id('sb_form_q')
      
      #--- Select everything in the search bar and delete it
      searchbar.clear()
      time.sleep(3)
            
      #--- Generate a random term to search for:
      term = search_terms[random.randrange(0,len(search_terms))]
<<<<<<< HEAD
      print ('Searching for:\t', term)
=======
      print 'Searching for:\t', term
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
      
      try:
        #--- Enter the search term:
        searchbar.send_keys(term,Keys.ENTER)
<<<<<<< HEAD
        self.page_searches += 1
=======
        self.page_searches_pc += 1
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
        time.sleep(random.randint(5,35))
      
        try:
          #--- Find a link on the page and click it
          link = driver.find_element_by_partial_link_text(term[1:3])
          #print 'Clicking link:\t',link.text
          #link.click()
          #time.sleep(random.randint(10,12))
          #--- Return to previous screen
          #driver.back()
        except:
<<<<<<< HEAD
          print ("No Links")
    
      except:
        print ('Problem searching for the term')
      
      #--- Quit if we've done enough searches
      if self.page_searches >= max_searches_pc:
        print ("Maximum searches of " + str(max_searches_pc) + " reached, exiting.\n")
        self.page_searches = 0
=======
          print "No Links"
    
      except:
        print 'Problem searching for the term'
      
      #--- Quit if we've done enough searches
      if self.page_searches_pc >= max_searches_pc:
        print "Maximum searches of " + str(max_searches_pc) + " reached, exiting.\n"
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
        driver.quit()
        break


  def mobile(self):
<<<<<<< HEAD
    #--- Determine max searches:
    now = datetime.datetime.now()
    if now.strftime('%A') == 'Tuesday' and now.strftime('%B') == 'May':
      print ("Running "  + str(most_searches_pc) +  " mobile searches...")
      print ('Day of week: ',now.strftime('%A'))
      print ('Every Tuesday in May gets up to 20 searches rewarded.')
      max_searches_mobile = most_searches_mobile
    else:
      print ("Running "  + str(normal_searches_mobile) +  " mobile searches...")  
      print ('Day of week: ',now.strftime('%A'))
      print ('Up to 10 searches rewarded today.')
=======
    print ('Running mobile searches...')
    #--- Determine max searches:
    now = datetime.datetime.now()
    if now.strftime('%A') == 'Tuesday' and now.strftime('%B') == 'May':
      print 'Day of week: ',now.strftime('%A')
      print 'Every Tuesday in May gets up to 20 searches rewarded.' 
      max_searches_mobile = most_searches_mobile
    else:
      print 'Day of week: ',now.strftime('%A')
      print 'Up to 10 searches rewarded today.'
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
      max_searches_mobile = normal_searches_mobile
    
    #--- Create instance of Chrome
    mobile_emulation = { "deviceName": "Google Nexus 5" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
    driver = webdriver.Chrome(chromedriver_location, chrome_options = chrome_options)
    driver.set_window_size(300,300)
    driver.set_window_position(300,300)
    
    #--- Open live.com to login
    driver.get('http://www.live.com')
    email = driver.find_element_by_id("i0116")
    password = driver.find_element_by_id("i0118")
    
    #--- Enter login details and submit
<<<<<<< HEAD
    print ('Account: ', self.email)
=======
    print 'Account: ', self.email
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
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
<<<<<<< HEAD
      print ('Current Points: ',rewards.text)
=======
      print 'Current Points: ',rewards.text
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0

      #--- Find the search bar
      searchbar = driver.find_element_by_id('sb_form_q')
      
      #--- Select everything in the search bar and delete it
      searchbar.clear()
      time.sleep(3)
            
      #--- Generate a random term to search for:
      term = search_terms[random.randrange(0,len(search_terms))]
<<<<<<< HEAD
      print ('Searching for:\t', term)
=======
      print 'Searching for:\t', term
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
      
      try:
        #--- Enter the search term:
        searchbar.send_keys(term,Keys.ENTER)
<<<<<<< HEAD
        self.page_searches += 1
=======
        self.page_searches_mobile += 1
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
        time.sleep(random.randint(5,35))
      
        try:
          #--- Find a link on the page and click it
          link = driver.find_element_by_partial_link_text(term[1:3])
          #print 'Clicking link:\t',link.text
          #link.click()
          #time.sleep(random.randint(10,12))
          #--- Return to previous screen
          #driver.back()
        except:
<<<<<<< HEAD
          print ("No Links")
    
      except:
        print ('Problem searching for the term')
      
      #--- Quit if we've done enough searches
      if self.page_searches >= max_searches_mobile:
        rewards = driver.find_element_by_id('id_rc')
        print ('Current Points: ',rewards.text)        
        print ("Maximum searches of " + str(max_searches_mobile) + " reached, exiting.\n")
        self.page_searches = 0
=======
          print "No Links"
    
      except:
        print 'Problem searching for the term'
      
      #--- Quit if we've done enough searches
      if self.page_searches_mobile >= max_searches_mobile:
        print "Maximum searches of " + str(max_searches_mobile) + " reached, exiting.\n"
>>>>>>> ae784d709227536b85024e2e817abb60eb3377a0
        driver.quit()
        break

if __name__ == "__main__":
  for email,password in credentials:
    bot = account(email,password)
    bot.desktop()
    bot.mobile()
