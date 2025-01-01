# main.py
from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    html_content = file.read()
    # Now you can work with the html_content variable
    # print(html_content)  # Example of working with the content

soup = BeautifulSoup(html_content, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)