import random
import time

def display_intro():
  print ("You are a scuba diver searching for a lost vessel that sunk in the Pacific Ocean.")
  time.sleep(1)
  print ("There's an abundance of tropical fish and sea creatures swimming beside you.")
  time.sleep(1)
  print ("Your exploration reveals nothing significant until...")
  time.sleep(1)
  print ("You discover a ship that matches what you are looking for.")

def start_game():
  outcomes = get_outcomes()

  choices = [1,2,3]
  choices[0] = choose_place("Do you want to investigate the front or back of the ship?", "1 for front or 2 for back")

  if not choices[0]:
    choices[1] = choose_place("You see a rusty hole, in which your scuba barely fits in the crack.\nBut were able to get in.\nNow you see two corridors.\nWhich way would you go?", "1 for left or 2 for right")
    choices[2] = choose_place("You selected to dive through this corridor.\nAfter diving for a few meters more, you now see two strange rooms.\nWhich room would you get in?", "1 or 2")
  else:
    choices[1] = choose_place("You see a round window, you managed to squeeze in.\nThe room you got into appears to be an officer's quarters.\nDo you want to investigate the room further?", "1 for yes or 2 for no")
    if not choices[1]:
      choices[2] = choose_place("You decided to investigate the room further.\nYou then discovered that the room have a secret basement.\nDo you want to enter?","1 for yes or 2 for no")
    else:
      choices[2] = choose_place("After you left the room, you saw two items that looks like treasure chests.\nWhich one would you want to open?","1 or 2")

  print(outcomes[choices[0]][choices[1]][choices[2]])

def get_outcomes():
  nodes = [[["N","N"],["N","N"]],[["N","N"],["N","N"]]]
  nodes[random.randint(0,1)][random.randint(0,1)][random.randint(0,1)] = "P"
  return nodes

def choose_place(description, num_choice):
  while True:
    place = raw_input("{0} ({1}): ".format(description,num_choice))
    if place == '1' or place == '2': break
  return (int(place) - 1)

def main():
  while True:
    display_intro()
    start_game()
    if(not raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]): break

if __name__ == "__main__": main()
