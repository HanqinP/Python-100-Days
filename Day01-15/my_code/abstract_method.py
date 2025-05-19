from abc import ABC,abstractmethod

class pets(ABC):
    @abstractmethod
    def make_voice(self):
        pass

class dog(pets):
    def run(self):
        print('It is running...')

    def make_voice(self):
        print('wang wang..')


if __name__ == '__main__':
    dog1 = dog()
    dog1.run()
    pass
