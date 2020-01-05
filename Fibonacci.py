print("Fibonacci Numbers")
n = int(input("Enter Any Number : "))
a, b, c = 0, 1, 0
while c < n:
    print(a)
    d = a + b
    a = b
    b = d
    c += 1
