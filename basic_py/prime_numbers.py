from math import sqrt

counter = 0
verified_number = int(input('Check if is prime: '))

if verified_number < 2:
    counter += 1

root_verified_number = int(sqrt(verified_number)) + 1

for i in range(2, root_verified_number):

    if verified_number % i == 0:
        counter += 1

    print('\nroot of verified number:',root_verified_number, '\nverified number==>',verified_number, 'divided by', i, '=', {verified_number % i})


if counter == 0:
    print('\n✅ It is prime because it has no residues in (0).')
    print('-' * 70)

else:
    print('\n❌ It is not a prime number because it has (1) or more residues in (0).')
    print('-' * 70)
