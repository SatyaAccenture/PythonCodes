
f1=open('abc','a')
f1.write("\n")
f1.write("Is the best")

f2=open('copy','w')
f= open("mydata",'r')
for data in f:
    f2.write(data)