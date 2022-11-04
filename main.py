import random
def random_function():
  name = input("enter name:  ")
  guesses = 0
  number = random.randint(0,100)
  guess = -1
  message = "guess a number 1 to 100:  "
  while guess != number:
    guesses += 1
    try:
      guess = int(input(message))
      if guess > number:
        message = "Lower:  "
      elif guess < number:
        message = "Higher:  "
      else:
        message = "well done you got it in ",guesses," guesses"
      
    
    except:
      print("not a valid integer")


  file = open('scores.txt',"a")
  score = ("%s, scored by %s " % (guesses, name))
  file.write(score)
  file.write("\n")
  file.close()
  return message
    


choice = input("P to play the game or S for The low score:   ")
choice= choice.upper()
if choice == 'P':
  print(random_function())
elif choice == 'S':
  try:
    file = open('scores.txt','r')
    low_score = 999999
    for line in file:
      if int(line[0]) < low_score:
  
        low_score = int(line[0])
        output = line
    print(output)
  except:
    print("no scores yet")
else:
  print("learn to read")
  

  



  
    
  
  
  