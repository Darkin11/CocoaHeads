from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects import postgresql
import logging
from flask import Flask, render_template

#this part enables SQL logging to the console- comment it out to disable
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('postgresql+psycopg2://agentm:x@localhost/cocoaheads')
Session = sessionmaker(bind=engine)
Base = declarative_base(metadata=MetaData(schema='cocoaheads'))
session = Session()

class GroupManager(Base):
	__tablename__ = 'groupmanager'

	id = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	realname = Column(String, nullable=False)
	isadmin = Column(Boolean, nullable=False)
	email = Column(String, nullable=False)
	password = Column(String, nullable=False)

class Group(Base):
	__tablename__ = 'group'
 
	id = Column(Integer, primary_key=True)
	intro = Column(String, nullable=False)
	cityid = Column(Integer, ForeignKey('city.id'), nullable=False)
	city = relationship('City', backref=backref('group', uselist=False))
	managerid = Column(Integer, ForeignKey('groupmanager.id'), nullable=False)
	enabled = Column(Boolean, default=True)
	groupmanager = relationship("GroupManager", backref=backref("group", uselist=False))
	events = relationship("Event", backref="group")

class City(Base):
	__tablename__ = 'city'

	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	timezonename = Column(String, nullable=False)
	countryid = Column(String(2), ForeignKey('country.isocode'), nullable=False)
	country = relationship('Country', backref='city')

class Country(Base):
	__tablename__ = 'country'

	isocode = Column(String(2), nullable=False, primary_key=True)
	name = Column(String, nullable= False)

class Event(Base):
	__tablename__ = 'event'

	id = Column(Integer, primary_key=True)
	groupid = Column(Integer, nullable=False)
	#got rid of "" around location
	location = Column(String, nullable=False)
	locationdetails = Column(String, nullable=False)
	startdate = Column(DateTime(timezone=True))
	enddate = Column(DateTime(timezone=True))
	#double? can I use Float?
	longitude = Column(Float, nullable=False, default=0)
	latitude = Column(Float, nullable=False, default=0)
	group_id = Column(Integer, ForeignKey('group.id'))

app = Flask('myapp', template_folder=".")

@app.route("/")
def GM_list():
    q = session.query(GroupManager)
    return render_template("groupmanager.html", GroupManagers=q)

if __name__ == "__main__":
    app.run()


