from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("F:/Nitish/coding/Python/PRO-C127 web_scraping/virtual/chromedriver.exe")

browser.get(START_URL)
time.sleep(10)

stars_data = []

def scrape():
    
    soup = BeautifulSoup(browser.page_source , "html.parser")
    table = soup.find("table" , attrs={"class" , "wikitable"})
    tbody = table.find("tbody")
    tr = tbody.find_all("tr")
    
    for each_tr in tr:
        td = each_tr.find_all("td")
        temp_list = []
        for each_td in td:
            data = each_td.text.strip()
            temp_list.append(data)
        
        stars_data.append(temp_list)

            
scrape()
print(stars_data[0])
yo = []

for i in range(0 , len(stars_data)):
    name = stars_data[i][1]
    distance = stars_data[i][3]
    mass = stars_data[i][5]
    radius = stars_data[i][6]
    lum = stars_data[i][7]

    yah = [name , distance , mass , radius , lum]
    yo.append(yah)


headers = ["star_name" , "distance" , "mass" , "radius" , "luminosity"]
star_df = pd.DataFrame(yo , columns=headers)
star_df.to_csv("stars.csv" , index = True , index_label="id")