from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except sqlite3.Error:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')
    
    products_list = []
    error_msg = None

    if source == 'json':
        try:
            products_list = read_json()
        except Exception:
            products_list = []
    elif source == 'csv':
        try:
            products_list = read_csv()
        except Exception:
            products_list = []
    elif source == 'sql':
        try:
            products_list = read_sqlite()
        except Exception:
            products_list = []
    else:
        error_msg = "Wrong source"
        return render_template('product_display.html', error=error_msg)

    if prod_id:
        try:
            prod_id = int(prod_id)
            products_list = [p for p in products_list if p['id'] == prod_id]
            if not products_list:
                error_msg = "Product not found"
        except ValueError:
            error_msg = "Product not found"
            products_list = []

    return render_template('product_display.html', products=products_list, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
