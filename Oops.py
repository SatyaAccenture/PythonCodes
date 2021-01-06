class Computer:
    def __init__(self,cpu,ram):
        self.ram=ram
        self.cpu=cpu
        print("in init")


    def config(self):
        print("config is"+self.cpu, self.ram)


comp1=Computer('i7',16)

print(type(comp1))
Computer.config(comp1)
comp1.config()