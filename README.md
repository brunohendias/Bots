<div align="center">

### Welcome to the Bot World

### Cooffeh Bot

### This project can provide you bots to use, customize, study...

</div>

# Features
- Easy Youtube video download sending the video link
- Download the thumbnails to the instagram posts sending the link
- Generate one long and strong random password
- Generate QRCode sending "qrcode https://github.com/brunohendias"
- Download Video on website sending the website link

# Features comming soon
- steganography (injecting bytes on image file)
- get news on the globo.com
- Automation test
- Covert any text into audio
- Send email

<br>

# Requirements

### To run the cooffeh telegram bot you need:
- Docker or Python
- Python version 3
- Pip (Python package manager)
- Obs: I recommend to run with docker, to make things more easy

### Pip packages on the cooffeh telegram bot:
- [Pyrogram](https://pypi.org/project/Pyrogram/) To create the telegram bot
- [TgCrypto](https://pypi.org/project/TgCrypto/) To make fast the script
- [python-dotenv](https://pypi.org/project/python-dotenv/) To load the env variables
- [jurigged](https://pypi.org/project/jurigged/) To autoload the project
- [pytube](https://pypi.org/project/pytube/) To Download the videos on youtube
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) To Interact with HTML
- [requests](https://pypi.org/project/requests/) To get things with links
- [Pillow](https://pypi.org/project/Pillow/) To Interact with Image files
- [scrapingant-client](https://docs.scrapingant.com) To render html on external server
- [pyshorteners](https://pypi.org/project/pyshorteners/) To short the link

<br>

# Running with docker

Install Docker and Docker compose openning this link [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Run these codes on the cooffeh folder:
```
docker-compose build
docker-compose up -d
```

<br>

# Running with python

Install python openning this link [Python Download](https://www.python.org/downloads/)

### Run these codes:

### Open the Docker folder and run: 
```
pip install -r requirements.txt
```

### On the root folder of the project run
```
jurigged -v run.py
```

<br>


# Configuring

First do you need to set up the .env variables

Go to the [bots](https://core.telegram.org/bots) link and follow the steps

Then set the variables on .env file with the values

Now your bot work!

<br>

# Contributing

This is a MIT open source code that you can feel free to contributing, use to your own project, replicate the code, create your own bot, improve the bot with pull requests.

- Just clone the repository, create a new branch with the feature/fix name, do your changes, test the code manually, and then create the pull request

- Obs: I'm implementting the selenium to run automation test

<br>

# Community support

This project don't have a community but you can talk with me on my socials
- [Discord](https://discord.gg/xUwQtJPBSP)
- [Instagram](https://www.instagram.com/bbrrunoh/)
- [Github](https://github.com/brunohendias)
- [Me](https://t.me/cooffeh_bot)

<br>

# License

It's a MIT license project

For more information see the [LICENSE file](https://github.com/brunohendias/Bots/blob/main/LICENSE)
