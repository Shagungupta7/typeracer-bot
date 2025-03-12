import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up ChromeDriver
chromedriver_path = r"C:\webdrivers\chromedriver-win32\chromedriver-win32\chromedriver.exe"  
service = Service(chromedriver_path)
options = Options()


# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)
# Open TypeRacer
driver.get('https://play.typeracer.com/')

time.sleep(5)
pyautogui.hotkey('ctrl', 'alt','i')
time.sleep(2)

text_container = driver.find_element(By.CSS_SELECTOR, ".podContainer.medium.gameView")
text = text_container.text.split("\n")
print(type(text))
print(text[-3])
time.sleep(13)

pyautogui.typewrite(text[-3], interval = 0.01)
time.sleep(15)
driver.quit()