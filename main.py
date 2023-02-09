from app import app
from config import db
from models import Customer, Order, OrderDetail, OrderStatus, Item, Payment, Credit, Cash, Check, WireTransfer
from models.Cash import Cash
from models.Check import Check
from models.Customer import Customer
from models.Credit import Credit
from models.Item import Item
from models.Order import Order
from models.OrderDetail import OrderDetail
from models.OrderStatus import OrderStatus
from models.Payment import Payment 
from models.WireTransfer import WireTransfer
from flask import Flask, request, jsonify, render_template

with app.app_context():
    db.create_all()

#======================================================POST===============================================

#Methode d'ajout de customer

@app.route('/customer/add', methods = ['POST'])
def customer_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']

        if name and deliveryAddress and contact and active and request.method == 'POST':
           
            print(" ****************** ")
            customers = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)
            db.session.add(customers)
            db.session.commit()
            resultat = jsonify('Customer added with succes')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout de order

@app.route('/order/add', methods = ['POST'])
def order_add():
    try:
        json = request.json
        print(json)
        createDate = json['createDate']

        if createDate and request.method == 'POST':
           
            print("******************")
            orders = Order(createDate = createDate)

            db.session.add(orders)
            db.session.commit()
            resultat = jsonify('Order add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout de orderStatus

@app.route('/orderStatus/add', methods = ['POST'])
def orderstatus_add():
    try:
        json = request.json
        print(json)
        CREATE = json['CREATE']
        SHIPPING = json['SHIPPING']
        DELIVERED = json['DELIVERED']
        PAID = json['PAID']

        if CREATE and SHIPPING and DELIVERED and PAID and request.method == 'POST':
           
            print("******************")

            orderStatus = OrderStatus(CREATE = CREATE, SHIPPING = SHIPPING, DELIVERED = DELIVERED, PAID = PAID)

            db.session.add(orderStatus)
            db.session.commit()
            resultat = jsonify('Order Status add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout de orderDetail

@app.route('/orderDetail/add', methods = ['POST'])
def orderdetail_add():
    try:
        json = request.json
        print(json)
        qty = json['qty']
        taxStatus = json['taxStatus']

        if qty and taxStatus and request.method == 'POST':
           
            print("******************")

            orderDetail = OrderDetail(qty = qty, taxStatus = taxStatus)

            db.session.add(orderDetail)
            db.session.commit()
            resultat = jsonify('New Order Detail add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#Methode d'ajout de item

@app.route('/item/add', methods = ['POST'])
def item_add():
    try:
        json = request.json
        print(json)
        weight = json['weight']
        description = json['description']
        price = json['price']

        if weight and description and price and request.method == 'POST':
           
            print("******************")

            item = Item(weight = weight, description = description, price = price)

            db.session.add(item)
            db.session.commit()
            resultat = jsonify('New Item add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#Methode d'ajout de payement

@app.route('/payment/add', methods = ['POST'])
def payment_add():
    try:
        json = request.json
        print(json)
        amount = json['amount']

        if amount and request.method == 'POST':
           
            print("******************")
            payments = Payment(amount = amount)

            db.session.add(payments)
            db.session.commit()
            resultat = jsonify('New Payment add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#Methode d'ajout de credit

@app.route('/credit/add', methods = ['POST'])
def credit_add():
    try:
        json = request.json
        print(json)
        number = json['number']
        types = json['types']
        expireDate = json['expireDate']

        if number and types and expireDate and request.method == 'POST':
           
            print("******************")

            credits = Credit(number = number, types = types, expireDate = expireDate)

            db.session.add(credits)
            db.session.commit()
            resultat = jsonify('New Credit add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout de cash

@app.route('/Cash/add', methods = ['POST'])
def cash_add():
    try:
        json = request.json
        print(json)
        cashTendered = json['cashTendered']

        if cashTendered and request.method == 'POST':
           
            print("******************")
            
            cashs = Cash(cashTendered = cashTendered)

            db.session.add(cashs)
            db.session.commit()
            resultat = jsonify('New Cash add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#Methode d'ajout de check

@app.route('/check/add', methods = ['POST'])
def check_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        bankID = json['bankID']

        if name and bankID and request.method == 'POST':
           
            print("******************")
            
            checks = Check(name = name, bankID = bankID)

            db.session.add(checks)
            db.session.commit()
            resultat = jsonify('New Check add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#Methode d'ajout de wiretransfer

@app.route('/wiretransfer/add', methods = ['POST'])
def wiretransfer_add():
    try:
        json = request.json
        print(json)
        bankID = json['bankID']
        bankName = json['bankName']

        if bankID and bankName and request.method == 'POST':
           
            print("******************")
            
            wiretransfer = WireTransfer(bankID = bankID, bankName = bankName)

            db.session.add(wiretransfer)
            db.session.commit()
            resultat = jsonify('New Wire Transfer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()




#======================================================GET===============================================

##GET de customer

@app.route('/customer', methods = ['GET'])
def get_all_customer():
    try:
        customers = Customer.query.all()
        data = [{"id":customer.id, "name":customer.name, "deliveryAdress":customer.deliveryAdress, "contact":customer.contact, "active":customer.active} for customer in customers]
        
        resultat = jsonify({"status_code": 200, "customer" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

##GET de order
@app.route('/order', methods = ['GET'])
def get_all_order():
    try:
        orders = Order.query.all()
        data = [{"id":order.id, "createDate": order.createDate} for order in orders]

        resultat = jsonify({"status_code": 200, "order" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

##GET de orderStatus
@app.route('/orderStatus', methods = ['GET'])
def get_all_orderStatus():
    try:
        orderStatus = OrderStatus.query.all()
        data = [{"id":orderStatu.id, "CREATE": orderStatu.CREATE, "SHIPPING":orderStatu.SHIPPING, "DELIVERED":orderStatu.DELIVERED, "PAID":orderStatu.PAID} for orderStatu in orderStatus]

        resultat = jsonify({"status_code": 200, "orderStatu" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


##GET de orderDetail
@app.route('/orderDetail', methods = ['GET'])
def get_all_orderDetail():
    try:
        orderDetails = Order.query.all()
        data = [{"id":orderDetail.id, "qty": orderDetail.qty, "taxStatus":orderDetail.taxtStatus} for orderDetail in orderDetails]

        resultat = jsonify({"status_code": 200, "orderDetail" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

##GET de item
@app.route('/item', methods = ['GET'])
def get_all_item():
    try:
        items = Order.query.all()
        data = [{"id":item.id, "weight":item.weight, "description": item.description, "price":item.price} for item in items]

        resultat = jsonify({"status_code": 200, "item" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


##GET de payement
@app.route('/payement', methods = ['GET'])
def get_all_payement():
    try:
        payements = Order.query.all()
        data = [{"id":payement.id, "amount": payement.amount} for payement in payements]

        resultat = jsonify({"status_code": 200, "payement" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


##GET de credit
@app.route('/credit', methods = ['GET'])
def get_all_credit():
    try:
        credits = Order.query.all()
        data = [{"id":credit.id, "number": credit.number, "type":credit.type, "expireDate":credit.expireDate} for credit in credits]

        resultat = jsonify({"status_code": 200, "credit" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


##GET de cash
@app.route('/cash', methods = ['GET'])
def get_all_cash():
    try:
        cashs = Order.query.all()
        data = [{"id":cash.id, "cashTendered": cash.cashTendered} for cash in cashs]

        resultat = jsonify({"status_code": 200, "cash" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


##GET de chek
@app.route('/chek', methods = ['GET'])
def get_all_chek():
    try:
        cheks = Order.query.all()
        data = [{"id":chek.id, "name": chek.name,"bankId":chek.bankId} for chek in cheks]

        resultat = jsonify({"status_code": 200, "chek" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


##GET de wireTansfer
@app.route('/wireTansfer', methods = ['GET'])
def get_all_wireTansfer():
    try:
        wireTansfers = Order.query.all()
        data = [{"id":wireTansfer.id, "bankId": wireTansfer.bankId, "bankName":wireTansfer.bankName} for wireTansfer in wireTansfers]

        resultat = jsonify({"status_code": 200, "wireTansfer" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


if(__name__ == '__main__'):
    app.run()