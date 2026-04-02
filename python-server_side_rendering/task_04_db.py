#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# -------- JSON --------
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# -------- CSV --------
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# -------- SQL --------
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    return products

# -------- ROUTE --------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Choisir la source
    try:
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        elif source == "sql":
            data = read_sql()
        else:
            return render_template("product_display.html", error="Wrong source")
    except Exception:
        return render_template("product_display.html", error="Database error")

    # Filtrer par id
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        data = [p for p in data if p["id"] == product_id]

        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)

# -------- RUN --------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
