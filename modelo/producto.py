from modelo.base import Base
from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = 'producto'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Double, nullable=False)
    codigo_fabricante = Column(Integer, ForeignKey('fabricante.codigo', ondelete='CASCADE'), nullable=False)

    # Define the relationship with the `Fabricante` class
    fabricante = relationship('Fabricante', back_populates='productos')

    def __str__(self):
        return f"Producto(codigo={self.codigo}, nombre='{self.nombre}', precio={self.precio}, codigo_fabricante={self.codigo_fabricante})"