from fastapi import APIRouter
from pydantic import BaseModel 
from typing import Literal 
import crud as C

router=APIRouter(prefix="/icecreams"
                 ,tags=['icecreams'])

class IceCream(BaseModel):
    id:int
    name:str
    price:float
    flavour:Literal["chocolate", "vanilla", "caramel"]

class response(BaseModel):
    message:str

@router.post("/create" ,response_model=response)
def store(ic:IceCream):
    C.store(ic)
    return response(message="done")

@router.get("/getall")
def get():
    ice =C.get_all()
    return{
        "message":"done .. ",
        "data":ice
    }

@router.get("/icecreams/flavour/{flavour}")
def flavour(flavour: str):
    items = [item for item in C.get_all() if item.get("flavour") == flavour]
    return {
        "message": "done .. ",
        "data": items
    }

@router.get("/icecreams/price/{max_price}")
def price(max_price: float):
    items = [item for item in C.get_all() if item.get("price", 0) <= max_price]
    return {
        "message": "done .. ",
        "data": items
    }

@router.delete("/delete/{id}")
def delete(id:int):
    C.delete_by_id(id)
    return " done"

@router.put("/update/{id}")
def update(id:int,ic:IceCream):
    print(ic)
    C.update(id,ic)
    return " done"