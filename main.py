import random
def random_function():
  number = random.randint(0,100)
  guess = -1
  message = "guess a number 1 to 100"
  while guess != number:
    guess = int(input(message))
    if guess > number:
      message = "Lower"
    elif guess < number:
      message = "Higher"
    else:
      message = "well done you got it"
  print(message)

random_function()

  



  
    
  
  
  