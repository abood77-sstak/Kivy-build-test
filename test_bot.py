
from selenium import webdriver
import telebot
from time import sleep

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--proxy-server=https://34.140.150.176:3128')
    driver = webdriver.Chrome(options=options)
    return driver

my_token = "6517080417:AAHQx2gxkQ5Sxs2GilTyCaOI4-jJZfIGaho"
chat_id =7031532556
bot = telebot.TeleBot(my_token)
for i in range(5):
  driver = web_driver()
  driver.get("https://google.com")
  sleep(5)
  photo = driver.save_screenshot("screenshot.png")
  with open("screenshot.png", "rb") as photo:
   bot.send_photo(chat_id, photo)
  driver.quit()
