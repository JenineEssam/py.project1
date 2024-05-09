print('Welcome to my math quiz!')

playing = input('Do you want to play? ')
score = 0

if playing == 'yes':
    print('Okay! Lets Play :3')

else:
    print('OKAY!! THATS NOT COOL BRO')
    quit()


answer = input('What is 1 x 3 equal to?  ')
if answer == '3':
    print('Correct! good job.')
    score += 1
else:
    print('Incorrect! Try again D:')


answer = input('What is 3 x 3 equal to?  ')
if answer == '9':
    print('Correct! good job.')
    score += 1
else:
    print('Incorrect! Try again D:')

answer = input('What is 3 x 4 equal to?  ')
if answer == '12':
    print('Correct! good job.')
    score += 1
else:
    print('Incorrect! Try again D:')

answer = input('What is 5 x 4 equal to?  ')
if answer == '20':
    print('Correct! good job.')
    score += 1
else:
    print('Incorrect! Try again D:')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score/4) * 100) + '%.')


