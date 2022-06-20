# define seperotr
def seperator():
    print()
    print("<=======================================================================================================================>")

## If you want to scrape a Website ##
#     1. Use The Official API of The Website Owner
#     2. HTML Web Scraping using Some Tools Like bs4

## Installing all the Required Packages ##
# pip install requests -> Install Requests Module
# pip install html5lib -> Install html5lib Module
# pip install bs4 -> Install bs4 Module

## Use of Packages ##
# Request: Scrap Website
# html5lib: Parse Website
# bs4: Used for Using Scraped Website Code

# Importing all the libraies
import requests
from bs4 import BeautifulSoup, NavigableString

url = "https://praddyumnyadav.github.io/Chocolate-Cake-Recipe-HTML./"
url2 = "https://codewithharry.com"
url3 = "https://www.udemy.com"
url4 = "https://www.facebook.com/thechotapacket"

# Welcome for web scraping
print("<======================================================> Web Scraping <======================================================>")
# step 1: Get The HTML
r = requests.get(url2)
r2 = requests.get(url)
htmlContent = r.content
htmlContent2 = r2.content

# step 2: Parse The HTML
soup = BeautifulSoup(htmlContent, "html.parser")
soup2 = BeautifulSoup(htmlContent2, "html.parser")

# step 3: HTML Tree traversal
# Commonly used types of objects in BeautifulSoup:
#     1. Tag
#     2. NavigableString
#     3. BeautifulSoup
#     4. Comment

# Get the title of HTML Page
print("-> Get Title of The HTML Page")
title = soup.title
print(title.string)

# Get all the pragraphs in this page
paras = soup.find_all("p")

# Get all the anchor tags of this page
anchors = soup.find_all("a")

# Get all the links of page
seperator()
print("All Links of The HTML Page .")
allLinks = set()
for link in anchors:
    if link.get("href") != "#":
        allLinks.add(url2 + link.get("href"))

for link in allLinks:
    print(link)

# Get First Element in the HTML Page
seperator()
print("-> Find First Paragraph tag form HTML Page .")
print(soup.find("p"))

# Get Class of any element in the HTML Page
seperator()
print("-> Get Class of any Element in HTML Page")
print(soup.find("p")["class"])

# Find all the elements with class lead
seperator()
print("-> find the paragraph whose class is lead")
print(soup.find_all("p", class_="lead"))

# Get the text from tags/soup
seperator()
print("-> Find Text of Paragraph")
print(soup.find("p").get_text())

# All Text Without Tags of the Page
seperator()
print("-> All Text Without Tags of The Page")
print(soup.get_text())

# All Main Content Of This Page
seperator()
print("-> All Main Content .")
AllMainContent = soup2.find(class_="content")
for element in AllMainContent.children:
    print(element)

# Parent of MainContent
seperator()
print("-> Print Parent of Main Content")
for item in AllMainContent.parents:
    print(item)
