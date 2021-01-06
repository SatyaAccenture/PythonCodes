

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):

        m1=self.m1+ other.m1
        m2=self.m2 + other.m2
        s3 = Student(m1, m2)
        print(s3.m1 ,s3.m2)
        return s3

    def __gt__(self, other):
        s1= self.m1+self.m2
        s2=other.m1+other.m2

        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1 ,self.m2)


s1=Student(56,77)
s2=Student(88,99)
s3=s1+s2

if s1 > s2:
    print("S1 wins")
else:
    print("s2 wins")

a=9
print(s1)