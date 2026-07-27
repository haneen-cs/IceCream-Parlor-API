from sqlalchemy import create_engine ,Column ,String ,Integer , Float ,Enum
from sqlalchemy.orm import declarative_base 
database_url="sqlite:///icecreams.db"


engine=create_engine(database_url)
print(engine)
base = declarative_base()


class IceCream(base):
    __tablename__='icecreams'
    id= Column(Integer , primary_key=True ,autoincrement=True)
    name= Column(String)
    price=Column(Float)
    flavour=Column(Enum("chocolate", "vanilla", "caramel"))


base.metadata.create_all(engine)
