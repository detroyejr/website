"""
Utilities
"""

import os

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