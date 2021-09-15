operation = input("""
 +
 -
 *
 /
 Select operation:
""")
number_1 = int(input("Enter first number: "))

number_2 = int(input("Enter second number: "))



if operation == "+":
    print("Your result: ", number_1 + number_2)
elif operation == "-":
    print("Your result: ", number_1 - number_2)
elif operation == "*":
    print("Your result: ", number_1 * number_2)
elif operation == "/":
    print("Your result: ", number_1 / number_2)
else:
    print("Error")