num_1 = int(input("ENTER FIRST NUMBER:"))
num_2 = int(input("ENTER SECOND NUMBER:"))
print()
print("--------------OPERATIONS--------------")
print("\n  1) ADD\n  2) SUBTRACT\n  3) MULTIPLY\n  4) DIVIDE")

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

choice = int(input("ENTER YOU CHOICE: "))

if choice == 1:
    print()
    print("RESULT",add(num_1,num_2))

elif choice == 2:
    print()
    print("RESULT: ",subtract(num_1,num_2))

elif choice == 3:
    print()
    print("RESULT: ",multiply(num_1,num_2))

elif choice == 4:
    print()
    print("RESULT: ",divide(num_1,num_2))

else:
    print("INVALID CHOICE")
