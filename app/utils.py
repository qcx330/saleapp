import json
from app import app
from app.models import Category, Product

def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)

def load_products(cate_id=None,kw=None):
    query=Product.query

    if cate_id:
        query=query.filter(Product.category_id.__eq__(cate_id))


    if kw:
        query=query.filter(Product.name.contains(kw))


    return query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)