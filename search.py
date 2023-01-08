text1 = str()
all_links = []
def text_gen():
    
    from googleapiclient.discovery import build
    api_key = 'AIzaSyBD-PHLnR9qYYDHIf8jfS7iIVS3k-wPs-8'
    
    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    search = input('What do you want to search? :')
    result = resource.list(q=search, cx='a5af6ed1b44c046c9').execute()
    # print(result)
    # print(result['items'][0])
    text1 = ""
    for item in result['items']:
#         print(item['title'], item['link'], item['snippet'])
        
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

text_gen()



# Import required module
import newspaper
 
# Assign url
for url in all_links:
    # Extract web data
    url_i = newspaper.Article(url="%s" % (url), language='en')
    url_i.download()
    url_i.parse()
     
    # Display scrapped data
    print(url_i.text)