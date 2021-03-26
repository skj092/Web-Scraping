# downloading web pages using requests module
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# data type
print(type(res))

# To see whether the download succeeded (method1)
print(res.status_code==requests.codes.ok)

# To see whether the download succeeded (method2)
print(res.raise_for_status())

print(len(res.text))

print(res.text[:100])