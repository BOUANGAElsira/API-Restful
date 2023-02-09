from config import db

class Item (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    weight = db.Column(db.Float, nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(255), nullable = False)

    ##Fonction permettant d'obtenir le poids
    def getWeight(self):
        return self.weight

    ##Fonction permettant d'obtenir le prix par quantité
    def getPriceForQuantity(self, qty):
        return self.price * qty
