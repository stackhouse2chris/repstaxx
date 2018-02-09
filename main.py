from flask import Flask, render_template, url_for, request, jsonify
from controller import Customer, Vendor
import json

app = Flask(__name__)

@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/orders")
def orders():
    customers = Customer.res
    principals = Vendor.get_principal_vendors()
    return render_template("orders.html", customers=customers, principals=principals)

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/invoices")
def invoices():
    return render_template("invoices.html")

@app.route("/customers")
def customers():
    ids = Customer.get_cust_ids()
    names = Customer.get_cust_names()
    return render_template("customers.html", ids=ids, names=names)

@app.route("/customer/<customerid>")
def customer(customerid):
    customer = Customer.get_cust_info(customerid)
    customer_name = customer[0]
    customer_add1 = customer[1]
    customer_add2 = customer[2]
    customer_city = customer[3]
    customer_state = customer[4]
    customer_zip = customer[5]
    return jsonify(customername=customer_name, customeradd1=customer_add1, customeradd2=customer_add2, customercity=customer_city,
                    customerstate=customer_state, customerzip=customer_zip)


@app.route("/items")
def items():
    return render_template("items.html")

@app.route("/purchases")
def purchases():
    return render_template("purchases.html")

@app.route("/vendors")
def vendors():
    return render_template("vendors.html")

@app.route("/accounting")
def accounting():
    return render_template("accounting.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")


if __name__ == "__main__":
    app.run(debug=True)
