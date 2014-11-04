from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, PickleType, ForeignKey 
from sqlalchemy import sessionmaker, relationship, backref, scoped_session

ENGINE = create_engine("sqlite:///checkins.db", echo=False)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

######################
# CLASS DECLARATIONS #
######################

class Attraction(Base):
	__tablename__ = "attractions"

	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	checkin_id = Column(Integer, nullable = True)

class Checkin(Base):
	pass

class User(Base):
	pass

# END CLASS DECLARATIONS #
##########################



def main():
	pass

if __name__ == "__main__":
	main()