from PersistenceLayer.DTO import*


class Employees:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, emp):
        self.conn.execute("""
        INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
        """,[emp.id, emp.name, emp.salary, emp.coff_stand])

    def get_all(self):
        cur = self.conn.cursor()
        all_employees = cur.execute("""
        SELECT* FROM Products order by id
        """).fetchall()
        return [Employee(*row) for row in all_employees]

    def get_emp_report(self):
        cur = self.conn.cursor()
        reports = cur.execute("""
            SELECT emp.name, emp.salary, stnd.location, ifnull(sum((-1) * P.price * act.quantity), 0) as sum
            From Employees as emp left outer join Coffee_stands as stnd on emp.coffee_stand = stnd.id
            left outer join Activities as act on act.activator_id = emp.id and act.quantity < 0
            left outer join Products as P on act.product_id = P.id group by emp.id
        """).fetchall()
        return [Employee_report(*r) for r in reports]


class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, sup):
        self.conn.execute("""
        INSERT INTO Suppliers (id, name, contact_information) VALUES(?, ?, ?) 
        """, [sup.id, sup.name, sup.cont_info])

    def get_all(self):
        cur = self.conn.cursor()
        all_suppliers = cur.execute("""
        SELECT* FROM Suppliers order by id
        """)
        return [Supplayer(*row) for row in all_suppliers]


class Products:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, prod):
        self.conn.execute("""
         INSERT INTO Products (id, description, price, quantity) VALUES(?, ?, ?, ?) 
         """, [prod.id, prod.description, prod.price, prod.quantity])

    def update_quantity(self, product_id, amount):
        self.conn.execute("""
        update Products set quantity = quantity  + (?) where quantity + (?) >= 0 and id = (?)
        """, [amount, amount, product_id])

    def get_quantity(self, product_id):
        cur = self.conn.cursor()
        cur.execute("""
        SELECT quantity FROM Products WHERE id = (?)
        """, [product_id])
        return cur.fetchone()[0]

    def get_all(self):
        cur = self.conn.cursor()
        all_products = cur.execute("""
        SELECT* FROM Products order by id
        """).fetchall()
        return [Product(*row) for row in all_products]


class Coffee_stands:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, cfs):
        self.conn.execute("""
        INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES(?, ?, ?) 
        """,[cfs.id, cfs.location, cfs.number_of_employees])
    def get_all(self):
        cur = self.conn.cursor()
        all_tables = cur.execute("""
        SELECT* FROM Coffee_stands order by id
        """).fetchall()
        return[Coffee_stand(*row) for row in all_tables]


class Activities:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, act):
        self.conn.execute("""
        INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [act.product_id, act.quantity, act.activator_id, act.date])

    def get_all(self):
        cur = self.conn.cursor()
        all_activities = cur.execute("""
        SELECT* FROM Activities order by date
        """).fetchall()
        return[Activity(*row) for row in all_activities]

    def get_activities_report(self):
        cur = self.conn.cursor()
        reports = cur.execute("""
            SELECT act.date, P.description, act.quantity, ifnull(sup.name, 'none'), ifnull(emp.name, 'none')
            FROM Activities as act
            left outer join Products as P on act.product_id = P.id
            left outer join Suppliers as sup on sup.id = act.activator_id
            left outer join Employees as emp on emp.id = act.activator_id
            order by act.date
          """).fetchall()
        return [Activities_report(*report) for report in reports]

