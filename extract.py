from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

import pandas as pd

random_sec = random.uniform(1,3)

title_list = []
likes_list = []
singer_list = []
lyrics_list = []

driver = webdriver.Chrome()
for i in range(20):
    i = i * 50 + 1
    url = "http://www.melon.com/genre/song_list.htm?gnrCode=GN0300#params%5BgnrCode%5D=GN0300&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=NEW&po=pageObj&startIndex={}".format(i)
    driver.get(url)
    for i in range(1, 51):
        try:
            time.sleep(random_sec)
            url2 = "/html/body/div/div[3]/div/div/div[5]/form/div/table/tbody/tr[{}]/td[4]/div/a".format(i)
            element = driver.find_element(By.XPATH, url2)
            element.click()
            title = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[1]/div[1]")
            likes = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[3]/button[1]/span[2]")
            singer = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/form/div/div/div[2]/div[1]/div[2]/a/span[1]")
            lyrics = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div[2]/div")
            print ("{}번째 곡".format(i))
            print ("Title :",title.text)
            #print ("Likes :",likes.text)
            print ("Singer :",singer.text)
            #print ("Lyrics :")
            #print (lyrics.text)
            title_list.append(title.text)
            likes_list.append(likes.text)
            singer_list.append(singer.text)
            lyrics_list.append(lyrics.text)
            driver.back()
            i += 1
        except:
            driver.back()
            i += 1
    driver.back()
    i += 1 

data = {"Title" : title_list,"Likes":likes_list, "Singer":singer_list, "Lyrics":lyrics_list}
df = pd.DataFrame(data)
df.to_csv('songs.csv', index = False)