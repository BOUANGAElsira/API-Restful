from config import db
from models.Payment import Payment

class Cash (Payment):
    __tablename__ = 'cash'
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key = True)
    cashTendered = db.Column(db.Float, nullable = False)
    type = db.Column(db.String(120), nullable = False, default='cash')
