#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import date, datetime
import requests
import sqlite3


db_file = "tweetly.db"
feed_url = "https://chabik.com/feed.xml"
today = date.today()


def parse_feed():
    """Fetch latest post from the RSS feed."""
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


def db_prepare():
    """Prepare database and table."""
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS tweetly
           (date text PRIMARY KEY, title text, link text)"""
    )
    conn.commit()
    conn.close()


def db_insert_data(date, title, link):
    """Insert data into tables, create DB if needed."""
    db_prepare()
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("INSERT INTO tweetly VALUES (?, ?, ?)", (date, title, link))
    conn.commit()
    conn.close()


def db_check_last_record():
    """Check date of the latest record in the DB."""
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT date FROM tweetly ORDER BY date DESC LIMIT 1")
    result_tuple = c.fetchone()
    result = "".join(str(column) for column in result_tuple)
    result = datetime.strptime(result, "%Y-%m-%d").date()
    conn.close()
    return result


def debug_values(date, title, link):
    print(date)
    print(type(date))
    print(title)
    print(type(title))
    print(link)
    print(type(link))


if __name__ == "__main__":
    (post_title, post_date, post_link) = parse_feed()
    # post_date = post_date.strftime("%Y%m%d")
    # debug_values(post_date, post_title, post_link)
    # db_insert_data(post_date, post_title, post_link)
    print(type(db_check_last_record()))
    print(db_check_last_record())
    print(type(post_date))
    print(post_date)
    # print(type(today))
    # print(today)
