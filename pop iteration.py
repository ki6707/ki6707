def pxp(a):
    b=list(a)
    for i in range(len(b)):
        b.pop()
        print(b)
x=[1,2,3,4,5,6,7,8,9,10]
pxp(x)