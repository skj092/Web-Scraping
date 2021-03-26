# Project 1: Create a list of all the books on the url "https://nostarch.com/"

# importing the libraries
import requests, bs4

# downloading web page
res = requests.get("https://nostarch.com/")

# creating a beautifulsoup object from html
soup = bs4.BeautifulSoup(res.text, "html.parser")

# all the book are with the <h2> tag and inside <a> tag (look at the files>booklist.PNG)
atags = soup.select("h2 a")

# booklist is the list containing all <a> tag
Books = []
for atag in atags:
    Books.append(atag.text)

# Final Book List
print(Books)
