from urllib.request import urlopen
import re as regex
from bs4 import BeautifulSoup as Soup

#function for taking in website and making a beautiful soup object. The return can be used to be passed into other bs methods
def souper(grabbed_url):
    open_page = urlopen(grabbed_url)
    raw_html = open_page.read().decode()

    return Soup(raw_html, 'html.parser')

def link_getter(soup_obj):
    list_of_links = []

    for tag in soup_obj.find_all('a'):
        list_of_links.append(tag['href'])

    return list_of_links

def img_getter(soup_obj):
    list_of_imgs = []

    for tag in soup_obj.find_all('img'):
        list_of_imgs.append(tag["src"])

    return list_of_imgs


#file1 = open(r"C:\Users\OLAHg\Desktop\web_scraper\stored_image_sources.txt", "w+")




#print(img_getter(souper("https://www.pinterest.com/ideas/wallpapers/951361127909/")))


#image_list = souper.find_all("img")
#print(image_source)

#pattern_1 = "<title.*?>.*?</title.*?"
#search_operand = regex.search(pattern_1, html, regex.IGNORECASE)
#title = search_operand.group()




