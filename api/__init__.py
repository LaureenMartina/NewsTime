import random
import webbrowser
import mimetypes, urllib

import requests

from api.Article import Article


def is_url_image(url):
    mimetype, encoding = mimetypes.guess_type(url)
    return mimetype and mimetype.startswith('image')

def check_url(url):
    try:
        headers = {
            "Range": "bytes=0-10",
            "User-Agent": "MyTestAgent",
            "Accept": "*/*"
        }

        req = urllib.Request(url, headers=headers)
        response = urllib.urlopen(req)
        return response.code in range(200, 209)
    except Exception as ex:
        return False

def is_image_and_ready(url):
    return is_url_image(url) and check_url(url)


if __name__ == '__main__':

    key = "8df18dcd35f649e3843d25920cdab720"
    sources = ["le-monde", "google-news-fr", "hacker-news", "liberation", "metro", "lequipe", "les-echos"]
    mode = ["top-headlines", "everything"]
    language = ["fr", "us", "gb", "de"]
    choice_scr = 0
    choice_mode = 0
    articles = []

    """ Choix du journal """

    print("Journaux disponibles: Le Monde, Google News, Hacker News, Liberation, Metro, L'Equipe et Les Echos")

    while True:
        choice_scr = int(input("Veuillez sélectionner votre journal (n° 0-6): "))
        if type(choice_scr) == int:
            if 0 <= choice_scr <= 6:
                break
        else:
            print('AttributeError: not a integer')

    """ Choix du mode """

    print("Mode Sélection Articles disponibles: Top-Headlines, Everything")

    while True:
        choice_mode = int(input("Veuillez sélectionner le mode de sélection (n° 0-1): "))
        if type(choice_mode) == int:
            if choice_mode >= 0 and choice_mode < 2:
                break
        else:
            print('AttributeError: not a integer')

    url = ('https://newsapi.org/v2/{}?'
           'sources={}&'
           'apiKey={}').format(mode[choice_mode], sources[choice_scr], key)

    response = requests.get(url)
    data = response.json()

    """ recuperer tous les articles disponibles """
    for art in data["articles"]:
        articles.append(art)

    """ recuperer toutes les données accessibles depuis un article """
    print(random.randint(0, len(articles)))
    info = articles[random.randint(0, len(articles))]

    name = info["source"]["name"]
    author = info["author"]
    title = info["title"]
    descrip = info["description"]
    link = info["url"]

    if is_image_and_ready(info["urlToImage"]):
        img = info["urlToImage"]
    else:
        img = ""

    date = info["publishedAt"]

    """ Creation des Articles """
    news = Article(name, author, title, descrip, link, img, date)
    print(news)

    """ Ecriture et Affichage des informations dans le browser """

    file = open('articleView.html', 'w+')

    view = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html;charset="UTF-8"/>
            <link rel="stylesheet" href="style.css" />
            <title>NewspaperLand</title>
        </head>
        <body style="background-image: url('paper.jpg')">
            <div style="width: 800px;background-color: #6A6967;text-align:center;margin-left: 385px;
                color: wheat;font-family: fantasy;font-size: -webkit-xxx-large;padding-bottom: 10px; padding-top: 10px
                ;margin-top: 60px">
                    %s
            </div>
            <div style="width: 800px;background-color: #AE2431;text-align:center;font-family:Algerian;margin-left: 385px;
                padding-bottom: 10px; padding-top: 10px;margin-top: 10px;color: white;font-size: 20px">
                    <h3 id="title"> %s </h3>
            </div>
            <div style="background-color: #AFAAA4;background-color: #AFAAA4;width: 800px;margin-left: 385px;
                margin-top: 10px;padding-bottom: 10px;">
                <div>
                    <img src="%s" alt="image correspondant à l'article" style="width:500px;">
                    <div style="float: right;">
                        <p id="author" style="float: right;margin-right: 10px"> %s </p>
                        <p style="float: right;margin-right: 115px"><i> %s </i></p>
                    </div>
                </div>
                <p style="font-family: Verdana"> %s </p>
            <a href="%s"> %s </a>
            </div>
            
        </body>
    </html>
    """ % (news.get_newspaper(), news.get_title(), news.get_urlImage(), news.get_author(), news.get_published()[0:10], news.get_description(),
           news.get_link(), news.get_link())

    file.write(view)
    file.close()

    # Change path to reflect file location
    fileHTML = 'D:\PyCharmProjects\\' + 'articleView.html'
    webbrowser.open_new_tab('articleView.html')
