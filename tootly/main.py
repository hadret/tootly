#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from parser import parse_feed

from database import Base, SessionLocal, Toot, engine
from shorty import get_short_link
from sqlalchemy.sql.sqltypes import Boolean
from toot import create_toot

Base.metadata.create_all(bind=engine)


def db_check_record(date: date, title: str) -> Boolean:
    """Check if the record already exists"""
    with SessionLocal() as session:
        query = (
            session.query(Toot).filter(Toot.date == date, Toot.title == title).first()
        )
        return query


def db_insert_data(date: date, title: str, link: str, tags: str, content: str) -> None:
    """Insert new post into the database"""
    if not db_check_record(date, title):
        short_link, admin_link = get_short_link(link)

        with SessionLocal() as session:
            new = Toot(
                date=date,
                title=title,
                link=link,
                short_link=short_link,
                admin_link=admin_link,
                tags=tags,
                content=content,
            )
            session.add(new)
            session.commit()
            print("Added new record to the DB!")


def publish_toot() -> None:
    """Toot with title and short_link"""
    with SessionLocal() as session:
        query = session.query(Toot).filter(Toot.is_tooted.is_(False)).first()
        if query:
            text = query.title, query.content, query.short_link, query.tags
            title, content, link, tags = text
            link = "\U0001F517 " + link
            text = (title, content, link, tags)
            text = "\n\n".join(x for x in text if x)
            create_toot(text)
            query.is_tooted = True
            session.commit()


if __name__ == "__main__":
    (post_title, post_date, post_link, post_tags, post_content) = parse_feed()
    db_insert_data(post_date, post_title, post_link, post_tags, post_content)
    publish_toot()
    print("Job well done!")
