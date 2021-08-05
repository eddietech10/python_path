print('-' * 70)
intro = """
Welcole to palindrome detector

Check if your word is the same backwards and forwards! 🔁
"""

print(intro)
print('-' * 70)

def run():
    usr = input('\nWrite any word: ')
    palindrome = usr.lower().replace(' ', '')

    if palindrome == palindrome[::-1]:
        print(f'\n{usr} ==> is a palindrome\n')
    else:
        print(f'\n{usr} ==> is not a palindrome\n')

    print('-' * 70)


new_try ="""
Do you want to try again?

press (y) for ==> Yes
press (n) for ==> No

"""

def second_chance(new_try):
    while True:
        usr_2 = input(f'{new_try}(?): ').lower().replace(' ', '')

        if usr_2 == 'y':
            print("Great! Let's do it!\n")
            print('-' * 70)
            run()
        elif usr_2 == 'n':
            print('\nThanks for using this program! 💽')
            print('-' * 70)
            break
        else:
            print('-' * 70)
            print('\nHouston we have a problem! 🧑🏼‍🚀🚀\n')
            print('-' * 70)
        second_chance(new_try)
        break


if __name__ == '__main__':
    run()
    second_chance(new_try)
