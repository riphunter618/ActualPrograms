from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

n = int(input('Enter no of messages'))
per = input('Enter the name of the person you want to terrorise')
msg = input('Enter the message')
br = webdriver.Chrome()
br.get('https://web.whatsapp.com/')
time.sleep(20)
search = br.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
search.send_keys(per)
search.send_keys(Keys.ENTER)
time.sleep(10)
text = br.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
time.sleep(5)
for a in range(n):
    text.send_keys(msg)
    text.send_keys(Keys.ENTER)
    time.sleep(0.5)
