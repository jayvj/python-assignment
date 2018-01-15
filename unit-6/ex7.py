import requests
from bs4 import BeautifulSoup
try:
    base_url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text,"html.parser")
    all_text = soup.find_all("div", "content")
    for element in all_text:
        print(element.text)
except:
    print("Error Occured..!")
