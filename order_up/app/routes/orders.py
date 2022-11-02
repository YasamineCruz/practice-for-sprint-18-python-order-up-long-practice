from flask import Blueprint,render_template
from flask_login import login_required
from ..forms import TableAssignmentForm, MenuItemAssignmentForm
from ..models import Table, Order, Employee, MenuItem, MenuItemType
from flask_login import current_user

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = TableAssignmentForm()
    # Get the tables and open orders
    tables = Table.query.order_by(Table.number).all()
    open_orders = Order.query.filter(Order.finished == False)
    print(open_orders)
    servers = Employee.query.all()

    # Get the table ids for the open orders
    busy_table_ids = [order.table_id for order in open_orders]

    # Filter the list of tables for only the open tables
    open_tables = [table for table in tables if table.id not in busy_table_ids]

    # Finally, convert those tables to tuples for the select field and set the
    # choices property to it
    form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    form.servers.choices = [(s.id, f"Servers {s.name}") for s in servers]

    all_orders = current_user.orders
    orders = [order for order in all_orders if order.finished == False]

    all_menuItems = MenuItem.query.join(MenuItemType).order_by(
        MenuItemType.name, MenuItem.name)

    menuItems = [(menuItem.name,menuItem.type.name) for menuItem in all_menuItems]


    return render_template("orders.html", form=form, orders=orders, menuItems=menuItems)


@bp.route("/orders/<int:id>/items", methods=["GET", "POST"])
@login_required
def additems():
    form = MenuItemAssignmentForm()
    form.menu_item_ids.choices = [(item.id, '')for item in MenuItem.query.all()]


    return render_template("additems.html", form=form)
