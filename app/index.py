from flask import render_template
from app import utils, app


@app.route("/")
def index():
    categories = utils.load_categories()
    products = utils.load_products()
    return render_template('index.html',
                           categories=categories,
                           products = products)


if __name__ == '__main__':
    app.run(debug=True)