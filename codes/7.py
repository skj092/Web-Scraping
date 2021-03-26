# Creating a BeautifulSoup Object from HTML

import requests, bs4

# downlaoding html page from the url
res = requests.get("https://nostarch.com/")

# To see whether the download succeeded
print(res.raise_for_status())

# Creating BeautifulSoup object from html
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")

# data type
print(type(noStarchSoup))


# Finding an Element with the select() Method

# finding title using title tag
pagetitle = noStarchSoup.select("title")

# title data type
print("dtype : ", type(pagetitle))

# printing
print(pagetitle)
