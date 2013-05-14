import random
import time

def display_intro():
  print ("")
  print ("")
  print ("")
  print ("\n")

def get_outcomes():
  nodes = [[["N","N"],["N","N"]],[["N","N"],["N","N"]]]
  nodes[random.randint(0,1)][random.randint(0,1)][random.randint(0,1)] = "P"
  return nodes

def choose_place(place):
  while True:
    place = raw_input("Which {} will you go into? (1 or 2): ".format(place))
    if place == '1' or place == '2': break
  return int(place)

def main():
  while True:
    display_intro()
    first_chosen = choose_place("Bangin")
    second_chosen = choose_place("Look")
    third_chosen = choose_place("Quad")
    outcomes = get_outcomes()
    print(outcomes[first_chosen][second_chosen][third_chosen])
    if(not raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]): break

if __name__ == "__main__": main()
