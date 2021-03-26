# downloading web pages using requests module
import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# data type
print(type(res))

# successfully downloaded or not
print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:100])
