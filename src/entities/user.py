from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, name, password, inventory=[], recipes=[], plans=[], is_admin=False):
        self.id = id
        self.name = name
        self.password = password
        self.inventory = inventory
        self.recipes = recipes
        self.plans = plans
        self.is_admin = is_admin

    def __repr__(self):
        return '<User {}>'.format(self.name)
