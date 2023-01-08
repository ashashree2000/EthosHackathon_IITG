from apiclient.discovery import build
api_key = 'AIzaSyBD-PHLnR9qYYDHIf8jfS7iIVS3k-wPs-8'

resource = build('customsearch', 'v1', developerKey=api_key).cse()
search = input('What do you want to search? :')
result = resource.list(q=search, cx='a5af6ed1b44c046c9').execute()
# print(result)
# print(result['items'][0])

for item in result['items']:
    print(item['title'], item['link'], item['snippet']])
