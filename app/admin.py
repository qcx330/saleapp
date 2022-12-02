from saleapp.models import Category, Product, Tag
from saleapp import db, app
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms import TextAreaField
from wtforms.widgets import TextArea


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class ProductView(ModelView):
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'price']
    can_view_details = True
    can_export = True
    column_exclude_list = ['image']
    column_labels = {
        'name': 'Tên sản phẩm',
        'description': 'Mô tả',
        'price': 'Gía'
    }
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'description': CKTextAreaField
    }

    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session, name='Danh mục'))
admin.add_view(ModelView(Tag, db.session, name='Tag'))
admin.add_view(ProductView(Product, db.session, name='Sản phẩm'))
admin.add_view(StatsView(name='Thông kê'))