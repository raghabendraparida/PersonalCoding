
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_vote(self):
        return self.age >= 18
