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
    return [
        (parse_date(x), parse_title(x), x[:-5]) for x in posts_list
    ]