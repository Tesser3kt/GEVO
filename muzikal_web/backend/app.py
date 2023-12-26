from re import A
from flask import Flask, render_template, send_from_directory
from config import TEMPLATE_FOLDER, STATIC_FOLDER, NEWS_MAX_CHAR
from database import Navigation, About, Title, Footer, News, NewsList, NewsContainer
from datetime import datetime

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_pyfile("config.py")


@app.route("/")
def hello_world():
    news = list(sorted(NewsList.news, key=lambda x: x.date, reverse=True))
    for new in news:
        excerpt = ""
        for word in new.text.split():
            if len(excerpt) < NEWS_MAX_CHAR:
                excerpt += word + " "
            else:
                break
        if len(excerpt) > NEWS_MAX_CHAR:
            excerpt += "..."
        new.text = excerpt

    context = {
        "page_title": "At zije LEnka VasatkOva",
        "date": Title.date,
        "title": Title.title,
        "subtitle": Title.subtitle,
        "links": Navigation.links,
        "link_count": len(Navigation.links),
        "about_text": About.text,
        "about_heading": About.heading,
        "copyright": Footer.copyright,
        "news_heading": NewsContainer.news_heading,
        "news": news,
    }
    return render_template(
        "main_page.html",
        **context,
    )

@app.route("/navigation.js")
def serve_navigation():
    return send_from_directory(STATIC_FOLDER, "navigation.js")
