"""
Website App

Description
-----------
The personal website of Jonathan De Troye
"""

import os
import logging
import sys
from flask import Flask, render_template, send_from_directory
from app.utilities import parse_date, parse_title, generate_html_posts

logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='[%(asctime)s +0000] [1] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %X'
    )

app = Flask(__name__)


@app.route("/")
def index():
    posts = generate_html_posts()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/static/<file>")
def resources(file):
    return send_from_directory("static", file)


@app.route("/blog")
def blog():
    posts = generate_html_posts()
    posts.reverse()
    # generate_html_posts()
    return render_template("blog.html", posts=posts)


@app.route("/blog/<path>")
def article(path):
    logging.info(path)
    p = "".join([x for x in open("app/posts/" + path + ".html").readlines()])
    return render_template("article.html", article_html=p)


if __name__ == "__main__":
    app.run()
