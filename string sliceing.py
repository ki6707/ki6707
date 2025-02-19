while True:

    a=str(input("enter a string: "))

    for i in range(len(a)):
        print(a[:i+1])