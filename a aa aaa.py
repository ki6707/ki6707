n = 4


for i in range(1, n + 1):

    for j in range(1, i + 1):

        print(chr(64 + j) * i, end=" ")

    print()
    