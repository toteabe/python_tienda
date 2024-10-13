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
from fabricante import Fabricante
from producto import Producto

#1. Lista los nombres y los precios de todos los productos de la tabla producto
def test1():

    connection_string = "mysql+mysqlconnector://root:secret@127.0.0.1:3306/tienda"
    engine = create_engine(connection_string, echo=True)

    with Session(engine) as session:
        stmt=select(Fabricante)
        fabricantes=session.scalars(stmt)

        fabs=[]
        for fabricante in fabricantes:
            fabs.append(fabricante)

        stmt=select(Producto)
        productos=session.scalars(stmt)
        prods=[]
        for producto in productos:
            prods.append(producto)

        prods = list(map(lambda p : (p.nombre, p.precio), prods))
        #list comprehension
        prods = [(p.nombre, p.precio) for p in prods]

        for prod in prods:
            print(prod)

test1()