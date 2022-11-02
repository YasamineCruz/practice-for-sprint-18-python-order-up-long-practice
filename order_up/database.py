from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType

with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)

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

    db.session.commit()
