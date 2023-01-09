from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request
from newspaper import Article
import newspaper

def sentiment_analysis(sentence):
    # create SentimentIntensityAnalyzer object 
    sid_obj = SentimentIntensityAnalyzer()
    # returns dict with +ve, -ve, neutral, compound
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    # print("Overall sentiment dictionary is : ", sentiment_dict)
    # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    # print("The overall sentence wil be rated as:", end="")
    
    # decide sentiment as positive, negative and neutral
    if (sentiment_dict['compound'] >= 0.04):
        return "Positive"

    elif (sentiment_dict['compound'] <= - 0.04):
        return "Negative"

    else :
        return "Neutral"

# scraping, get links, get passage
all_links = []
def text_gen(search):
    from googleapiclient.discovery import build
    api_key = 'AIzaSyAUxzmrggYiQ4vLvjuCzful3gtAy2hj8XA'
    
    resource = build('customsearch', 'v1', developerKey=api_key).cse()
    result = resource.list(q=search, cx='a5af6ed1b44c046c9').execute()
   
    for item in result['items']:
        link = item['link']
        all_links.append(link)

    return all_links

def get_parsed_news(all_links):
    for url in all_links:
        # Extract web data
        url_i = newspaper.Article(url="%s" % (url), language='en')
        url_i.download()
        url_i.parse()

        # Display scrapped data
        # print(url_i.text)
    return url_i.text

# summary_list = []
# def summarize(all_links):
#     for i in all_links:
#         article = Article(i)
#         article.download()
#         article.parse()
#         article.nlp()
        
# #         print(f'Title: {article.title}')
# #         print(f'Summary: {article.summary}\n')
#         summary_list.append(article.summary)
#     return summary_list

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("text")
        links = text_gen(content)
        parsed_news = get_parsed_news(links)
        # summarized_news = summarize(links)
        sentiment = sentiment_analysis(parsed_news)
        return "The sentiment associated with person you entered: " + sentiment
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)