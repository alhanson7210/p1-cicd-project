from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self):
        self.curr_user = None
        self.password_hash = None

    def set_user(self, user: str):
        self.curr_user = user

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)

class UserManager:
    user_table: str = "users"

    def __init__(self):
        self.user = User()
