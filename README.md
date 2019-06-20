<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://image.flaticon.com/icons/png/512/8/8800.png" alt="Bot logo"></a>
</p>

<h1 align="center">:smiley: Random Happy Bot :smiley:</h1>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![Platform](https://img.shields.io/badge/platform-twitter-1DA1F2.svg)](https://www.twitter.com/RandomHappyBot)
  [![GitHub Issues](https://img.shields.io/github/issues/AshuK650/Random_Happy_Face.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/AshuK650/Random_Happy_Face.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
 ![Last Commit](https://img.shields.io/github/last-commit/AshuK650/Random_Happy_Face.svg)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> This is a simple bot that creates tweets a happy face of emojis every day at about 12 PM EST. One emoji will be used for the eyes and the other will be used for the mouth. 
    <br> 
</p>

## 📝 Table of Contents
+ [About](#about)
+ [How it works](#working)
+ [Usage](#usage)
+ [Getting Started](#getting_started)
+ [Deploying your own bot](#deployment)
+ [Built Using](#built_using)
+ [Authors](#authors)
+ [Acknowledgments](#acknowledgement)

## 🧐 About Random Happy Face<a name = "About"></a>
The purpose of this bot is rather simple as to entertain your Twitter feed by sending out a simple smiley face made of emojis that will contain two randomly selected emojis that will be used for the eyes and mouth. 

This bot is set up to tweet at 12 PM every day. This bot will hopefully soon be developed to allow for this bot to be able to tweet multiple times of the day at random times of the day. 
![About](https://i.gifer.com/B4IU.gif)

## 💭 How it works<a name = "working"></a>

This bot first creates a string using a template that will create a smiley face using a dictionary of every emoji with the name and the unicodes for it in the file [unicode_codes.py](https://github.com/AshuK650/Random_Happy_Face/blob/master/unicode_codes.py) which will be converted into a list to allow randomization of selection. 

The Tweet will be made into a string in the file [tweet.py](https://github.com/AshuK650/Random_Happy_Face/blob/master/tweet.py). This file has a function that is dedicated to getting the randomly selected emojis from [unicode_codes.py](https://github.com/AshuK650/Random_Happy_Face/blob/master/unicode_codes.py). After getting the names and the unicodes of the two emojis, it will then use Python's replace string methods to place the emojis and names into the template. 

To get the login credentials as found in [credentials.py](https://github.com/AshuK650/Random_Happy_Face/blob/master/credentials.py), it will read a text file set up in the format as [credentials_example.txt](https://github.com/AshuK650/Random_Happy_Face/blob/master/credentials_example.txt) but should be ranamed to credentials.txt to avoid an error in [credentials.py](https://github.com/AshuK650/Random_Happy_Face/blob/master/credentials.py)

Those three files will then all congregate into the main file [main.py](https://github.com/AshuK650/Random_Happy_Face/blob/master/main.py) where it will use Tweepy where it will get the credentials and use them to authenticate the bot as a user and then send the tweet using Tweepy. 

The entire bot is written in Python 3.7.1

## 🎈 Usage <a name = "usage"></a>

To use the bot, type into the bash console:
```bash
python main.py 
```

The bot will output this: 
```python
# meaning the tweet execution was successful 
"Execution Complete: No Errors"  
```
or this: 
```python 
# in the brackets, the error found will be put in as a string 
"Here's the problem: {}"
```

### Example:
``` bash
python main.py 
```
**Tweet Example:**
[Here](https://twitter.com/RandomHappyBot/status/1140366150645235712)

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

To make use of Tweepy, you have to install it from the bash console by typing one of the following into your terminal.

Easy Install: 
```bash
pip install tweepy 
```

From Github: 
```bash 
git clone https://github.com/tweepy/tweepy.git
cd tweepy 
python setup.py install 
```

## 🚀 Deployment <a name = "deployment"></a>
To deploy my bot, I used a site called [**PythonAnywhere**](https://pythonanywhere.com) to host my code to run 24/7. In PythonAnywhere, I made use of the **Tasks** tabs to run my code once a day at 16:00 UTC (12 PM EST) everyday. 

In order for PythonAnywhere to be able to use Tweepy, you must instal it by creating a console and using one of the methods found in [Getting Started](#getting_started).

In the Tasks tab, when asked for bash command line to execute at your desired time, I put the following 
``` bash
python main.py
```

## ⛏️ Built Using <a name = "built_using"></a>
+ [Spyder](https://www.spyder-ide.org/) - Python IDE 
	+ Note: Use any IDE that you are comfortable with
+ [PythonAnywhere](https://www.pythonanywhere.com/) - Online Python code hosting and editing 

## ✍️ Authors <a name = "authors"></a>
+ [@AshuK650](https://github.com/AshuK650) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
+ [This article was very helpful and has source code too.](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39)
+ [Tweepy Documentation](http://docs.tweepy.org/en/latest/index.html) 
+ [Python 3.7.1 Documentation](https://docs.python.org/3/)

<sup>If there are any issues with a bot, contact me [here](https://twitter.com/AshuKher)</sup>
<sup>Want to check out other stuff that I made? Check my [GitHub](https://github.com/AshuK650)</sup>