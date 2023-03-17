import os
from dotenv import load_dotenv

load_dotenv()


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


def create_user() -> User:
    # It would be better to get random users from database
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    return User(email, password)
