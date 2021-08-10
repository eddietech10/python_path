import time

print('-' * 70)
intro = """
Welcole to palindrome detector

Check if your word is the same backwards and forwards! 🔁
"""

print(intro)
print('-' * 70)
time.sleep(2)

def run():
    usr = input('\nWrite any word: ').replace(',', ' ').replace('.', ' ')
    palindrome = usr.lower().replace(' ', '').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u').replace(';', '').replace(':', '')

    if palindrome == palindrome[::-1]:
        time.sleep(1.5)
        print(f'\n{usr} ==> is a palindrome\n')
    else:
        time.sleep(1.5)
        print(f'\n{usr} ==> is not a palindrome\n')

    print('-' * 70)


new_try ="""
Do you want to try again?

press (y) for ==> Yes
press (n) for ==> No

"""

def second_chance(new_try):
    while True:
        time.sleep(1)
        usr_2 = input(f'{new_try}(?): ').lower().replace(' ', '').replace(',', ' ').replace('.', ' ').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u').replace(';', '').replace(':', '')

        if usr_2 == 'y' or usr_2 == 'yes':
            time.sleep(1)
            print("\nGreat! Let's do it!\n")
            print('-' * 70)
            run()
        elif usr_2 == 'n' or usr_2 == 'no':
            time.sleep(1)
            print('\nThanks for using this program! 💽')
            print('-' * 70)
            break
        else:
            time.sleep(1)
            print('-' * 70)
            print('\nHouston we have a problem! 🧑🏼‍🚀🚀\n')
            print('-' * 70)
        second_chance(new_try)
        break


if __name__ == '__main__':
    run()
    second_chance(new_try)
