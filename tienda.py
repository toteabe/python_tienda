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
from sqlalchemy.orm import Session, joinedload
from modelo.fabricante import Fabricante
from modelo.producto import Producto

connection_string = "mysql+mysqlconnector://root:secret@127.0.0.1:3306/tienda"
engine = create_engine(connection_string, echo=True)

def find_all_fabs():
    
    with Session(engine) as session:
        stmt=select(Fabricante).options(joinedload(Fabricante.productos))
        fabricantes=session.scalars(stmt).unique()

        fabs=[f for f in fabricantes]

    return fabs


def find_all_prods():

    with Session(engine) as session:
        stmt=select(Producto).options(joinedload(Producto.fabricante))
        productos=session.scalars(stmt).unique()
    
        prods=[p for p in productos]
        
    return prods;


def test_fabs():

        fabs = find_all_fabs()
    
        fabs_sol_lambda = list(map(lambda f : f.nombre, fabs))
        #list comprehension
        fabs_sol_comprehension = [ f.nombre for f in fabs]

        print(">>fabs_sol_lambda:")
        for f in fabs_sol_lambda:
            print(f)

        print(">>fabs_sol_comprehension:")
        print(fabs_sol_comprehension)

test_fabs()


def testProds():

        prods = find_all_prods()

        prods_sol_lambda = list(map(lambda p : (p.nombre, p.precio), prods))
        #list comprehension
        prods_sol_comprehension = [(p.nombre, p.precio) for p in prods]

        print(">>prods_sol_lambda:")
        for prod in prods_sol_lambda:
            print(prod)

        print(">>prods_sol_comprehension:")
        print(prods_sol_comprehension)
    

# testProds()


#1. Lista los nombres y los precios de todos los productos de la tabla producto
def test1():
    
    prods = find_all_prods()

    nombre_precio = list(map( lambda p : (p.nombre, p.precio), prods ))

    for nom, prec in nombre_precio:
        print( f' {nom} = {prec} €' )


#2. Devuelve una lista de Producto completa con el precio de euros convertido a dólares .
def test2():

    prods = find_all_prods()

    for p in prods:
        print(p)

    def precio_a_dolar(p):
         p.precio = p.precio * 1.09
         return p

    prods_dolar = list(map( precio_a_dolar, prods ))
    for p in prods_dolar:
         print(p)


    prods_dolar_list_comprehension = [precio_a_dolar(p) for p in prods]
    for p in prods_dolar_list_comprehension:
         print(p)
             

# 3. Lista los nombres y los precios de todos los productos, convirtiendo los nombres a mayúscula.             
def test3():
        
    prods = find_all_prods()

    prods_upper_prec = list(map( lambda p: (p.nombre.upper(), p.precio), prods ))

    for nom_prec in prods_upper_prec:
        print(nom_prec)

    prods_upper_prec_lc = [ ( p.nombre.upper(), p.precio ) for p in prods]

    for nom_prec in prods_upper_prec_lc:
            print(nom_prec)

# 4. Lista el nombre de todos los fabricantes y a continuación en mayúsculas los dos primeros caracteres del nombre del fabricante.
def test4():

    fabs = find_all_fabs()

    #nomFabs = list(map( lambda f: (f.nombre, f.nombre[:2].upper()), fabs ))
    nom_fabs = [ (f.nombre, f.nombre[:2].upper()) for f in fabs]
    for nom in nom_fabs:
        print(nom)

# 5. Lista el código de los fabricantes que tienen productos.
def test5():

    fabs = find_all_fabs();

    fabs_con_prods = list( 
        map(
            lambda f: f.codigo,
            filter(lambda f: len(f.productos) >0,
                    fabs)    
        )
     )

    for cod_f in fabs_con_prods:
         print(cod_f)

    assert 7 == len(fabs_con_prods)

    #Ejemplo de List Comprehension
    fabs_con_prods_lc = [ f.codigo for f in fabs if len(f.productos) > 0 ]
    for cod_f in fabs_con_prods_lc:
         print(cod_f)    

    assert 7 == len(fabs_con_prods_lc)
    

if __name__ == "__main__":
    #test1()
    #test2()
    #test3()
    test4()
    #test5()
    print("Everything passed")