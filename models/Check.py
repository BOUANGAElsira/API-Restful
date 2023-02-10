from config import db
from models.Payment import Payment

class Check (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    bankId = db.Column(db.String(120), nullable = False)
  
    _mapper_args_ = {
        'polymorphic_identity': 'credit',
    }

    ##Méthode authorized()
    def authorized(self):
        if (self.name == self.bankId):
            self.authorized = True
        else:
            self.authorized = False