```python
# Import required libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define a class for Suzuki car models
class SuzukiCar:
    def __init__(self, name, price, engine, transmission, fuel_type):
        self.name = name
        self.price = price
        self.engine = engine
        self.transmission = transmission
        self.fuel_type = fuel_type

# Define a class for the Suzuki car catalog
class SuzukiCarCatalog:
    def __init__(self):
        self.cars = [
            SuzukiCar("Suzuki Alto", 1500000, "660cc", "Manual", "Petrol"),
            SuzukiCar("Suzuki WagonR", 1800000, "1000cc", "Manual", "Petrol"),
            SuzukiCar("Suzuki Cultus", 2000000, "1000cc", "Manual", "Petrol"),
            SuzukiCar("Suzuki Swift", 2500000, "1300cc", "Manual", "Petrol"),
            SuzukiCar("Suzuki Baleno", 2800000, "1300cc", "Manual", "Petrol"),
        ]

    def get_cars(self):
        return self.cars

    def search_cars(self, name):
        return [car for car in self.cars if name.lower() in car.name.lower()]

    def filter_cars(self, price):
        return [car for car in self.cars if car.price <= price]

# Define the main application class
class SuzukiCarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suzuki Cars Pakistan")
        self.catalog = SuzukiCarCatalog()

        # Create tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.home_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.home_tab, text="Home")

        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Search")

        self.filter_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.filter_tab, text="Filter")

        self.dealership_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.dealership_tab, text="Dealership")

        # Home tab
        self.home_label = ttk.Label(self.home_tab, text="Welcome to Suzuki Cars Pakistan!")
        self.home_label.pack(pady=10)

        self.cars_button = ttk.Button(self.home_tab, text="View All Cars", command=self.view_cars)
        self.cars_button.pack(pady=10)

        # Search tab
        self.search_label = ttk.Label(self.search_tab, text="Search for a car:")
        self.search_label.pack(pady=10)

        self.search_entry = ttk.Entry(self.search_tab, width=30)
        self.search_entry.pack(pady=10)

        self.search_button = ttk.Button(self.search_tab, text="Search", command=self.search_car)
        self.search_button.pack(pady=10)

        # Filter tab
        self.filter_label = ttk.Label(self.filter_tab, text="Filter cars by price:")
        self.filter_label.pack(pady=10)

        self.filter_entry = ttk.Entry(self.filter_tab, width=30)
        self.filter_entry.pack(pady=10)

        self.filter_button = ttk.Button(self.filter_tab, text="Filter", command=self.filter_cars)
        self.filter_button.pack(pady=10)

        # Dealership tab
        self.dealership_label = ttk.Label(self.dealership_tab, text="Dealership Information:")
        self.dealership_label.pack(pady=10)

        self.dealership_text = tk.Text(self.dealership_tab, height=10, width=40)
        self.dealership_text.pack(pady=10)
        self.dealership_text.insert(tk.END, "Contact us at 123-456-7890 or visit our website at suzuki.com.pk")

    def view_cars(self):
        # Create a new window to display all cars
        cars_window = tk.Toplevel(self.root)
        cars_window.title("All Cars")

        # Create a text box to display car information
        cars_text = tk.Text(cars_window, height=20, width=60)
        cars_text.pack(pady=10)

        # Get all cars from the catalog
        cars = self.catalog.get_cars()

        # Display each car's information
        for car in cars:
            cars_text.insert(tk.END, f"Name: {car.name}\n")
            cars_text.insert(tk.END, f"Price: {car.price}\n")
            cars_text.insert(tk.END, f"Engine: {car.engine}\n")
            cars_text.insert(tk.END, f"Transmission: {car.transmission}\n")
            cars