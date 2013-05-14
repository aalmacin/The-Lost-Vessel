import random
import time

def display_intro():
  print ('You are on a planet full of dragons. In front of you,')
  print ('you see two caves. In one cave, the dragon is friendly')
  print ('and will share his treasure with you. The other dragon')
  print ('is greedy and hungry, and will eat you on sight.')
  print

def main():
  play_again = True
  while play_again:
    display_intro()
    play_again = raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]

if __name__ == "__main__": main()
