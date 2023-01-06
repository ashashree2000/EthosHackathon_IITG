from bs4 import BeautifulSoup
import requests

#requesting to website and download HTML content
url = "https://news.abplive.com/news/india/ajmal-kasab-was-smiling-in-jail-had-no-remorse-anjali-kunthe-nurse-26-11-mumbai-attacks-unsc-1569887"
req = requests.get(url)
# content = req.text
# print(content)
content = BeautifulSoup(req.text, "html.parser")
titles = content.find_all('title')
print(titles)
