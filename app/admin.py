from flask import redirect, url_for, flash
from flask_login import current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


class AdminMixin(AdminIndexView):
    def is_accessible(self):
        return current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        flash('You must be an administrator.', 'warning')
        return redirect(url_for('auth.login'))


class HomeAdminView(AdminMixin):
    pass


class UserAdminView(ModelView):
    form_columns = ['username', 'email', 'confirmed', 'member_since']


class PostAdminView(ModelView):
    form_columns = ['body', 'author', 'timestamp']


class CommentAdminView(ModelView):
    form_columns = ['body', 'author', 'post', 'timestamp']
