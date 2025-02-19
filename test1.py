import random;

print("Hi, try to guess my number if you can!")
number_to_guess = random.randrange(100)

chances = 7
guess_counter = 0

while guess_counter < chances:
  guess_counter += 1
  my_guess = int(input('Please Enter your Guess:'))
  
  if my_guess == number_to_guess:
    print(f'The number is {number_to_guess} and you guessed correctly! On attempt No. {guess_counter}')
    break
  elif guess_counter >= chances and my_guess != number_to_guess:
    print(f'Oops sorry, The number is {number_to_guess}. Better luck next time.')
  elif my_guess > number_to_guess:
    print('You guess is higher')
  elif my_guess < number_to_guess:
    print('Your guess is lower')