"""
Website App

Description
-----------
The personal website of Jonathan De Troye

"""
import os
from flask import Flask, render_template, send_from_directory
import pypandoc
from utilities import parse_date, parse_title, generate_html_posts, md_to_html

app = Flask(__name__)

@app.route("/")
def index():
    posts = generate_html_posts()
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/images/<file>")
def images(file):
    return send_from_directory("images", file)

@app.route("/blog")
def blog():
    posts = generate_html_posts()
    # generate_html_posts()
    return render_template("blog.html", posts=posts)

@app.route("/blog/<path>")
def article(path):
    p = "".join([x for x in open("app/posts/" + path + ".html").readlines()])
    return render_template("article.html", article_html=p)

        
if __name__ == '__main__':
    app.run(host='0.0.0.0')
