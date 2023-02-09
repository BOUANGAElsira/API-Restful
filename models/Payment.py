from config import db 

class Payment (db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float, nullable = False)
    type = db.Column(db.String(120), nullable = False)

    ## OneToMany de Order vers payment
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])
