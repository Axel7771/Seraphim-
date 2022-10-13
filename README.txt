How to run vicebot scripts 

1) Download python 3 (3.9.7 or later)
2) Open command prompt and enter
 

	python --version
	and
	pip --version 

to ensure that python 3 and pip are installed
3) Install Tweepy library
	
	pip install tweepy

4) Ensure that all scripts and text files including "keys.txt" are present, store your api public and secret keys here
5) Ensure that there is a tweet id in "last_seen.txt" and that the ID matches your tweet ID.
You may find the tweet id by visiting a tweet on your brownser the ID will be located at the end of your tweet URL (On browser)
6) Open command line prompt and run:
	
	python 'script_name.py'

7) Create a twitter account and Tweet the following sample tweets (steps 6 and 7 are interchangeable):

	Hello @ACADev77 how are you? #vicebots
	I need some advice @ACADev77 #vicebot_advice
	Reply to this tweet @ACADev77 #vicebots
	@ACADev77 generate a reply #vicebots

if you are testing this on your own twitter bot use their twitter screen_name (@ id)

8) KILL the process 

The purpose of this bot is to use AI practices to generate replies and interact with users based of a collection of keywords pertaining to the topic of programming and technology
If you encounter any issues running this program email: axel.alvarez@ttu.edu 

Future features include
	- syntax detection 
	- advanced text generation using gpt-2 and OpenAI
	- dynamic replies using key phrases
	- database or csv file integration
	

