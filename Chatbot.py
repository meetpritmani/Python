print("Answer The Simple Question")
a = input("Hey What's Your Name: ")
print("hi. ")

b = input("How Are You: " + a)

if b == 'fine':
    c = input("How Was or Is Your Day: ")
    if c == 'good':
        print("Nice")
    else:
        print("Please ans my Question")
else:
    print("Please Ans My Question: " + a)
