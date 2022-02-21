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

img = [rock,paper,scissors]

player = int(input('What do you choose? Tye - for Rock, 0 for Paper or 1 for Scissors 2.'))
if player < 0 or player > 2:
  print('Out of range ! Pick another number')
else:
  print(img[player])

computer = len(img)-1
random_pick = random.randint(0,computer) 
print(img[random_pick])

if player  == random_pick:
  print('Draw')
elif player == 0 and random_pick == 1:
  print('You Lose')
elif player == 0 and random_pick == 2:
  print('You Win')
elif player == 1 and random_pick == 0:
  print('You Win')
elif player == 1 and random_pick == 2:
  print('You Lose')
elif player == 2 and random_pick == 0:
  print('You lose')
elif player == 2 and random_pick == 1:
  print('You Win')
