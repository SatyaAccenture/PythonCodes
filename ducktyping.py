class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyCharm:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

l1=Laptop()
m1=MyCharm()
p1=PyCharm()

l1.code(m1)
print("------------------------")
l1.code(p1)