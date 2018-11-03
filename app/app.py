"""
Website App

Description
-----------
The personal website of Jonathan De Troye

"""
import os
from flask import Flask, render_template, send_from_directory
import pypandoc

app = Flask(__name__)

@app.route("/")
def index():
    posts = generate_html_posts()
    return render_template("index.html", posts=posts)

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

def parse_date(x):
    return x[:10].replace("_", "-")

def parse_title(x):
    return x[11:][:-5].replace("_", " ")

def generate_html_posts():
    posts_list = os.listdir("app/posts")
    md_to_html()
    return [
        (parse_date(x), parse_title(x), x[:-5]) for x in posts_list
    ]

def md_to_html():
    for file in os.listdir("/app/posts"):
        os.system("pandoc --highlight-style pygments -f markdown -t html /app/posts/{} -o /app/posts/{}".format(file, file))

        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')