import random

runner = True
games_played = 0
games_won = 0

while runner:
  print("==SCOREBOARD==")
  print(f"Games Played: {games_played}")
  print(f"Games Won: {games_won}")
  print()
  magic_number = random.randint(1,100)
  counter = 7
  previous_guesses = []
  print("Welcome to the Million dollar game.")
  print("You will have 5 opportunities.")
  print("Think carefully.")
  
  
  while counter > 0:
    print("You previously guessed:")
    print(previous_guesses)
    user_guess = int(input("Guess a number between 1 and 100: "))
    previous_guesses.append(user_guess)
  
    if magic_number == user_guess:
      print("You won!")
      games_won += 1
      break
    elif user_guess < magic_number:
      print("Your guess was too low:")
    elif user_guess > magic_number:
      print("Your guess was too high.")
  
    counter -= 1
  
  if counter <= 0:
    print("You lose!")

  games_played += 1
  runner = input("Would you like to play again(y/n)? ")
  if runner == "y":
    runner = True
  if runner == "n":
    runner = False

  
