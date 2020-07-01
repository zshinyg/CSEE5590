from bs4 import BeautifulSoup
from requests import get
import os

html = get("https://en.wikipedia.org/wiki/Google")
bsObj = BeautifulSoup(html.content,"html.parser")

with open(os.path.join('Python_Lesson7/',"input.txt"), mode='w') as file:
    file.write(bsObj.getText())