from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    registered_on = Column(DateTime, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    group_number = Column(Integer, ForeignKey('groups.group_number'))
    

    def __init__(self, username, email, password, registered_on, admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.registered_on = registered_on
        self.admin = admin

    def __repr__(self):
        return f'<User {self.username!r}>'

class Group(Base):
    __tablename__ = 'groups'

    group_number = Column(Integer, primary_key=True)
    group_members = relationship("User", backref="groups")

    def __init__(self, group_number):
        self.group_number = group_number

    def __repr__(self):
        return f'<Group {self.group_number!r}>'

# >>> parent = Parent()
# >>> child = Child()
# >>> child.parent = parent
# >>> print(parent.children)
# [Child(...)]