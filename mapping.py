from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, MetaData
from sqlalchemy.orm import sessionmaker

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

for gm in session.query(GroupManager).filter(GroupManager.realname.like('%John%')):
	print gm.realname


class Group(Base):
	__tablename__ = 'group'
 
	id = Column(Integer, primary_key=True)
	intro = Column(String, nullable=False)
	cityid = Column(Integer, primary_key=True)
	managerid = Column(Integer, primary_key=True)
	enabled = Column(Boolean, default=True)

class City(Base):
	__tablename__ = 'city'

	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	timezonename = Column(String, nullable=False)
	#is character(2) the same as String(2)?
	countryid = Column(String(2), nullable=False)

class Country(Base):
	__tablename__ = 'country'

	isocode = Column(String(2), nullable=False)
	name = Column(String, nullable= False)


class Event(Base):
	__tablename__ = 'event'

	id = Column(Integer, primary_key=True)
	groupid = Column(Integer, primary_key=True)
	#got rid of "" around location
	location = Column(String, nullable=False)
	locationdetails = Column(String, nullable=False)
	startdate = Column(DateTime(timezone=True))
	enddate = Column(DateTime(timezone=True))
	#double? can I use Float?
	longitude = Column(Float, nullable=False, default=0)
	latitude = Column(Float, nullable=False, default=0)

