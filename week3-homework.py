#Ask the user for a number between 1 and 50
#if it is odd, print number is odd
#if it is even print number is even
#use a while loop to keep going until the user inputs a number bigger than 50
error = False

while error == False:
    number = int(input("Input a number between 1 and 50: "))
    if number > 50 or number < 1:
        error = True
        print("Error Try Again!")
    elif number % 2 == 0:
        print("It is Even!")
    elif number % 2 != 0:
        print("It is Odd!")
