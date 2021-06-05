def odd_or_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


name = input("What's your name?\n")
print("Hello, {}.".format(name))
times_played = int(input("How many times do you want to play? "))
i = 0
print("Please input some numbers one at a time!\nI will tell you whether the number is even or odd.")
while i < times_played:
    try:
        number = int(input())
        ans = odd_or_even(number)
        i+= 1
        if ans:
            print(number, "is an even number!")
        else:
            print(number, "is an odd number!")
    except Exception:
        print("That is not a valid input. Please try again!")

print("All done!")
