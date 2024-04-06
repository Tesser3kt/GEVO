from flask import (
    Flask,
    render_template,
    send_from_directory,
    request,
    redirect,
    session,
)
from flask_sqlalchemy import SQLAlchemy
from config import TEMPLATE_FOLDER, STATIC_FOLDER, NEWS_MAX_CHAR
from datetime import datetime
import hashlib

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_pyfile("config.py")

db = SQLAlchemy()
db.init_app(app)

from models import *


@app.template_filter("news_id")
def news_id(news_id):
    return f"/news/{news_id}"


@app.route("/")
def hello_world():
    title = Title.query.first()
    news_list = News.query.all()
    navigation = Link.query.all()
    image_list = Image.query.all()
    about = About.query.first()
    news = list(sorted(news_list, key=lambda x: x.date, reverse=True))
    news_excerpts = {}

    for new in news:
        excerpt = ""
        for word in new.text.split():
            if len(excerpt) < NEWS_MAX_CHAR:
                excerpt += word + " "
            else:
                break
        if len(excerpt) > NEWS_MAX_CHAR:
            excerpt += "..."
        news_excerpts[new.id] = excerpt

    context = {
        "page_title": "J.A.K.",
        "date": title.date,
        "title": title.title,
        "subtitle": title.subtitle,
        "links": navigation,
        "link_count": len(navigation),
        "about_text": about.text,
        "about_heading": about.heading,
        "about_image": about.image,
        "news": news,
        "news_excerpts": news_excerpts,
        "imagelist": image_list,
    }
    return render_template(
        "main_page.html",
        **context,
    )


@app.route("/news/<int:id>")
def news_detail(id: int):
    new = News.query.filter_by(id=id).first()
    navigation = Link.query.all()
    context = {
        "page_title": "Novinky",
        "links": navigation,
        "link_count": len(navigation),
        "new": new,
    }

    return render_template(
        "news.html",
        **context,
    )


@app.route("/login")
def login():
    links = Link.query.all()
    context = {
        "page_title": "صفحة تسجيل الدخول",
        "links": links,
        "link_count": len(links),
    }
    return render_template("login.html", **context)


@app.post("/login")
def auth():
    if request.method != "POST":
        return "Method not allowed", 405

    username = request.form.get("username")
    password = request.form.get("password")

    if username is None or password is None:
        return "Missing username or password", 405

    db_user = User.query.filter_by(username=username).first()
    if db_user is None:
        return "User not found", 405

    hash = hashlib.sha256()
    hash.update(password.encode())
    password = hash.hexdigest()
    if db_user.password != password:
        return "Falsches Passwort", 405

    session["user"] = username
    return redirect("/admin")


@app.post("/title")
def update_title():
    if "user" not in session:
        return redirect("/login")

    title = Title.query.first()
    title.title = request.form.get("title")
    title.subtitle = request.form.get("subtitle")
    date = request.form.get("date")
    title.date = datetime.fromisoformat(date)
    db.session.add(title)
    db.session.commit()
    return redirect("/admin")


@app.post("/about")
def update_about():
    if "user" not in session:
        return redirect("/login")

    about = About.query.first()
    about.heading = request.form.get("heading")
    about.text = request.form.get("text")
    about.image = request.form.get("image")

    db.session.add(about)
    db.session.commit()
    return redirect("/admin")


@app.post("/news/<int:id>")
def update_news(id: int):
    if "user" not in session:
        return redirect("/login")
    news = News.query.filter_by(id=id).first()
    news.title = request.form.get("title")
    news.text = request.form.get("text")
    news.author = request.form.get("author")
    news.date = datetime.now()
    news.image = request.form.get("image")
    db.session.add(news)
    db.session.commit()
    return redirect("/admin")


@app.route("/admin")
def admin():
    if "user" not in session:
        return redirect("/login")
    title = Title.query.first()
    about = About.query.first()
    links = Link.query.all()
    news_list = News.query.all()
    news = list(sorted(news_list, key=lambda x: x.date, reverse=True))

    context = {
        "page_title": "Admin",
        "links": links,
        "link_count": len(links),
        "about": about,
        "title": title.title,
        "subtitle": title.subtitle,
        "date": title.date,
        "news": news,
    }
    return render_template("admin.html", **context)


@app.route("/navigation.js")
def serve_navigation():
    return send_from_directory(STATIC_FOLDER, "navigation.js")


@app.route("/flowbite.min.js")
def serve_flowbite():
    return send_from_directory(
        "../frontend/node_modules/flowbite/dist/", "flowbite.min.js"
    )
