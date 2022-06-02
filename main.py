#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
from sqlalchemy import select
from config import get_settings
from database import Base, engine, SessionLocal, Tweet

today = date.today()
feed_url = get_settings().feed_url
Base.metadata.create_all(bind=engine)


def parse_feed() -> tuple:
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


def db_insert_data(date: date, title: str, link: str) -> None:
    """Insert data into tables, create DB if needed"""
    with SessionLocal() as session:
        new = Tweet(date=date, title=title, link=link)
        session.add(new)
        session.commit()


def db_check_last_record() -> date:
    """Check date of the latest record in the DB"""
    session = SessionLocal()
    result = session.execute(select(Tweet.date).order_by(Tweet.date.desc()).limit(1))
    result = result.fetchone()
    result = datetime.strptime(result[0], "%Y-%m-%d").date()
    return result


def debug_values(date: date, title: str, link: str):
    print(date)
    print(type(date))
    print(title)
    print(type(title))
    print(link)
    print(type(link))


if __name__ == "__main__":
    (post_title, post_date, post_link) = parse_feed()
    post_date = post_date.strftime("%Y-%m-%d")
    debug_values(post_date, post_title, post_link)
    # db_insert_data(post_date, post_title, post_link)
    # print(type(db_check_last_record()))
    print(db_check_last_record())
    # print(type(post_date))
    # print(post_date)
    # print(type(today))
    # print(today)
