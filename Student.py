class Student:
    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.lap=self.Laptop()

    def avarage(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("Inside static method")

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.cpu ,self.brand ,self.ram)

s1= Student(34,47,32)
s2=Student(76,88,74)
print(s1.avarage())
print(s2.avarage())
print(Student.info())
print(s1.lap.show())



