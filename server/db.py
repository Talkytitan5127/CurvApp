from flask import current_app

from .models import Employee, TimeTable
from .s_uuid import get_uuid


class Cursor:
    def __init__(self):
        self.app_session = current_app.config['session']
        self.session = self.app_session()

    def close(self):
        self.app_session.remove()

    def commit(self, arr):
        self.session.add_all(arr)
        self.session.commit()

    def create_user(self, data):
        middle_name = data.get('middle_name', None)
        u_id = get_uuid()
        user = Employee(
            first_name=data['first_name'],
            last_name=data['last_name'],
            middle_name=middle_name,
            uuid=u_id
        )

        self.commit([user])

        return user

    def get_user(self, u_id):
        user = self.session.query(Employee).filter_by(uuid=u_id).first()
        return user
