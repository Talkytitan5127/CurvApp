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
            uuid=u_id,
            rank=data.get('rank', None),
            department=data.get('department', None),
        )

        return user

    def get_user(self, u_id, db_id=None):
        if db_id is not None:
            user = self.session.query(Employee).get(db_id)
        else:
            user = self.session.query(Employee).filter_by(uuid=u_id).first()
        return user

    def get_all_users(self):
        users = self.session.query(Employee).all()
        return users

    def get_user_time(self, user):
        timelist = self.session.query(TimeTable).filter_by(employee_id=user.id).all()
        return timelist

    def create_time(self, user, is_exit, time_str=None):
        record = TimeTable(
            is_exit=is_exit,
            employee_id=user.id,
            person_time=time_str,
        )

        return record
