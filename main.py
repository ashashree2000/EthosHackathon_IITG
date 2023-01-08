from flask import Flask, render_template, request

from googleapiclient.discovery import build


api_key = 'AIzaSyAUxzmrggYiQ4vLvjuCzful3gtAy2hj8XA'
app = Flask(__name__)

resource = build('customsearch', 'v1', developerKey=api_key).cse()


@app.route('/', methods=['GET', 'POST'])
def Index():
    if request.method == "POST":
        # getting input from search in HTML form
        search = request.form.get("srch")

        result = resource.list(q=search, cx='a5af6ed1b44c046c9').execute()

        all_links = []
        all_snippets = []
        for item in result['items']:
            #         print(item['title'], item['link'], item['snippet'])
            snippet = item['snippet']
            links = item['link']
            all_links.append(links)
            all_snippets.append(snippet)

#         print(links)

#     text1 = print(text1.replace('.', ''))
#     text1 = print(text1.replace('"', ''))
#     text1 = print(text1.replace("'", ''))
#     text1 = print(text1.replace('"', ''))
        return render_template('results.html', context=all_links)
    # return render_template('results.html', context='result')

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)