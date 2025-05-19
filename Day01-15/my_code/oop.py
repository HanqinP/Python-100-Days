# oriental object programming

class my_class(object):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


if __name__ == '__main__':
    test = my_class(18)
    print(test.value)
    test.value = 1
    print(test.value)

    #python 可以动态绑定属性和方法给对象，这里面people是动态加的
    test.people = 'test'
    print(test.people)
    #print(test.__value) exception:AttributeError: 'my_class' object has no attribute '__value'
