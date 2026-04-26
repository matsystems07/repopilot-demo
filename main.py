```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_cors import CORS

# Create the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoes_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

# Initialize the database, marshmallow, bcrypt, and JWTManager
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.role = role

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, product_id, status):
        self.user_id = user_id
        self.product_id = product_id
        self.status = status

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for the User model
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Define the schema for the Product model
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

# Define the schema for the Order model
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True

# Define the user authentication route
@app.route('/login', methods=['POST'])
def login():
    """
    User authentication route.

    :return: JSON response with access token or error message
    """
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify(error='Invalid username or password'), 401

# Define the user registration route
@app.route('/register', methods=['POST'])
def register():
    """
    User registration route.

    :return: JSON response with success message or error message
    """
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(error='Username already exists'), 400
    new_user = User(username, password, role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='User created successfully')

# Define the product catalog route
@app.route('/products', methods=['GET'])
def get_products():
    """
    Product catalog route.

    :return: JSON response with list of products
    """
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products))

# Define the product filtering route
@app.route('/products/filter', methods=['GET'])
def filter_products():
    """
    Product filtering route.

    :return: JSON response with filtered list of products
    """
    name = request.args.get('name')
    price = request.args.get('price')
    products = Product.query
    if name:
        products = products.filter(Product.name.like(f'%{name}%'))
    if price:
        products = products.filter(Product.price <= float(price))
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products.all()))

# Define the shopping cart route
@app.route('/cart',