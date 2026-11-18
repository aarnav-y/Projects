import random
secret = random.randint(1,5)
print(20 * "=")
print("NUMBER GUESSING GAME")
print(20 * "=")
attempts = 1
print("GUESS THE NUMBER BETWEEN 1 AND 5")
while attempts<=3:
  guess = int(input("Enter your guess: "))
  if guess==secret:
    print("😁CORRECT GUESS!!")
    break
  elif attempts<3:
    print("😭WRONG GUESS, TRY AGAIN!!")
  attempts+=1
else:                                      #when user completed all 3 attempts but didn't give correct answer
  print("😱GAME OVER, NO CHANCES LEFT")
  print(f"The secret number was {secret}")