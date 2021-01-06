class A:
    def __init__(self):
        print("In A Init")
    def feature1(self):
        print("Feature 1-A Working")

    def feature2(self):
        print("Feature 2 Working")



class B:
    def __init__(self):

        print("Inside init B")

    def feature1(self):
        print("Feature 1-B Working")

    def feature4(self):
        print("Feature 4 Working")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("In init C")
    def feat(self):
        super().feature2()

c1=C()
c1.feat()
