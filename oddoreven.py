def even_or_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False


name = input("What's your name?\n")
print("Hello, {}.".format(name))
print("Please input some numbers one at a time!\nI will tell you whether the number is even or odd.")
for i in range(10):
    number = input()
    is_float = isinstance(number, float)
    num = int(number)
    ans = even_or_odd(num)
    if ans:
        print(num, "is an even number!")
    else:
        print(num, "is an odd number!")

print("All done!")
