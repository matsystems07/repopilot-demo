```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
import json

# Create a new Flask application
app = Flask(__name__)

# Sample donut data
donuts = [
    {
        "id": 1,
        "name": "Strawberry Sprinkles",
        "description": "A sweet strawberry flavored donut with colorful sprinkles",
        "image": "strawberry_sprinkles.jpg",
        "ingredients": ["Flour", "Sugar", "Strawberry Flavoring", "Sprinkles"],
        "nutritional_info": {
            "calories": 250,
            "fat": 10,
            "carbs": 30,
            "protein": 5
        }
    },
    {
        "id": 2,
        "name": "Chocolate Chip",
        "description": "A rich chocolate flavored donut with dark chocolate chips",
        "image": "chocolate_chip.jpg",
        "ingredients": ["Flour", "Sugar", "Cocoa Powder", "Dark Chocolate Chips"],
        "nutritional_info": {
            "calories": 280,
            "fat": 12,
            "carbs": 35,
            "protein": 6
        }
    },
    {
        "id": 3,
        "name": "Raspberry Filled",
        "description": "A sweet raspberry filled donut with a hint of tartness",
        "image": "raspberry_filled.jpg",
        "ingredients": ["Flour", "Sugar", "Raspberry Jam", "Confectioner's Sugar"],
        "nutritional_info": {
            "calories": 240,
            "fat": 9,
            "carbs": 30,
            "protein": 4
        }
    }
]

# About page data
about_data = {
    "story": "Crusteez Donuts was founded in 2010 with a passion for creating unique and delicious donuts. Our mission is to provide high-quality donuts that bring joy to our customers.",
    "mission": "To be the leading donut shop in the city, known for our creative flavors and exceptional customer service."
}

# Contact page data
contact_data = {
    "store_locations": [
        {"location": "Downtown", "hours": "Mon-Fri: 8am-6pm, Sat-Sun: 9am-7pm"},
        {"location": "Uptown", "hours": "Mon-Fri: 7am-5pm, Sat-Sun: 8am-6pm"}
    ]
}

# Home page route
@app.route("/")
def index():
    """Render the home page with donut catalog"""
    return render_template("index.html", donuts=donuts)

# Donut details page route
@app.route("/donut/<int:donut_id>")
def donut_details(donut_id):
    """Render the donut details page with ingredients and nutritional information"""
    donut = next((d for d in donuts if d["id"] == donut_id), None)
    if donut is None:
        return "Donut not found", 404
    return render_template("donut_details.html", donut=donut)

# About page route
@app.route("/about")
def about():
    """Render the about page with Crusteez story and mission"""
    return render_template("about.html", about_data=about_data)

# Contact page route
@app.route("/contact")
def contact():
    """Render the contact page with store locations and hours"""
    return render_template("contact.html", contact_data=contact_data)

# Filtering and sorting options for donuts
@app.route("/donuts", methods=["GET"])
def get_donuts():
    """Return a list of donuts with filtering and sorting options"""
    filter_name = request.args.get("name")
    sort_by = request.args.get("sort_by")
    donut_list = donuts.copy()
    if filter_name:
        donut_list = [d for d in donut_list if filter_name.lower() in d["name"].lower()]
    if sort_by:
        if sort_by == "name":
            donut_list.sort(key=lambda x: x["name"])
        elif sort_by == "calories":
            donut_list.sort(key=lambda x: x["nutritional_info"]["calories"])
    return jsonify(donut_list)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

```

To run this application, you will need to have Flask installed. You can install it using pip:
```bash
pip install flask
```
You will also need to create the following HTML templates in a templates folder:
- `index.html`: The home page with donut catalog
- `donut_details.html`: The donut details page with ingredients and nutritional