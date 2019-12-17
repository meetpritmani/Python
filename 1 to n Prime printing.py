print("Prime Number")
a = int(input("Enter Any Number: "))
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print("Not Prime")
            break
    else:
        for b in range(a):
            if (b % a) == 0:
                print(b)
else:
    print("Not Prime")
