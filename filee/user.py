class User:
    def __init__(self, user_id, name, phone, email, password):
        self._user_id = user_id
        self._name = name
        self._phone = phone
        self._email = email
        self._password = password

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email

    def check_password(self, password):
        return self._password == password
