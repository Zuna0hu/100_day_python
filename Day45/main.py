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

all_anchor_tags = soup.find_all(name="a")

# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# how to find an element using name and id
heading = soup.find(name="h1", id="name")
print(heading.getText())

# how to find an element using name and class
section_heading = soup.find(name="h3", class_="heading") # as class is a reserved keyword in Python
print(section_heading.get("class"))
