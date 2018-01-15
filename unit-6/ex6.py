import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")
def NewYorkTimes():
    for titles in soup.find_all(class_="story"):
        title = titles.a
        try:
            print(title.string)
        except AttributeError:
            print("AttributeError Found..!")
NewYorkTimes()

