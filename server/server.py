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
