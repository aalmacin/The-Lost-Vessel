import random
import time

def display_intro():
  print ('You are on a planet full of dragons. In front of you,')
  print ('you see two caves. In one cave, the dragon is friendly')
  print ('and will share his treasure with you. The other dragon')
  print ("is greedy and hungry, and will eat you on sight.\n")

def choose_cave():
  while True:
    cave = raw_input('Which cave will you go into? (1 or 2): ')
    if cave == '1' or cave == '2': break
  return cave

def check_cave(chosen_cave):
  print ('You approach the cave...')
  time.sleep(2)
  print ('It is dark and spooky...')
  time.sleep(2)
  print ('A large dragon jumps out in front of you! He opens his jaws and...')
  print
  time.sleep(2)

  friendly_cave = random.randint(1, 2)

  if chosen_cave == str(friendly_cave):
    print ('Gives you his treasure!')
  else:
    print ('Gobbles you down in one bite!')

def main():
  while True:
    display_intro()
    chosen_cave = choose_cave()
    check_cave(chosen_cave)
    if(not raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]): break

if __name__ == "__main__": main()
