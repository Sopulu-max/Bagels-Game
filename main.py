# Bagels a deductive logic game

import random

NUM_DIGITS = 4
MAX_GUESSES = 10

def get_secret_num():
  numbers = list("0123456789")
  random.shuffle(numbers)
  secret_num = ""
  for i in range(NUM_DIGITS):
    secret_num += str(numbers[i])
  return secret_num

def get_clues(guess, secret_num):
  clues = []
  if guess == secret_num:
    return "You got it!"

  for i in range(len(guess)):
    if guess[i] == secret_num[i]:
      # A correct digit is in the correct position
      clues.append("Fermi")
    elif guess[i] in secret_num:
      # A correct digit is in the incorrect position
      clues.append("Pico")
  if len(clues) == 0:
    return "Bagels" # There are no correct digits
  else:
    clues.sort()
    return " ".join(clues)


def  main():
  print(f"""Bagels a deductive logic game
  
  I am thinking of a {NUM_DIGITS}-digit number with no repeated digits
  Try to guess what number it is. Here are some clues:
  Pico: One digit is correct but in the wrong position
  Fermi: One digit is correct and in the right postion
  Bagels: No digit is correct

  For example if the correct number was 248 and your guess was 843 the clues would be Fermi, Pico and Bagels
  """)
  while True: #main game loop
    secret_num = get_secret_num()
    print("I am thought up a number")
    print(f"You have {MAX_GUESSES} guesses to get it right")

    num_guesses = 1
    while num_guesses <= MAX_GUESSES:
      guess = ""
      # keep looping until they enter a valid guess
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print(f"Guess #{num_guesses}")
        guess  = input("> ")

      clues = get_clues(guess, secret_num)
      print(clues)
      num_guesses += 1

      if guess == secret_num:
        break
      if num_guesses > MAX_GUESSES:
        print("You ran of guesses")
        print(f"The answer was {secret_num}")

    # Ask player if they want to play again
    print("Do you want to play again? (yes/no)")
    answer = str(input("> "))
    if not answer.lower().startswith("y"):
      break

  print("Thanks for playing")


if __name__ == "__main__":
  main()
  
      
      
            
       