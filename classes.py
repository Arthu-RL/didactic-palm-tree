class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def tofilm(self):
        if self.filming:
            return f'{self.name} its already filming.'

        self.filming = True
        return f'{self.name} its filming.'

    def stopfilm(self):
        if not self.filming:
            return

        self.filming = False
        return f'{self.name} has stoped filming.'

    def photograph(self):
        if self.filming:
            return f'{self.name} cant take photos while filming.'
        else:
            return f'{self.name} is taking photos.'


import json


class SaveFile:
    def __init__(self, *args):
        self.args = args

    def savefile(self):
        person = [self.args]
        with open('person.json', 'w', encoding='utf-8') as file:
            json.dump(*person, file, ensure_ascii=False, indent=2)

    def readfile(self):
        with open('person.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(*data)


class LearningMethods:
    ano = 2023

    def __init__(self, word):
        self.word = word

    @classmethod
    def classmethod(cls, word):
        return cls(word)


class Connections:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def sum(x, y):
        return x + y


class Pen:
    def __init__(self, color):
        self.color = color

    # Protecting the name "color" in a function
    def get_color(self):
        return self.color

# In python, we have a way to protect the name "color" this.
# The Pythonic way to protect the name "color".
class Pencil:
    def __init__(self, color):
        self.__color = color

    # GETTER
    @property
    def color(self):
        return self.__color

    # SETTER
    @color.setter
    def color(self, value):
        self.__color = value
