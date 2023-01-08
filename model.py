import os
import matplotlib.pyplot as plt

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
import newspaper

# scraping, get links, get passage
all_links=[]
def text_gen():
    from googleapiclient.discovery import build
    api_key = 'AIzaSyAUxzmrggYiQ4vLvjuCzful3gtAy2hj8XA'
    
    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    search = input('What do you want to search? :')
    result = resource.list(q=search, cx='a5af6ed1b44c046c9').execute()
    # print(result)
    # print(result['items'][0])
    text1 = str()
    for item in result['items']:
#   print(item['title'], item['link'], item['snippet'])
        
        snippet = item['snippet']
        text1 = text1 + snippet
        links = item['link']
        all_links.append(links)
#         print(links)
    
#     text1 = print(text1.replace('.', ''))
#     text1 = print(text1.replace('"', ''))
#     text1 = print(text1.replace("'", ''))
#     text1 = print(text1.replace('"', ''))
    return all_links

    # scrape the urls obtained
text_gen()
def get_parsed_news(all_links):
    for url in all_links:
        # Extract web data
        url_i = newspaper.Article(url="%s" % (url), language='en')
        url_i.download()
        url_i.parse()

        # Display scrapped data
#         print(url_i.text)
    return url_i.text
parsed_news = get_parsed_news(all_links)


# function for sentimental analysis

def sentiment_analysis(sentence):
    # create SentimentIntensityAnalyzer object 
    sid_obj = SentimentIntensityAnalyzer()
    # returns dict with +ve, -ve, neutral, compound
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    print("The overall sentence wil be rated as:", end="")
    
    # decide sentiment as positive, negative and neutral
    if (sentiment_dict['compound'] >= 0.04):
        print("Positive")

    elif (sentiment_dict['compound'] <= - 0.04):
        print("Negative")

    else :
        print("Neutral")
        
# driver code
if __name__ == "__main__":
    print("program starts")
    # text_gen()
    sentiment_analysis(parsed_news)