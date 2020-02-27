from sqlalchemy import Column, Integer, String, Float, Numeric, ForeignKey, DateTime
from main import db
import datetime

class Stock(db.Model):
    __tablename__ = 'new_stock'
    id = Column(Integer, primary_key=True)
    inv_id = Column(Integer, ForeignKey('new_inventories.id'))
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)