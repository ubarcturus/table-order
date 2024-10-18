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
        self.products = []

    def add_product(self,name, quantity):
        product = []
        product.append(name)
        product.append(quantity)
        self.products.append(product)
        
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


    def verifie_order(self, products_list):
        '''
        if self.desk > self.desk_numbers:
            return False
        '''
        #Parse Json Product List #TODO FAILSAVE IF quantity 0
        with open('json/availiable-products.json', 'r') as r_file:
            products = json.load(r_file)
        availiable_products_list = []

        for product in products["products"]:
            availiable_products_list.append(product["name"])

        for product in products_list:
            if product[0] in availiable_products_list:
                pass
            else:
                print(product, availiable_products_list)
                return False

        return True


def process_products(): #open 
    with open('json/product-order.json', 'r') as file: # TODO: #provision json r -> to flask.POST from user and check valid
        #Parse Json Product List
        products = json.load(file)
    products_list = []
    for j, product in enumerate(products["products"]):
        products_list.append((product["name"],product["quantity"]),)
    return products_list


if __name__ == '__main__':

    add_order = Product()
    order = Order()
    data_list =  process_products()
    if order.verifie_order(data_list):
        for data in data_list:
            add_order.add_product( data[0],  data[1])
        print(add_order.products)
    else:
        print("There was an invalid order! Someone messing whit the HTML source?")

