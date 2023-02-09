from config import db
from models.Payment import Payment

class Check (Payment):
    __tablename__ = 'check'
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    bankId = db.Column(db.String(120), nullable = False)
    type = db.Column(db.String(120), nullable = False, default='check')

    ##Méthode authorized()
    def authorized(self):
        if (self.name == self.bankId):
            self.authorized = True
        else:
            self.authorized = False