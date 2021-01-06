def topten():
    n=1

    for  n in range(1,11):
        sq=n*n
        yield sq
        n+=1


values=topten()

for i in values:
        print(i)

