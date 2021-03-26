# Saving downloaded file into hard drive

import requests

# downloading web page
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# To see whether the download succeeded 
print(res.raise_for_status())

# creating a text file
playFile = open('RomeoAndJuliet.txt', 'wb')

# appending text from res to playFile
for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()