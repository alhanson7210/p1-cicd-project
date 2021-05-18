from flask import make_response, request, render_template
from app.database_model import DatabaseManager
from user_model import UserManager

def get_cookie():
    user = request.cookies.get('username')

class Session:
    def __init__(self):
        pass

    @staticmethod
    def set_cookie():
        if request.method == 'POST':
            user = request.form['email']
            resp = make_response(render_template('riff_tracker.html'))
            resp.set_cookie('username', user)
            return resp

class SessionManager:
    def __init__(self):
        self.user_manager: UserManager = UserManager()
        self.user_session: Session = Session()
        self.database_manager: DatabaseManager = DatabaseManager()
