import random
def random_function():
  number = random.randint(0,100)
  return number

  
def check_guess(guess,number,answer="Correct"):
  if guess > number:
    answer = "lower"
  elif guess < number:
    answer = "higher"
  return answer

def play_game(guess,number):
  answer = "0git"
  while answer != "Correct":
    guess = int(input(check_guess(guess,number)))
    answer = check_guess(guess,number)


  
    
  
  
  