import atexit
import sqlite3
import os


from PersistenceLayer.DAO import*
from PersistenceLayer.DTO import*


class Repository(object):

    def __init__(self):
        with sqlite3.connect('moncafe.db') as c:
            self.conn = c
        self.Employees = Employees(self.conn)
        self.Suppliers = Suppliers(self.conn)
        self.Products = Products(self.conn)
        self.Coffee_stands = Coffee_stands(self.conn)
        self.Activities = Activities(self.conn)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def init_tables(self):
        self.conn.executescript("""
        CREATE TABLE Employees(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary REAL NOT NULL,
            coffee_stand INTEGER REFERENCES Coffee_stands(id)
            );
        CREATE TABLE Suppliers(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_information TEXT
        );
        CREATE TABLE Products(
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        );
        CREATE TABLE Coffee_stands(
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            number_of_employees INTEGER
        );
        CREATE TABLE Activities(
            product_id INTEGER INTEGER REFERENCES Products(id),
            quantity INTEGER NOT NULL,
            activator_id INTEGER NOT NULL,
            date DATE NOT NULL 
        );""")

    def config_employee(self, t):
        emp = Employee(t[1], t[2], t[3], t[4])
        self.Employees.insert(emp)

    def config_supplier(self, t):
        sup = Supplayer(t[1], t[2], t[3])
        self.Suppliers.insert(sup)

    def config_product(self, t):
        prod = Product(t[1], t[2], t[3], 0)
        self.Products.insert(prod)

    def config_coffee_stand(self, t):
        cft = Coffee_stand(t[1], t[2], t[3])
        self.Coffee_stands.insert(cft)

    def insert_to_database(self, t):
        config_map = {
            "E": self.config_employee,
            "S": self.config_supplier,
            "P": self.config_product,
            "C": self.config_coffee_stand
        }
        typeof = t[0]
        func = config_map.get(typeof)
        func(t)

    def apply_action(self, t):
        if self.Products.get_quantity(t[0]) + int(t[1]) >= 0:
            self.Products.update_quantity(t[0], t[1])
            act = Activity(t[0], t[1], t[2], t[3])
            self.Activities.insert(act)


repo = Repository()
atexit.register(repo.close)