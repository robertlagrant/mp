import os
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy

# Make the Flask object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Our only model - should be broken out into models file(s)/blueprints if app were bigger
class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    price = db.Column(db.Numeric())
    product_code = db.Column(db.String(10), unique=True)

    def __init__(self, name, price, product_code):
        self.name = name
        self.price = price
        self.product_code = product_code


# Helper functions convert Map <-> SQLA model
def models_to_map(models):
    return [{ 'id': model.id, 
              'name': model.name, 
              'price': '{:,.2f}'.format(model.price), 
              'product_code': model.product_code} 
           for model in models]


# API methods - should be broken out into API file(s)/blueprints if app were bigger
@app.route('/v1/products')
def get_products():
    products = Product.query.all()

    return jsonify(models_to_map(products))


@app.route('/v1/product/<product_id>')
def get_product(product_id):
    product = Product.query.get(int(product_id)) or abort(404)

    return jsonify(models_to_map([product])[0])


@app.route('/v1/product', methods=['POST'])
def create_product():
    name = request.form['name']
    price = request.form['price']
    
    # Optional
    product_code = request.form['product_code'] if 'product_code' in request.form else None 

    db.session.add(Product(name=name, price=price, product_code=product_code))
    db.session.commit()

    return ('', 200)


@app.route('/v1/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id) or abort(404)

    if 'name' in request.form:
        product.name = request.form['name']
    if 'price' in request.form:
        product.price = request.form['price']

    db.session.add(product)
    db.session.commit()

    return ('', 200)


@app.route('/v1/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(int(product_id)) or abort(404)
    db.session.delete(product)
    db.session.commit()

    return ('', 200)


# Go go go
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
