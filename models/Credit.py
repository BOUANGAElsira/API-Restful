from config import db
from models.Payment import Payment

class Credit (Payment):
    __tablename__ = 'credit'
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key = True)
    number = db.Column(db.String(120), nullable = False)
    type = db.Column(db.String(120), nullable = False, default='credit')
    expireDate = db.Column(db.Date, nullable = False)
