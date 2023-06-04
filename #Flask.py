#Flask

from flask import Flask, render_template, request
app = Flask(__name__)

class Item:
    def __init__(self, name, image, description, price_IRR, price_USD):
        self.name = name
        self.image = image
        self.description = description
        self.price_IRR = price_IRR
        self.price_USD = price_USD

clothing_list = [
        {'name': 'Item 1', 'description': 'This is item 1', 'price_IRR': '420000','price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 2', 'description': 'This is item 2', 'price_IRR': '420000', 'price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 3', 'description': 'This is item 3', 'price_IRR': '420000', 'price_USD': '39.99','category':'electronics'}
    ]

electronics_list = [
        {'name': 'Item 1', 'description': 'This is item 1', 'price_IRR': '420000','price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 2', 'description': 'This is item 2', 'price_IRR': '420000', 'price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 3', 'description': 'This is item 3', 'price_IRR': '420000', 'price_USD': '39.99','category':'electronics'}
    ]

kitchenware_list = [
        {'name': 'Item 1', 'description': 'This is item 1', 'price_IRR': '420000','price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 2', 'description': 'This is item 2', 'price_IRR': '420000', 'price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 3', 'description': 'This is item 3', 'price_IRR': '420000', 'price_USD': '39.99','category':'electronics'}
    ]

miscellaneous_list = [
        {'name': 'Item 1', 'description': 'This is item 1', 'price_IRR': '420000','price_USD': '40.99', 'category':'electronics'},
        {'name': 'Item 2', 'description': 'This is item 2', 'price_IRR': '420000', 'price_USD': '39.99', 'category':'electronics'},
        {'name': 'Item 3', 'description': 'This is item 3', 'price_IRR': '420000', 'price_USD': '39.99','category':'electronics'}
    ]

@app.route('/')
def main_page():
    return render_template('MainPage.html', clothing_list=clothing_list, electronics_list=electronics_list,kitchenware_list=kitchenware_list,miscellaneous_list=miscellaneous_list)

@app.route('/sell', methods=['GET', 'POST'])
def AddItems():
    if request.method == 'POST':
        item_name = request.form['item-name']
        item_description = request.form['item-description']
        item_price = request.form['item-price']
        item_image = request.form['item-image']
        item_category = request.form['item-category']
    return render_template('AddItemPage.html')

@app.route('/sell')
def sell_page():
    return render_template('AddItemPage.html')

if __name__ == '__main__':
    app.run(debug=True)