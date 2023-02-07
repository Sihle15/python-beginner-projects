# Calculator
def add(a, b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)}")


def sub(a, b):
    answer = a - b
    print(f"{str(a)} - {str(b)} = {str(answer)}")


def mul(a, b):
    answer = a * b
    print(f"{str(a)} * {str(b)} = {str(answer)}")


def div(a, b):
    answer = a / b
    print(f"{str(a)} / {str(b)} = {str(answer)}")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit \n")

    choice = input("Please enter arithmetic choice: ")

    if choice.lower() == 'a':
        print('Addition')
        first_number = int(input('Please enter first number: '))
        second_number = int(input('Please enter second number: '))
        add(first_number, second_number)

    elif choice.lower() == 'b':
        print('Subtraction')
        first_number = int(input('Please enter first number: '))
        second_number = int(input('Please enter second number: '))
        sub(first_number, second_number)

    elif choice.lower() == 'c':
        print('Multiplication')
        first_number = int(input('Please enter first number: '))
        second_number = int(input('Please enter second number: '))
        mul(first_number, second_number)

    elif choice.lower() == 'd':
        print('Division')
        first_number = int(input('Please enter first number: '))
        second_number = int(input('Please enter second number: '))
        div(first_number, second_number)

    elif choice.lower() == 'e':
        print("Switching off...")
        quit()

    else:
        print('Please select from the list')