from base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Fabricante(Base):
    __tablename__ = 'fabricante'

    codigo = Column(Integer, primary_key=True, autoincrement=True,)
    nombre = Column(String(100), nullable=False)

    # Define the reverse relationship with the `Producto` class
    productos = relationship('Producto', back_populates='fabricante')

    def __str__(self):
        return f"Fabricante(codigo={self.codigo}, nombre='{self.nombre}')"