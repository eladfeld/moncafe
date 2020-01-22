

class Employee:
    def __init__(self, id, name, salary, coff_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coff_stand = coff_stand

    def __str__(self):
        return str((self.id, self.name, self.salary, self.coff_stand))

class Supplayer:
    def __init__(self, id, name, cont_info):
        self.id = id
        self.name = name
        self.cont_info = cont_info

    def __str__(self):
        return str((self.id, self.name, self.cont_info))


class Product:
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str((self.id, self.description, self.price, self.quantity))


class Coffee_stand:
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

    def __str__(self):
        return str((self.id, self.location, self.number_of_employees))


class Activity:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

    def __str__(self):
        return str((self.product_id, self.quantity, self.activator_id, self.date))


class Employee_report:
    def __init__(self, name, salary, location, sum):
        self.name = name
        self.salary = salary
        self.location = location
        self.sum = sum

    def __str__(self):
        return self.name + " " + str(self.salary) + " " + self.location + " " + str(self.sum)


class Activities_report:
    def __init__(self, date, description, quantity, SupplyerName, EmployeeName ):
        self.date = date
        self.description = description
        self.SupplyerName = SupplyerName
        self.EmployeeName = EmployeeName
        self.quantity = quantity

    def __str__(self):
        return str((self.date, self.description, self.quantity, self.EmployeeName, self.SupplyerName))
