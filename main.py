import random
def random_function():
  name = input("enter name:  ")
  guesses = 0
  number = random.randint(0,100)
  guess = -1
  message = "guess a number 1 to 100:  "
  while guess != number:
    guesses += 1
    guess = int(input(message))
    if guess > number:
      message = "Lower:  "
    elif guess < number:
      message = "Higher:  "
    else:
      message = "well done you got it in ",guesses," guesses"

  file = open('scores.txt',"a")
  score = ("%s, scored %s" % (name, guesses))
  file.write(score)
  file.close()
  return message

print(random_function())

  



  
    
  
  
  