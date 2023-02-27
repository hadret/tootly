import re
import textwrap
from datetime import date, datetime

import requests
from bs4 import BeautifulSoup
from config import get_settings

feed_url = get_settings().feed_url
tags = get_settings().tags


def parse_feed() -> tuple[str, date, str, str, str]:
    """Fetch latest post from the RSS feed"""
    feed = requests.get(feed_url)

    if feed:
        soup = BeautifulSoup(feed.text, "xml")
        latest_post = soup.find_all("item")[0]
        post_title = latest_post.find("title").text
        post_link = latest_post.find("link").text
        post_date = latest_post.find("pubDate").text
        post_date = datetime.strptime(post_date, "%a, %d %b %Y %H:%M:%S %Z").date()
        post_content = latest_post.find("content:encoded").text
        post_tags = [f"#{tag}" for tag in tags if re.search(tag, post_content)]
        post_tags = " ".join(post_tags[:8])
        post_content = textwrap.shorten(
            BeautifulSoup(post_content, "lxml").text, width=200
        )
        return post_title, post_date, post_link, post_tags, post_content
    else:
        raise SystemExit("Feed couldn't be reached!")
