from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.python.org/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
tags = soup.find("div", class_="blog-widget")

d_list = []
for tag in tags.find_all("li"):
    tag_url = tag.find("a").get("href")

    sleep(1)

    tag_r = requests.get(tag_url)
    tag_soup = BeautifulSoup(tag_r.content, "lxml")
    tag_h2 = [h2.text for h2 in tag_soup.find_all("h2")]
    d = {
        "date": tag.find("time").text,
        "title": tag.find("a").text,
        "url": tag_url,
        "tag_h2": tag_h2
    }
    d_list.append(d)

df = pd.DataFrame(d_list)
print(df)

df.to_csv("python_web_tag.csv", index=None, encoding="utf-8-sig")
#df.to_excel("python_web_tag.xlsx", index=None, encoding="utf-8-sig")

#加筆3