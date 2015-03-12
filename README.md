Bing Search Bot V1.0
=============================

Earns Rewards Points for Bing
	
	Last Modified: 3/12/2015

	Forked from: Jeff Henry's Bing Search Bot V1.0 (https://github.com/JeffHenry/Bing-Search-Bot)

	
	This bot uses the selenium library to search for items using bing.
	Accumulates rewards points for bing rewards.
	PC browsers can only get 15 points a day.
	
	How to use:
		- Install selenium using pip 'pip install -U selenium'
		- Download chromedriver to working directory  -> https://sites.google.com/a/chromium.org/chromedriver/downloads
		- Register an email with live.com and with bing rewards prior to using the bot
		- Run and enjoy the benefits 'python bing.py'
		

	Feel free to change the search_terms or add to the code.
	Edit email and password to individual login information.
	
  V1.0
  
	- Initial Commit
	- Successfully accumulates 15 points in a few minutes
	- Prints out current point count

  V1.1 Updates:
	- Handles if current weekday is tuesday of may, which means more points!

  V1.2 Updateos:
	- Removed link clinking, switched to chromedriver in preparation for mobile search update.

  V1.3 Updates:
	- Added the abilty to have email and password outside of file in accounts.txt

  V1.4 Updates:
	- Added mobile search emulation! 
	- Moved search options for future parameterization.

