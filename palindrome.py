while True:

    a=str(input("enter a string: "))
    if(a==a[::-1]):
        print("the givien word is palindrome")
    else:
        print("the not givien word is palindrome")