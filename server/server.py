import json
import datetime

'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",)
def view_form():
    return render_template('../index.html')

@app.route("/order_get", method=["POST"])
def handle_get():
    if request.method == 'GET':
        desk = request.args['desk']
        food_name = request.args['food-name']
        return '<h1>your order! </h1>' + food_name + "at desk:" + desk
    else:
        return render_template('../index.html')
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''
class Product(object):
    def __init__(self):
        self.date = datetime.datetime.now()
        self.availibility = 1
        self.products = dict()

    def add_product(self,name, quantity):
        self.products[name] = name
        self.products[quantity] = quantity
        
 # Index on-stage characters using their charid

class Desk(object):
    numbers = 3

    def __init__(self):
        self.numbers = 0 # TODO: ADD
class Order(object):
    def __init__(self): #TODO: add desk and finsihed
        self.number = Desk().numbers
        self.desk = 1

        #TODO: replace product-order.json whit json object POST from flask
         # Adding Desk object to Order
        self.finished = 0

        Desk.__init__(self)
        self.desk_numbers = self.number 
        objs = [Desk() for i in range(self.number )] # Adding Desk object to Order
        for obj in objs:
            Order.add(obj)


    def verifie_order(self):
        if self.desk > self.desk_numbers:
            return False
        #Parse Json Product List
        with open('/json/availiable-products.json' 'r') as r_file:
            products = json.load(r_file)
        
        for in_order_product in self.products:
            #Check if its in Product List.
            for product in products:
                pass

def process_products():
    with open('/json/product-order.json', 'r') as file: # TODO: #provision json r -> to flask.POST from user and check valid
        #Parse Json Product List
        products = json.load(file)
    products_list = ()
    for j, product in enumerate(products["products"]):
        products_list+= ((product["name"],product["quantity"]),)
        print(products_list)
    return products_list


if __name__ == '__main__':

    add_order = Product()
    for data in process_products():
        add_order.add_product( data[0],  data[1])

    print(add_order.products)