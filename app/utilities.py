"""
Utilities
"""

import os

def parse_date(x):
    """get the date from a file name"""
    return x[:10].replace("_", "-")

def parse_title(x):
    """get the title from a file name"""
    return x[11:][:-5].replace("_", " ")

def generate_html_posts():
    """create a list of articles that are passed into flask"""
    posts_list = os.listdir("app/posts")
    md_to_html()
    return [
        (parse_date(x), parse_title(x), x[:-5]) for x in posts_list
    ]

def md_to_html():
    """use pandoc to convert markdown to html"""
    for file in os.listdir("/app/posts"):
        os.system("pandoc --highlight-style pygments -f markdown -t html /app/posts/{} -o /app/posts/{}".format(file, file))