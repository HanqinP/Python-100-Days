from abc import ABCMeta, abstractmethod

class fighter(object, metaclass=ABCMeta):

    def __init__(self, hp, name):
        self._hp = hp
        self._name = name

    @staticmethod
    def attack(self, other):
        pass
