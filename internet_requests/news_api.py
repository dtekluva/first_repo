import requests

response = requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-01&sortBy=publishedAt&apiKey=e360f2ac87ca4582b35b8e98776777b9")

data = response.json()

articles = data["articles"]

for i in articles:
    print(i["title"])
    print()