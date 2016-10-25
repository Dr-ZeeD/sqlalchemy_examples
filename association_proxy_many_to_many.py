#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# All models need to be derived from Base
Base = declarative_base()


# Models definition
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return 'User({})'.format(self.name)


def main(argv):
    parser = ArgumentParser(description='A minimum example for SQLAlchemy.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='run verbose')
    args = parser.parse_args(argv[1:])

    # We need to start the session
    engine = create_engine('sqlite:///:memory:', echo=args.verbose)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(User(name='steve'))
    session.add(User(name='john'))
    session.commit()

    for user in session.query(User).all():
        print(user)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
