from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import json


def link_scraper(link):
    root = "https://google.com/"
    # link = "https://www.google.com/search?q=shah+rukh+khan&rlz=1C1CHBF_enIN967IN967&biw=963&bih=836&tbm=nws&sxsrf=AJOqlzVotgMvDYaG4h5RSPj6ro5co2WoNw%3A1673027158602&ei=Vl64Y7amJMOYseMPpuyAsA8&oq=shah+&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQARgAMgoIABCxAxCDARBDMggIABCABBCxAzIICAAQgAQQsQMyBwgAELEDEEMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BAgAEEM6CAgAELEDEIMBOgUIABCRAlDWBFjNCmDwFmgBcAB4AYAB7gGIAeoKkgEFMC40LjOYAQCgAQHAAQE&sclient=gws-wiz-news"
    
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    # print(webpage)
    
    # making requested page readable
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        # print(soup)
    link_list = []
    for item in soup.find_all('div', attrs={'class': 'X7NTVe'}):
        raw_link = (item.find("a", href=True)['href'])
        link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
        
        # title = (item.find('div', attrs={'class': 'BNeawe deIvCb AP7Wnd'}).get_text)
        # print(title)
        # print(item)
        # print(link)
        link_list.append(link)
    return link_list
link_list = link_scraper("https://www.google.com/search?q=shah+rukh+khan&rlz=1C1CHBF_enIN967IN967&biw=963&bih=836&tbm=nws&sxsrf=AJOqlzVotgMvDYaG4h5RSPj6ro5co2WoNw%3A1673027158602&ei=Vl64Y7amJMOYseMPpuyAsA8&oq=shah+&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQARgAMgoIABCxAxCDARBDMggIABCABBCxAzIICAAQgAQQsQMyBwgAELEDEEMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BAgAEEM6CAgAELEDEIMBOgUIABCRAlDWBFjNCmDwFmgBcAB4AYAB7gGIAeoKkgEFMC40LjOYAQCgAQHAAQE&sclient=gws-wiz-news")
jsonstring = json.dumps(link_list)
print(jsonstring)



#text scraping
# requesting to website and download HTML content
# link_scraper()
def title_scraper():
    for url in link_list:
    #     # url = "https://news.abplive.com/news/india/ajmal-kasab-was-smiling-in-jail-had-no-remorse-anjali-kunthe-nurse-26-11-mumbai-attacks-unsc-1569887"
        req = requests.get(url)
        content = req.text
    #     # print(content)
        content = BeautifulSoup(req.text, "html.parser")
        titles = list(content.find_all('title'))
        print(titles)
       
    return titles


print(title_scraper())

