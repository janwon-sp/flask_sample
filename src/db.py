import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id   = Column(Integer(), primary_key=True)
    name = Column(String())
    age  = Column(Integer())

    def fetch_all(session):
        users = session.query(User)
        return users

    def fetch_by_age(session,age):
        users = session.query(User).filter(User.age > age)
        return users

    def fetch_by_name(session, name):
        search = '%{}%'.format(name)
        users = session.query(User).filter(User.name.like(search))
        # おなじ
        #users = session.query(User).filter(User.name.like('%%%s%%' % name))
        return users

def main():
    engine = create_engine('sqlite:////db/sample1.db', echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    users = User.fetch_all(session)
    for user in users:
        print(user.name, user.age)
    print('===============')
    users = User.fetch_by_age(session,20)
    for user in users:
        print(user.name, user.age)
    print('===============')
    users = User.fetch_by_name(session, 'とも')
    for user in users:
        print(user.name, user.age)

if __name__ == "__main__":
    main()