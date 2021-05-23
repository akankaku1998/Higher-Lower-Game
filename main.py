from art import logo, vs
from game_data import data
import random
from replit import clear

def random_data(data):
  return random.choice(data)

def display(A, B):
  print(f"Campare A: {A['name']}, {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

def compare(A, B):
  if A['follower_count'] > B['follower_count']:
    return True
  else:
    return False

def game_start():
  should_continue = True
  score = 0
  while should_continue:
    clear()
    print(logo)

    if score != 0:
      print(f"You're right! Current score: {score}.")
    if score == 0:
      A = random_data(data)
    B = random_data(data)

    display(A, B)
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if (choice == 'A' and compare(A, B)) or (choice == 'B' and compare(B, A)):
      score += 1
      A = B
    else:
      should_continue = False
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")

game_start()