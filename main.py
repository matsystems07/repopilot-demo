```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Create a Flask application
app = Flask(__name__)

# Configure the application to use a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///honda_cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy object
db = SQLAlchemy(app)

# Define a Car model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    specifications = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    reviews = db.relationship('Review', backref='car', lazy=True)

# Define a Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a function to add a car to the database
def add_car(model, year, price, specifications, image):
    car = Car(model=model, year=year, price=price, specifications=specifications, image=image)
    db.session.add(car)
    db.session.commit()

# Define a function to add a review to the database
def add_review(car_id, rating, review):
    review = Review(car_id=car_id, rating=rating, review=review)
    db.session.add(review)
    db.session.commit()

# Define a route for the home page
@app.route('/')
def home():
    cars = Car.query.all()
    return render_template('home.html', cars=cars)

# Define a route for the car details page
@app.route('/car/<int:car_id>')
def car_details(car_id):
    car = Car.query.get(car_id)
    reviews = Review.query.filter_by(car_id=car_id).all()
    return render_template('car_details.html', car=car, reviews=reviews)

# Define a route for the add car page
@app.route('/add_car', methods=['GET', 'POST'])
def add_car_page():
    if request.method == 'POST':
        model = request.form['model']
        year = int(request.form['year'])
        price = float(request.form['price'])
        specifications = request.form['specifications']
        image = request.files['image']
        image.save(os.path.join('static/images', secure_filename(image.filename)))
        add_car(model, year, price, specifications, secure_filename(image.filename))
        return redirect(url_for('home'))
    return render_template('add_car.html')

# Define a route for the add review page
@app.route('/add_review/<int:car_id>', methods=['GET', 'POST'])
def add_review_page(car_id):
    if request.method == 'POST':
        rating = int(request.form['rating'])
        review = request.form['review']
        add_review(car_id, rating, review)
        return redirect(url_for('car_details', car_id=car_id))
    return render_template('add_review.html')

# Define a route for filtering cars by year
@app.route('/filter_by_year/<int:year>')
def filter_by_year(year):
    cars = Car.query.filter_by(year=year).all()
    return render_template('home.html', cars=cars)

# Define a route for filtering cars by model
@app.route('/filter_by_model/<string:model>')
def filter_by_model(model):
    cars = Car.query.filter_by(model=model).all()
    return render_template('home.html', cars=cars)

# Define a route for filtering cars by price
@app.route('/filter_by_price/<float:price>')
def filter_by_price(price):
    cars = Car.query.filter_by(price=price).all()
    return render_template('home.html', cars=cars)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**templates/home.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Honda Car Catalog</title>
</head>
<body>
    <h1>Honda Car Catalog</h1>
    <ul>
    {% for car in cars %}
        <li>
            <a href="{{ url_for('car_details', car_id=car.id) }}">{{ car.model }} ({{ car.year }})</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_car_page') }}">Add a car</a></p>
</body>
</html>
```

**templates/car_details.html