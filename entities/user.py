class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    def password_is_valid(self) -> bool:
        return self.password is not None and len(self.password) > 5

class UserFactory:
    @staticmethod
    def create(name: str, password: str) -> User:
        return User(name, password)
