from sqlalchemy import Column, Integer, String, Float, Numeric, ForeignKey, DateTime
from main import db

class Inventories(db.Model):
    __tablename__ = 'new_inventories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    type = Column(String, nullable=False)
    buying_price = Column(Integer)
    selling_price = Column(Integer)

    stock = db.relationship('Stock', backref='inventories', cascade='all,delete-orphan', lazy=True)
    sales = db.relationship('Sales', backref='inventories', cascade='all,delete-orphan', lazy=True)
    sales = db.relationship('Sales',cascade='all,delete-orphan')
    stock = db.relationship('Stock',cascade='all,delete-orphan')