#Write a simple program that parse a Wiki page 
#mentioned below and follow the instructions:
#https://en.wikipedia.org/wiki/Deep_learning
#Print out the title of the page
#Find all the links in the page (‘a’ tag)
#Iterate over each tag(above) then return the link using attribute "href" using get
#Save all the links in the file#

from requests import get
from bs4 import BeautifulSoup
import os


html = get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(html.content, "html.parser")




file = open("Prob2_Results.txt", 'w')

link_containers = bsObj.find_all('a')

print(bsObj.title.string)

for link in link_containers:
    file.write(str(link.get('href')))
    file.write("\n")

file.close()









