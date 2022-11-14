from config import get_settings
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(get_settings().db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    date = Column(String, unique=True, index=True)
    title = Column(String, unique=True, index=True)
    link = Column(String, index=True)
    short_link = Column(String, unique=True, index=True)
    admin_link = Column(String, unique=True, index=True)
    is_published = Column(Boolean, default=False)
    is_tooted = Column(Boolean, default=False)
