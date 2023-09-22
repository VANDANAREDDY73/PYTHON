class M3:
    def __init__(self):
        self.__c=500
    def getter(self):
        return self.__c
obj=M3()
print(obj.getter())