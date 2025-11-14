from urllib.request import urlopen
import urllib.error
import re as regex
from bs4 import BeautifulSoup as Soup



#function for taking in website and making a beautiful soup object. The return can be used to be passed into other bs methods
def souper(grabbed_url):
    try:
        open_page = urlopen(grabbed_url)
        raw_html = open_page.read().decode()
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
        print("Error: unable to fetch page.")
        return None

    return Soup(raw_html, 'html.parser')

def link_getter(soup_obj):
    list_of_links = []

    for tag in soup_obj.find_all('a'):
        if 'href' in tag.attrs:
            list_of_links.append(tag['href'])

    return list_of_links

def img_getter(soup_obj):
    list_of_imgs = []

    for tag in soup_obj.find_all('img'):
        if 'src' in tag.attrs:
            list_of_imgs.append(tag["src"])

    return list_of_imgs
