class M3:
    def __init__(self):
        self.a = 100
        self._b = 300
        self.__c = 500
    def method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
obj = M3()
obj.method()
print(obj.a)
print(obj._b)
print(obj.__c)