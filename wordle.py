""" A simple wordle game in python# The computer chooses a random 5-letter word from a list# The player has 6 guesses to find the word# The computer gives feedback for each guess# A green square means the letter is in the correct position# A yellow circle means the letter is in the word but not in the correct position# A gray dot means the letter is not in the word"""
import random
# A list of possible 5-letter words
words = ["about", "above", "acorn", "adapt", "admit", "adopt", "adult", "agent", "alarm", "album", "alert", "alike", "alive", "allow", "alone", "along", "among", "angel", "anger", "angle", "ankle", "apple", "apron", "arise", "array", "arrow", "aside", "asked", "asset", "audio", "avoid", "award", "aware", "baker", "basic", "beach", "beard", "beast", "begin", "being"]
# The computer chooses a random word from the list
word = random.choice(words)
# The player has 6 guesses
guesses = 6
# A loop to play the game
while guesses > 0:    # The player enters a guess    
  guess = input("Enter a 5-letter word: ").lower()    # Check if the guess is valid    
  if len(guess) != 5 or not guess.isalpha():
    print("Invalid guess. Try again.")        
    continue    
    # Check if the guess is correct    
  if guess == word:        
    print("You win! The word was:", word)        
    break    
      # Give feedback for each letter in the guess    
  feedback = ""    
  for i in range(5):        
    if guess[i] == word[i]:            
      feedback += "\u25A0" # green square        
    elif guess[i] in word:            
      feedback += "\u25CB" # yellow circle        
    else:            
      feedback += "\u25CF" # gray dot    
    print(feedback)    
# Reduce the number of guesses by one    
  guesses -= 1
# If the player runs out of guesses, they lose
  if guesses == 0:    
    print("You lose. The word was:", word)