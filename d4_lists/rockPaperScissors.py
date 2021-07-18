import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

def win():
  print("You won!")

def lose():
  print("You lost!")



user = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or 2 for Scissors. "))

if user > 2 or user < 0:
  print("You typed an invalid number, you lost!")
else: 
  print(game_images[user])
  cpu = random.randint(0,2)

  print("Computer chose:")
  print(game_images[cpu])

  if user == 0 and cpu == 2:
    win()
  elif user == 2 and cpu ==0:
    lose()
  elif user > cpu:
    win()
  elif user < cpu:
    lose()
  elif user == cpu:
    print("You tied!")




