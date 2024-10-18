import json
import datetime

from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 

# create an in-memory SQLite database 
engine = create_engine('sqlite:///db.sqlite', echo=True) 
  
Base = declarative_base() 
  

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
class Product():
    def __init__(self):
        self.date = datetime.datetime.now()
        self.availibility = True #TODO check make method!
        self.products = []

    def add_product(self, name, quantity):
        product = []
        product.append(name)
        product.append(quantity)
        self.products.append(product)
        
 # Index on-stage characters using their charid

class Desk():
    numbers = 3

    def __init__(self):
        self.numbers = 0 # TODO: ADD


class Order(Base):
    __tablename__ = 'order'
    number = Column(Integer, primary_key=True) 
    desk_number = Column(String) 
    products_list_json = Column(JSON)
    finished = Column(String) 
  
    def __init__(self, desk_number,products_list_json=products_list_json, finished=False, ): #TODO: add desk and finsihed
        self.number = desk_number
        self.desk = 1
        #TODO: replace product-order.json whit json object POST from flask
         # Adding Desk object to Order
        self.finished = finished
        self.products_list_json = self.process_main()



    def process_main(self):
        data_list = self.process_products()
        if self.verifie_order(data_list):
            product = Product()
            for data in data_list:
                product.add_product(data[0],  data[1])
            return json.dumps(product.products) #SQLalchemy doesnt support ARRAY so JSON instead
                
        else:
            print("There was an invalid order! Someone messing whit source?")
            return
        #TODO: Placeholder



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


    def process_products(self): #open 
        with open('json/product-order.json', 'r') as file: # TODO: #provision json r -> to flask.POST from user and check valid
            #Parse Json Product List
            products = json.load(file)
        products_list = []
        for j, product in enumerate(products["products"]):
            products_list.append((product["name"],product["quantity"]),)
        return products_list
    

if __name__ == '__main__':

    # create the users table 
    Base.metadata.create_all(engine) 
    
    # create a session to manage the connection to the database 
    Session = sessionmaker(bind=engine) 
    session = Session() 
    
    # add a new user to the database 
    order = Order(1)
    order.process_main() # whit desk number TODO: later maybe direct here products also
    session.add(order) 
    session.commit() 
    
