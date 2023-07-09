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

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type '0' for rock, '1' for paper and '2' for scissors.\n"))

# 0 = rock
# 1 = paper
# 2 = scissors
print("You Chose:\n")

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

print("\n\n Computer Chose:\n")
comp_choice = random.randint(0,2)
if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
elif comp_choice == 2:
  print(scissors)

if user_choice== 0 and comp_choice == 2:
  print("\n\nYou WIN !!")
elif user_choice== 1 and comp_choice == 0:
  print("\n\nYou WIN !!")
elif user_choice== 2 and comp_choice == 1:
  print("\n\nYou WIN !!")
elif user_choice == comp_choice:
  print("\n\nIt is a TIE !!")
else:
  print("You Lose !!")
