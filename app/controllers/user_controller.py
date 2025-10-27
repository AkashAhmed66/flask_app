from ..models.user_model import User
from ..extensions.db import db

class UserController:

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def create_user(data):
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
