import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
import telebot
# import time



# driver = webdriver.Edge()

token = '6388955939:AAFrszEHJpfDMZfJyn2i0xU_vNPGT-_lEFk'
botusername = '@scrapwebass_bot'

scraper = telebot.TeleBot(token=token)


url = 'https://linkupaddis.com/publications/'
response = requests.get(url)
content = response.content



def stuff():
    soup = BeautifulSoup(content, "html.parser")
    posters = soup.find_all("div", class_="v-image v-responsive v-carousel__item theme--dark")
    titles = soup.find_all("div", class_="v-list-item__content")

    # title = soup.find("title")
    # print(title.text)

    for i in range(len(posters)):
        # Get the div that contains the poster
        poster_container= posters[i].find("div", class_="v-image__image v-image__image--preload v-image__image--cover")

        # get url from poster container style
        poster_url = poster_container["style"]
        poster_url = poster_url.split("(")[1].split(")")[0].replace('"', '')
        print(poster_url)
        print(titles[i].text)
        print("=" * 50)

        # scraper.send_message(chat_id='@linkupposters', text=titles[i])

        
        scraper.send_photo(chat_id='@linkupposters', photo=poster_url , caption=titles[i])
        scraper.send_photo(chat_id=467630144, photo=poster_url , caption=titles[i])
        # time.sleep(3)
      
        


        
        
while True:
    
    stuff()
    time.sleep(3)
