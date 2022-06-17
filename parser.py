import requests
from bs4 import BeautifulSoup
from config import get_settings
from datetime import date, datetime

feed_url = get_settings().feed_url


def parse_feed() -> tuple[str, date, str]:
    """Fetch latest post from the RSS feed"""
    feed = requests.get(feed_url)

    if feed:
        soup = BeautifulSoup(feed.text, "xml")
        latest_post = soup.find_all("item")[0]
        post_title = latest_post.find("title").text
        post_link = latest_post.find("link").text
        post_date = latest_post.find("pubDate").text
        post_date = datetime.strptime(post_date[:-6], "%a, %d %b %Y %H:%M:%S").date()
        return post_title, post_date, post_link
    else:
        raise SystemExit("Feed couldn't be reached!")
