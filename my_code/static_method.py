# 有些方法属于类，但不属于对象，比如三角形类中，计算周长可以属于对象类，但是判断是否是三角形不是，因为那时候都没生成三角形，即没有对象，就不会有对象方法
#此时，判断能否成为三角形的方法就可以是类方法，用静态方法即可实现

class triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self):
        return self._a + self._b + self._c

    @staticmethod
    def is_triangle(self):
        if self._a + self._b > self._c:
            return True
        elif self._a + self._c > self._b:
            return True
        elif self._b + self._c > self._a:
            return True
        else:
            return False


