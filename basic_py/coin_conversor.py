options = """

Choose your coin:

Press 1️⃣  for ==> 💵 Dollars
Press 2️⃣  for ==> 💶 Euros
Press 3️⃣  for ==> 💷 Pounds

"""

eur_dls = 1.18
eur_pds = 1.17
dls_pds = 0.72

eu = '€ EU'
usd = '$ USD'
lbs = '£ LBS'

def run():

    print('-' * 70,'\n',options)
    usr_first_choice = int(input('Select your first currency: '))
    usr_second_choice = int(input('Select your second currency '))
    usr = int(input('How much money do you want to exchange?: '))
    line = '-' * 70
    intro = 'You have'

    if usr_first_choice == 1 and usr_second_choice == 2:
        print(f'{intro} {round(usr/eur_dls)}{eu} \n{line}')

    elif usr_first_choice == 1 and usr_second_choice == 3:
        print(f'{intro} {round(usr*dls_pds, 2)}{lbs} \n{line}')

    elif usr_first_choice == 2 and usr_second_choice == 1:
        print(f'{intro} {round(usr*eur_dls, 2)}{usd} \n{line}')

    elif usr_first_choice == 2 and usr_second_choice == 3:
        print(f'{intro} {round(usr*eur_pds, 2)}{lbs} \n{line}')

    elif usr_first_choice == 3 and usr_second_choice == 1:
        print(f'{intro} {round(usr/dls_pds, 2)}{usd} \n{line}')

    elif usr_first_choice == 3 and usr_second_choice == 2:
        print(f'{intro} {round(usr*eur_pds, 2)}{eu}\n{line}')
    else:
        print(f'{line}\n ⚠️  Please choose a valid option! ⚠️')
        run()

if __name__ == '__main__':
    run()