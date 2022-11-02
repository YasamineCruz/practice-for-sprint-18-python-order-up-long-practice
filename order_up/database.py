from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table, Order

with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)

    order1 = Order(employee_id=1, table_id=1, finished=False)
    order2 = Order(employee_id=1, table_id=2, finished=False)
    order3 = Order(employee_id=1, table_id=3, finished=False)
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)

    beverages = MenuItemType(name="Beverages")
    db.session.add(beverages)

    entrees = MenuItemType(name="Entrees")
    db.session.add(entrees)

    sides = MenuItemType(name="Sides")
    db.session.add(sides)

    dinner = Menu(name="Dinner")
    db.session.add(dinner)

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    db.session.add(fries)

    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    db.session.add(drp)

    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    db.session.add(jambalaya)

    table1 = Table(number=1, capacity=12)
    table2 = Table(number=2, capacity=2)
    table3 = Table(number=3, capacity=10)
    table4 = Table(number=4, capacity=8)
    table5 = Table(number=5, capacity=7)
    table6 = Table(number=6, capacity=6)
    table7 = Table(number=7, capacity=5)
    table8 = Table(number=8, capacity=5)
    table9 = Table(number=9, capacity=4)
    table10 = Table(number=10, capacity=4)

    db.session.add(table1)
    db.session.add(table2)
    db.session.add(table3)
    db.session.add(table4)
    db.session.add(table5)
    db.session.add(table6)
    db.session.add(table7)
    db.session.add(table8)
    db.session.add(table9)
    db.session.add(table10)

    db.session.commit()
 