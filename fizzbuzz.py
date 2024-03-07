for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("This would be a FizzBuzz")
    elif i % 3 == 0:
        print("This is Fizz")
    elif i % 5 == 0:
        print("This is Buzz")
    else:
        print(i)