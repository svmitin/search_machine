"""Инициализация библиотеки по работе с бд"""
import os
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, relationship
from sqlalchemy import types, Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy.dialects import postgresql as dtypes
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

from constants import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

Base = declarative_base()
ENGINE = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
metadata = MetaData()
DBSession = Session(bind=ENGINE)


class Mixin():
    
    def save(self) -> Boolean:
        try:
            DBSession.commit()
            return True
        except (sqlalchemy.exc.IntegrityError, sqlalchemy.exc.PendingRollbackError) as error:
            # already exists
            DBSession.rollback()
        return False

    def add(self):
        DBSession.add(self)
        if self.save():
            DBSession.refresh(self)


class Site(Mixin, Base):
    """Домены. Для будущей аналитики и другого функционала будем сохранять все известные нам доменые имена"""
    __tablename__ = 'search_sites'

    id = Column(Integer, nullable=False, primary_key=True)
    url = Column(Text(), nullable=False, unique=True)
    integration_hash = Column(Text(), nullable=False, unique=True)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.url}'


class Word(Mixin, Base):
    """Initialize words table"""
    __tablename__ = 'search_words'

    id = Column(Integer, nullable=False, primary_key=True)
    word = Column(Text(), nullable=False, unique=True)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return self.word


class Page(Mixin, Base):
    __tablename__ = 'search_pages'

    id = Column(Integer, nullable=False, primary_key=True)
    site_id = Column(types.Integer, ForeignKey('search_sites.id', ondelete='SET NULL'), nullable = True, comment = 'Сайт страницы')
    url = Column(Text(), nullable=False, unique=True)
    title = Column(Text())
    description = Column(Text())
    keywords = Column(Text())
    status_code = Column(Integer(), default=500)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    updated = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    site = relationship('Site', foreign_keys = [site_id])

    def __repr__(self):
        return self.url


class WordsInPages(Mixin, Base):
    __tablename__ = 'search_words_in_pages'

    id = Column(Integer, nullable=False, primary_key=True)
    words = Column(dtypes.ARRAY(types.Integer), nullable = False)
    page_id = Column(Integer, ForeignKey("search_pages.id"))
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return self.word


class Link(Mixin, Base):
    __tablename__ = 'search_links'

    id = Column(Integer, nullable=False, primary_key=True)
    url = Column(Text(), nullable=False, unique=True)
    text = Column(Text(), default=False)                        # Текст ссылки
    page = Column(Text(), nullable=False, unique=True)          # Страница, на которой ссылка была встречена
    visited = Column(Boolean, default=False)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    crawler_name = Column(Text(), default='crawler_1')
    debug = Column(Text(), default=False)

    def __repr__(self):
        return f'{self.url} {self.text} {self.page}'


class SitesQueue(Mixin, Base):
    __tablename__ = 'search_sites_queue'

    id = Column(Integer, nullable=False, primary_key=True)
    url = Column(Text(), nullable=False, unique=True)
    visited = Column(Boolean, default=False)
    crawler_name = Column(Text(), nullable=True, default=None)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.url}'
