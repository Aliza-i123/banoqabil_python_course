# ALIZA ROSHAN
# roshanaliza177@gmail.com
# TASK 2

# MAKING A CALCULATER

print("Calculate on your own choice")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select an operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Select your option(1, 2, 3, 4, 5) :"))
if choice == 1:
    print("Result :", num1 + num2)
elif choice == 2:
    print("Result :", num1 - num2)
elif choice == 3:
    print("Result :", num1 * num2 )
elif choice == 4:
    print("Result :", num1 / num2)
elif choice ==5:
    print("EXIT")
else:
    print("EXIT")
