# Character generator plus battle

import random, os
from time import sleep
global A
global B
global name
global battleA
global battleB

def name():
  name = input("Give a name to your newborn character: ")
  print()
  return name

def type(Name):
  type = input("Write the type you want to assign to your character. Choose betweeen Human, Imp, Wizard or Elf: ")
  print()
  if type == "human" or type == "Human":
    print("Congratulations!",Name,"is a Human.")
    print("Well, that's not such a great new, but yeah...")
  elif type == "Imp" or type == "imp":
    print("Congratulations!",Name,"is an Imp.")
    print("«O impious imp, be ye turned to stone»!")
  elif type == "Wizard" or type == "wizard":
    print("Congratulations!",Name,"is a Wizard.")
    print("And no, it did not went to Hogwartz")
  elif type == "Elf" or type == "elf":
    print("Congratulations!",Name,"is an Elf.")
    print("«I’m very elf-sufficient»")
  return type

def diceRoll(X):
    roll = random.randint(1, X)
    int(roll)
    return roll
   
def health():
    health = ((diceRoll(6) * diceRoll(12)) / 2) + 10
    print("HEALTH: ",health,)
    return health
  
def strength():
    strength = ((diceRoll(6) * diceRoll(12)) / 2) + 12
    print("STRENGTH: ",strength,)
    return strength

def characterA():
    print("Player 1")
    print()
    NameA = name()
    TypeA = type(NameA)
    HealthA = health()
    StrenghtA = strength()
    global A
    A = NameA, TypeA, HealthA, StrenghtA
    return(A)

def characterB():
    print("Player 2")
    print()
    NameB = name()
    TypeB = type(NameB)
    HealthB = health()
    StrenghtB = strength()
    global B
    B = NameB, TypeB, HealthB, StrenghtB
    return(B)

def menu():
  print("💥 Dice Battle Arena 💥")
  print()
  sleep(1)

def cb():
  print("⚔️  Character Builder  ⚔️")
  print()
  characterA()
  os.system("clear")
  menu()
  print("⚔️  Character Builder ⚔️")
  print()
  characterB()
  os.system("clear")

# The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
# Find the difference between the strength of both opponents and add one.
# Take that amount away from the loser's health.

def battle():
    counter = 0
    while True:
        counter =+1
        print("Battle time! ",counter,"🔪🔪🔪")
        print("Player 1:",A[0])
        roll = input("Press 'r' to roll the dice: ")
        if roll == "r" or roll == "R":
          battleA = diceRoll(6)
        else:
          print()
          roll = input("You pressed",roll,"Press 'r' to roll the dice or any other letter to exit")
          if roll == "r" or roll == "R":
            battleA = diceRoll(6)
          else:
            exit()
        print("Result:")
        print(battleA)
        print()
        print("Player 2:",B[0])  
        roll = input("Press 'r' to roll the dice: ")
        if roll == "r" or roll == "R":
          battleB = diceRoll(6)
        else:
          print()
          roll = input("You pressed",roll,"Press 'r' to roll the dice or any other letter to exit")
          if roll == "r" or roll == "R":
            battleB = diceRoll(6)
          else:
            exit()
        print("Result:")
        print(battleB)
        print()
        
        print(A)
        print(B)
        
        diff = A[3] - B[3]
        if diff <= 0:
          diff *= -1
        else:
          pass
        diff = diff + 1  
 
        if battleA > battleB:
          print(A[0],"wins!")
          global HealthA
          global HealthB
          HealthA = A[2]
          float(HealthA)
          HealthB = B[2]
          float(HealthB)
          print(B[0],"loses",diff)
          score()
          print()
          sleep(5)
          os.system("clear")
        elif battleA < battleB:
          print(B[0],"wins!")
          HealthB =  - diff
          HealthA = A[2]
          print(A[0],"loses",diff)
          score()
          print()
          sleep(5)
          os.system("clear")
        else:
          print("Tied! Roll again...")
          print()
        return HealthA
        return HealthB
        if A[2] <= 0 or B[2] <= 0:
          print("Game over!")
          if A[2] <= 0:
            print(A[0],"died!")
            print(B[0],"wins!")
            print()
            score()
            break
          else:
            print(B[0],"died!")
            print(A[0],"wins!")
            print()
            score()
            break
        else:
          score()
          os.system("clear")
          continue
            
# To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
# Extra points for the use of emojis, colors, or even sound code!

def score():
    print(A[0],"health: ")
    print(HealthA)
    print(B[0],"health: ")
    print(HealthB)

def end():
        print()

HealthA = ""
HealthB = ""

menu()
cb()
while True:
  battle()
 


# break
# repeat = input("Again?...")  
# if repeat == "no" or repeat == "No" or repeat == "NO":
#   os.system("clear")
#   print("Ok, bye!")
#   break
# else:
#   print()
#   os.system("clear")
#   sleep(1)
#   continue