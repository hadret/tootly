#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from sqlalchemy.sql.sqltypes import Boolean
from database import Base, engine, SessionLocal, Tweet
from parser import parse_feed
from shorty import get_short_link
from tweet import create_tweet

Base.metadata.create_all(bind=engine)


def db_check_record(date: date, title: str) -> Boolean:
    """Check if the record already exists"""
    with SessionLocal() as session:
        query = (
            session.query(Tweet)
            .filter(Tweet.date == date, Tweet.title == title)
            .first()
        )
        return query


def db_insert_data(date: date, title: str, link: str) -> None:
    """Insert new post into the database"""
    if not db_check_record(date, title):

        short_link, admin_link = get_short_link(link)

        with SessionLocal() as session:
            new = Tweet(
                date=date,
                title=title,
                link=link,
                short_link=short_link,
                admin_link=admin_link,
            )
            session.add(new)
            session.commit()
            print("Added new record to the DB!")


def publish_tweet() -> None:
    """Publish Tweet with title and short_link"""
    with SessionLocal() as session:
        query = session.query(Tweet).filter(Tweet.is_published.is_(False)).first()
        if query:
            text = query.title, query.short_link
            text = " ".join(text)
            create_tweet(text)
            query.is_published = True
            session.commit()


if __name__ == "__main__":
    (post_title, post_date, post_link) = parse_feed()
    db_insert_data(post_date, post_title, post_link)
    publish_tweet()
