import random
import os
from game_data import data
from art import logo, vs

# Format account data into printable format.
def format_data(account):
  """Format account into printable format: name, description and country"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, {account_descr}, {account_country}")

## If Statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
      

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make game repeatable.
while game_should_continue:
  # Generate a random account from the game data.

  # Make B become the next A.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is correct.
      ## Get follower count.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen between rounds.
  os.system('cls')
  print(logo)
  # Give user feedback on their guess.
  # Score Keeping.
  if is_correct:
    score += 1
    print(f"You're right! Current Score : {score}")
    
  else:
    print(f"Sorry, you're wrong. Final Score : {score}.")
    game_should_continue = False
  




