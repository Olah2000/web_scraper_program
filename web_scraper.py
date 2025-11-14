from urllib.request import urlopen
import re as regex


#Cleaner version
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern_1 = "<title.*?>.*?</title.*?"
search_operand = regex.search(pattern_1, html, regex.IGNORECASE)
title = search_operand.group()

print(title)


