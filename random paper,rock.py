import random

user_wins=0
coumper_wins=0
result_equal=0
options=['rock','paper','scissors']

while True:
    user_input=input('Enter scissors, rock, paper or Q to quit :').lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    coumper_pick=options[random_number]
    print(f'the coumper pick {coumper_pick}.')
    
    if user_input=='rock' and coumper_pick=='scissors':
        print('you wins.')
        user_wins+=1
    elif user_input=='paper' and coumper_pick=='rock':
        print('you wins.')
        user_wins+=1
    elif user_input=='scissors' and coumper_pick=='paper':
        print('you wins.')
        user_wins+=1
    elif user_input=='scissors' and coumper_pick=='scissors':
        print('The result is equal. no winner.')
        result_equal+=1
    elif user_input=='rock' and coumper_pick=='rock':
        print('The result is equal. no winner.')
        result_equal+=1
    elif user_input=='paper' and coumper_pick=='paper':
        print('The result is equal. no winner.')
        result_equal+=1
    else:
        print('you lost')
        coumper_wins+=1

print(f'you win {user_wins} times.')
print(f'The coumper win {coumper_wins} times.')
print(f'The result is equal {result_equal} times.')
print('Good bye')