
number = int(input("Enter a number less than 25\n"))

if number > 25:
    print("Error")
else:
    for i in range(number, 26):
        print(f"Inside the loop, my variable is {i}")
