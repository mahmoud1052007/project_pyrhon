import random
print('🎊  Welcome to The Number Guessing Game 🎊')

secret_number =random.randint(1,10)
attempt =0

while True:
    guess =input('Enter a number between 1 and 10 : ')
    guess =int(guess)
    attempt+=1
    
    if guess==secret_number:
        print('🥳  corret you guessed the number in',attempt,'tries')
        break
        
    elif guess>secret_number:
        print('⬆too high !? try agin')
        
    else:
        print('⬇too low !! try agin')