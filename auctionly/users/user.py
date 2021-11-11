""" User class implemented to provide parent class methods to its children """
from auctionly.models import User as user
from auctionly import db

class User:

    def __init__(self, user_id, name, last_name, email, password):
        self.user_id = user_id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.feed = []

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        # to-do: implement hashing function for password
        pass

    # As a seller I want to be able to view the feed so that I can see the art available.
    def get_user_feed(self):
        return self.feed

    def set_user_feed(self, feed):
        self.feed = feed
