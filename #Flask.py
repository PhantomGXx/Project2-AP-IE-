#Flask

import csv
from flask import Flask, render_template, request,redirect,url_for,flash,session, jsonify
app = Flask(__name__)
app.secret_key = "Ph4nt0m"

import requests

url = "https://api.apilayer.com/fixer/convert?to=USD&from=IRR&amount=1"

headers = {
    "apikey": "y1nAFLy9Mt7kO9xglrjDuHKIz4GG7BbW"
}

response = requests.get(url, headers=headers)
status_code = response.status_code
result = response.json()

print(result) 



def update_csv_file():
    with open('storage.csv', mode='w', newline='') as csvfile:
        fieldnames = ['image', 'name', 'description', 'price_IRR', 'category', 'price_USD']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        items_list = clothing_list + electronics_list + kitchenware_list + miscellaneous_list

        for item in items_list:
            writer.writerow({
                'image': item['image'],
                'name': item['name'],
                'description': item['description'],
                'price_IRR': item['price_IRR'],
                'price_USD': item['price_USD'],
                'category': item['category']
            })

class Item:
    def __init__(self, name, image, description, price_IRR):
        self.name = name
        self.image = image
        self.description = description
        self.price_IRR = price_IRR

items_list = []

with open('storage.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['price_IRR'] = int(row['price_IRR'])
        row['price_USD'] = row['price_IRR'] * result['result'] / 10
        items_list.append(row)

clothing_list = [item for item in items_list if item['category'].strip().lower() == 'clothing']
electronics_list = [item for item in items_list if item['category'].strip().lower() == 'electronics']
kitchenware_list = [item for item in items_list if item['category'].strip().lower() == 'kitchenware']
miscellaneous_list = [item for item in items_list if item['category'].strip().lower() == 'miscellaneous']

cart_list = []

with open('cart.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cart_list.append(row)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if 'cart' not in session:
        session['cart'] = []
    if request.method == 'POST' and 'add_to_cart' in request.form:
        item_id = int(request.form['item_id'])
        list_name = request.form['list_name']
        if list_name == 'clothing':
            item_list = clothing_list
        elif list_name == 'electronics':
            item_list = electronics_list
        elif list_name == 'kitchenware':
            item_list = kitchenware_list
        elif list_name == 'miscellaneous':
            item_list = miscellaneous_list

        item = item_list[item_id]
        session['cart'].append(item)
        cart_list.append(item)
        flash('Success! Item added to cart.')
        update_csv_file()
        return redirect(url_for('main_page'))
    return render_template('MainPage.html', clothing_list=clothing_list, electronics_list=electronics_list, kitchenware_list=kitchenware_list, miscellaneous_list=miscellaneous_list)

@app.route('/sell', methods=['GET', 'POST'])
def AddItems():
    if request.method == 'POST':
        item_name = request.form['item-name']
        item_description = request.form['item-description']
        item_price = int(request.form['item-price'])
        item_image = request.form['item-image']
        item_category = request.form['item-category']
        new_item = {
            'image': item_image,
            'name': item_name,
            'description': item_description,
            'price_IRR': item_price,
            'price_USD': item_price * result['result'] / 10,
            'category': item_category
        }
        if item_category == 'clothing':
            clothing_list.append(new_item)
        elif item_category == 'electronics':
            electronics_list.append(new_item)
        elif item_category == 'kitchenware':
            kitchenware_list.append(new_item)
        else:
            miscellaneous_list.append(new_item)
        flash('Success! Your item has been added.')
        update_csv_file()
        return redirect(url_for('main_page'))
    return render_template('AddItemPage.html')

@app.route('/sell')
def sell_page():
    return render_template('AddItemPage.html')

@app.route('/error')
def error_page():
    return render_template('ErrorPage.html')

@app.route('/cart')
def cart_page():
    total_price_IRR = sum(item['price_IRR'] for item in cart_list)
    total_price_USD = sum(item['price_USD'] for item in cart_list)
    return render_template('ShoppingCartPage.Html', cart_list=cart_list, total_price_IRR=total_price_IRR, total_price_USD=total_price_USD)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'cart' not in session:
        session['cart'] = []
    if request.method == 'POST' and 'remove_from_cart' in request.form:
        item_id = int(request.form['item_id'])
        item = cart_list[item_id]
        session['cart'].remove(item)
        cart_list.remove(item)
        flash('Success! Item removed from cart.')
        update_csv_file()
    return cart_page()


if __name__ == '__main__':
    app.run(debug=True)
