class encapsulation:
    a=5
    def __init__(self):
        self._salary=40000
        self.__rf=15000
    def salary(self):
        print(self.__rf)
        return self._salary
obj=encapsulation()
print(obj.a)
print(obj.salary())
print(obj._salary)