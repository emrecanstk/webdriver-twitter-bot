from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

tarayici = webdriver.Chrome()

tarayici.get('https://twitter.com/i/flow/login')
time.sleep(7)

eposta = 'testcanstk@gmail.com'
sifre = 'Test2022'
kullanici_adi = "testcan2022"

eposta_giris = tarayici.find_element(By.NAME,'text')
eposta_giris.click()
eposta_giris.send_keys(eposta)
time.sleep(1)
eposta_giris.send_keys(Keys.ENTER)

try:
    sifre_giris = tarayici.find_element(By.NAME,'password')
except:
    time.sleep(2)
    kullanici_adi_giris = tarayici.find_element(By.NAME,'text')
    kullanici_adi_giris.send_keys(kullanici_adi)
    kullanici_adi_giris.send_keys(Keys.ENTER)

time.sleep(3)
sifre_giris = tarayici.find_element(By.NAME,'password')
sifre_giris.click()
sifre_giris.send_keys(sifre)
sifre_giris.send_keys(Keys.ENTER)

time.sleep(7)

liste = tarayici.find_elements(By.CSS_SELECTOR,'.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')

for i in liste:
    if '#' in i.text:
        print(i.text)



# Medium: Twitter Bot | Selenium Webdriver
# Yazar: Emre Can Satık

# Bağlantı: https://medium.com/@emrecanstk/twitter-botu-selenium-webdriver-527699e3cd4f
