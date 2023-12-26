from art import logo, vs
from game_data import data
from replit import clear
import secrets

###############Function Definitions:

def validator(option_a, option_b, prompt):
  valid = True
  guess = input(prompt).upper()
  if (guess != option_a) and (guess != option_b):
    valid = False
    while not valid:
      print("\nPlease enter a valid option.")
      guess = input(prompt).upper()
      if (guess == option_a) or (guess == option_b):
        valid = True
  return guess

def intro_and_retrieval(celeb1, celeb2, score):
  prompt = "\nWho has more followers? Type 'A' or 'B': "
  print(logo)
  print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}.")
  print(vs)
  print(f"Against B: {celeb2['name']}, a {celeb2['description']} from {celeb2['country']}.")
  print(f"\nScore: {score}")
  user_choice = validator("A", "B", prompt)
  correct = evaluate(user_choice, celeb1['follower_count'], celeb2['follower_count'])
  return correct
  
def evaluate(choice, follow_count1, follow_count2):
  correct = True
  correct_answer = ""
  if follow_count1 > follow_count2:
    correct_answer = "A"
  elif follow_count2 > follow_count1:
    correct_answer = "B"
  if choice != correct_answer:
    correct = False
  return correct

###############Functions Defined:

on_streak = True
celebrity1 = secrets.SystemRandom().choice(data)
score = 0
while on_streak:
  clear()
  celebrity2 = secrets.SystemRandom().choice(data)
  if celebrity2 == celebrity1:
    celebrity2 = secrets.SystemRandom().choice(data)
  on_streak = intro_and_retrieval(celebrity1, celebrity2, score)
  if on_streak:
    score += 1
    celebrity1 = celebrity2
print(f"\nIncorrect.\n\nFinal Score: {score}")
