from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://google.com/"
link = "https://www.google.com/search?q=shah+rukh+khan&rlz=1C1CHBF_enIN967IN967&biw=963&bih=836&tbm=nws&sxsrf=AJOqlzVotgMvDYaG4h5RSPj6ro5co2WoNw%3A1673027158602&ei=Vl64Y7amJMOYseMPpuyAsA8&oq=shah+&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQARgAMgoIABCxAxCDARBDMggIABCABBCxAzIICAAQgAQQsQMyBwgAELEDEEMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BAgAEEM6CAgAELEDEIMBOgUIABCRAlDWBFjNCmDwFmgBcAB4AYAB7gGIAeoKkgEFMC40LjOYAQCgAQHAAQE&sclient=gws-wiz-news"

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
# print(webpage)

# making requested page readable
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    # print(soup)

for item in soup.find_all('div', attrs={'class': 'X7NTVe'}):
    raw_link = (item.find("a", href=True)['href'])
    link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
    
    # title = (item.find('div', attrs={'class': 'BNeawe deIvCb AP7Wnd'}).get_text)
    # print(title)
    # print(item)
    print(link)