import time

intro = """
Welcome to times tables program! 🧑🏻‍🏫

Choose one option:

👉🏼 1️⃣  ==> to show all tables
👉🏼 2️⃣  ==> to show one tables
👉🏼 3️⃣  ==> to multiplied two numbers
"""

separator = '-' * 70

def run():
    """Receive user input and check which option he/she wants.

The 'if statement' is also used to evaluate the user's input option.
Returns all tables, one tables or multiplication between two numbers.
"""

    usr = input(f'{separator}\n{intro}\nWhat is your choice?: ')
    print(f'\n{separator}\n')
    time.sleep(0.5)

    while True:
        """Ensures that the user does not exit the program until a valid option is entered."""

        if usr == '1':
            counter = 0
            for n in range(11):
                for i in range(10):
                    counter += 1
                    tables = n*counter
                    print(f'\n{n} times {counter} = {tables}')
                time.sleep(0.3)
                counter = 0
                print(f'\n{separator}')
            break

        elif usr == '2':
            table = int(input('What table do you want?: '))
            print('\n')
            counter = 0
            for counter in range(11):
                answer = table * counter
                time.sleep(0.3)
                print(f'{table} times {counter} = {answer}\n') # \n
                counter += 1
            break

        elif usr == '3':
            multiplicand = int(input('Choose a number: '))
            time.sleep(0.5)
            multiplier = int(input('Choose other number: '))
            product = multiplicand * multiplier
            time.sleep(0.5)
            print(f'\n==> {multiplicand} times {multiplier} = {product}\n')
            break

        # This elif cath the error and begin the while sentence
        elif usr != '1' or usr != '2' or usr != '3':
            time.sleep(0.5)
            print(f'{separator}\nPlease choose a valid option\n{separator}')
            run()

        else:
            time.sleep(0.5)
            print('\nHouston we have a problem! 🧑🏼‍🚀🚀\n')
        break

if __name__ == '__main__':
    run()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

new_try ="""
Do you want to try again?

press (y) for ==> Yes
press (n) for ==> No
"""

while True:
    """Check if user want to try again.
    """
    time.sleep(0.5)
    usr2 = input(f'{separator}\n{separator}\n{new_try}\n(❓): ').lower().replace(' ', '')

    if usr2 == 'y' or usr2 == 'ye' or usr2 == 'yes':
        time.sleep(0.3)
        print("\n> Great! Let's do it!\n")
        print(separator)
        run()

    elif usr2 == 'n' or usr2 == 'no':
        time.sleep(0.3)
        print('\nThanks for using this program! 💽')
        break

    # This elif cath the error and begin the while sentence
    elif usr2 != 'y' or usr2 != 'yes' or usr2 != 'n' or usr2 != 'no':
        time.sleep(0.3)
        print(f'{separator}\nPlease choose a valid option\n{separator}')

    else:
        time.sleep(0.5)
        print('\nHouston we have a problem! 🧑🏼‍🚀🚀\n')
        break

