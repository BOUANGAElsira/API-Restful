from config import db
from models.Payment import Payment

class WireTransfer (Payment):
    __tablename__ = 'wire_transfer'
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key = True)
    bankId = db.Column(db.String(120), nullable = False)
    bankName = db.Column(db.String(120), nullable = False)
    type = db.Column(db.String(120), nullable = False, default='wire_transfer')
