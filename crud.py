from dbtest import engine, IceCream
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def store(ic):
    db = Session()
    ice = IceCream(name=ic.name, price=ic.price, flavour=ic.flavour)
    db.add(ice)
    db.commit()
    db.close()

def get_all():
    db = Session()
    icecreams = db.query(IceCream).all()
    ices = []
    for st in icecreams:
        ice = {
            'id': st.id,  
            'name': st.name,
            'price': st.price,
            'flavour': st.flavour
        }
        ices.append(ice)
    db.close()
    return ices

def delete_by_id(id: int):
    db = Session()
    ic = db.query(IceCream).filter(IceCream.id == id).first()
    if ic: 
        db.delete(ic)
        db.commit()
    db.close()
    return "done"

def update(id: int, ice):
    db = Session()
    ic = db.query(IceCream).filter(IceCream.id == id).first()
    if ic:
        ic.name = ice.name
        ic.price = ice.price
        ic.flavour = ice.flavour
        db.commit()
    db.close()
    return "done"