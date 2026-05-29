for i in range(1,9):
    if i%2==1:
        for j in range(1,9):
            if j%2==1:
                print("\u2B1c",end="")
            else:
                print("\u2B1B",end="")
        print()
    else:
        for j in range(1,9):
            if j%2==1:
                print("\u2B1B",end="")
            else:
                print("\u2B1c",end="")
        print()