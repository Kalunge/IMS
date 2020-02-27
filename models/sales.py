from sqlalchemy import Column, Integer, String, Float, Numeric, ForeignKey, DateTime
from main import db
import datetime

class Sales(db.Model):
    __tablename__ = 'new_sales'
    id = Column(Integer, primary_key=True)
    inv_id = Column(Integer, ForeignKey('new_inventories.id'))
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)