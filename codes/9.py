# Project: Downloading All XKCD Comics

import os, requests, bs4

url = "https://xkcd.com/"

os.makedirs("../files/xkcd", exist_ok=True)  # store comics in ../files/xkcd

# Step 1: Design the Program

# The URL of the comic’s image file is given by the href attribute of an <img> element.
# The <img> element is inside a <div id="comic"> element.
# The Prev button has a rel HTML attribute with the value prev.
# The first comic’s Prev button links to the https://xkcd.com/# URL, indicating that there are no more previous pages.

# Step 2: Download the Web Page
while not url.endswith("#"):
    # Download the page.
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Step 3: Find and Download the Comic Image.
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = "https:" + comicElem[0].get("src")
        # Download the image.
        print("Downloading image %s..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # Step 4: Save the Image and Find the Previous Comic
    imageFile = open(os.path.join("../files/xkcd", os.path.basename(comicUrl)), "wb")
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")
print("Done.")
