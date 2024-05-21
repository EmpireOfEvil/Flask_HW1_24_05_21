from flask import Flask,render_template
from warehouse import Merch, warehouse

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/shop/<path:pagename>/')
def shop_page(pagename):
    return render_template('shoplist.html', stock = warehouse[pagename])

customer_cart = []

@app.route('/cart+<path:cart_item>/')
def add_to_cart_page(cart_item):
    item_name, item_price = cart_item.split('+')[-2],cart_item.split('+')[-1]
    customer_cart.append(Merch(item_name, int(item_price)))
    cart_sum = sum(item.price for item in customer_cart)
    return render_template('cart.html', customer_cart = customer_cart, total_sum = cart_sum)

@app.route('/cart/')
def cart_page():
    cart_sum = sum(item.price for item in customer_cart)
    return render_template('cart.html', customer_cart=customer_cart, total_sum=cart_sum)

if __name__ == '__main__':
    app.run(debug=True)