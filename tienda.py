#INSTALACION
#sudo apt install pip
#sudo apt install python3.12-venv
#python3.12 -m venv env
#source env/bin/activate
#pip list
#pip install mysql-connector-python
#pip install SQLAlchemy
#pip list
#pip freeze > requirements.txt
#Ctrl+Shift+P 
#   > Python: Select Interpreter
#       ./env/bin/python

#Si exportas el código en zip y quieres reinstalar las dependencias en otro dir:
#pip install -r requirements.txt

#Para desactivar el virtual environment venv:
#deactivate

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelo.fabricante import Fabricante
from modelo.producto import Producto


def findAllFabs():
    connection_string = "mysql+mysqlconnector://root:secret@127.0.0.1:3306/tienda"
    engine = create_engine(connection_string, echo=True)

    with Session(engine) as session:
        stmt=select(Fabricante)
        fabricantes=session.scalars(stmt)

        fabs=[f for f in fabricantes]

    return fabs


def findAllProds():
    connection_string = "mysql+mysqlconnector://root:secret@127.0.0.1:3306/tienda"
    engine = create_engine(connection_string, echo=True)

    with Session(engine) as session:
        stmt=select(Producto)
        productos=session.scalars(stmt)
    
        prods=[p for p in productos]
        
    return prods;


def testFabs():

        fabs = findAllFabs()
    
        fabsSolLambda = list(map(lambda f : f.nombre, fabs))
        #list comprehension
        fabsSolComprehension = [ f.nombre for f in fabs]

        print(">>fabsSolLambda:")
        for f in fabsSolLambda:
            print(f)

        print(">>fabsSolComprehension:")
        print(fabsSolComprehension)

testFabs()


def testProds():

        prods = findAllProds()

        prodsSolLambda = list(map(lambda p : (p.nombre, p.precio), prods))
        #list comprehension
        prodsSolComprehension = [(p.nombre, p.precio) for p in prods]

        print(">>prodsSolLambda:")
        for prod in prodsSolLambda:
            print(prod)

        print(">>prodsSolComprehension:")
        print(prodsSolComprehension)
    

testProds()


#1. Lista los nombres y los precios de todos los productos de la tabla producto
def test1():
    pass