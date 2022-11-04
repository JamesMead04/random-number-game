import random
def random_function():
  guesses = 0
  number = random.randint(0,100)
  guess = -1
  message = "guess a number 1 to 100"
  while guess != number:
    guesses += 1
    guess = int(input(message))
    if guess > number:
      message = "Lower"
    elif guess < number:
      message = "Higher"
    else:
      message = "well done you got it in ",guesses," guesses"
  return message

print(random_function())

  



  
    
  
  
  