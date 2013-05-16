''' Author Name: Aldrin Jerome Almacin
    Last Modified by: Aldrin Jerome Almacin
    Date last Modified:
    Program description: A game that asks the user to select paths that would lead to finding a treasure. There are 7 negative outcomes and one positive outcome. The player can then play the game again if desired.
    Revision History: 0.3
'''
import random
import time

#def display_intro():
  #narrate_sleep("You are a scuba diver searching for a lost vessel that sunk in the Pacific Ocean.|There's an abundance of tropical fish and sea creatures swimming beside you.|Your exploration reveals nothing significant until...|You discover a ship that matches what you are looking for.|You are now swimming beside this massive ship.|But you wanna know more about it.", 2)

def start_game():
  outcomes = get_outcomes()

  first_choice = get_first_choice()
  second_choice = get_second_choice(first_choice)
  third_choice = get_third_choice(first_choice, second_choice)

  narrate_sleep(outcomes[first_choice][second_choice][third_choice])

def get_first_choice():
  return choose_place("Do you want to investigate the front or back of the ship?", "1 for front or 2 for back")

def get_second_choice(back_of_the_ship):
  if back_of_the_ship:
    narrate_sleep("You see a round window at the back of the ship, you managed to squeeze in.|The room you got into appears to be an officer's quarters.")
    return choose_place("Do you want to investigate the room further?", "1 for yes or 2 for no")
  else:
    narrate_sleep("You see a rusty hole in front of the ship, in which your scuba barely fits in the crack.|But were able to get in.|Now you see two corridors.")
    return choose_place("Which way would you go?", "1 for left or 2 for right")

def get_third_choice(back_of_the_ship, picked_two):
  if back_of_the_ship:
    if picked_two:
      narrate_sleep("After you left the room...|You saw an item that looks like a chest.")
      chest_left = choose_place("Do you want to open the chest?","1 to open or 2 to leave it alone")
      if chest_left:
        narrate_sleep("After leaving the chest alone...|You saw an item.|You picked it up then...")
      return chest_left
    else:
      narrate_sleep("You decided to investigate the room further.|You then discovered that the room have a secret basement.")
      left_secret_basement = choose_place("Do you want to enter?","1 for yes or 2 for no")
      if left_secret_basement:
        narrate_sleep("After leaving the secret basement alone...|You saw an item.|You picked it up then...")
      else:
        narrate_sleep("After getting in the secret basement...|You saw an item.|You picked it up then...")
      return left_secret_basement
  else:
    if picked_two:
      narrate_sleep("You selected to dive through the right corridor.|After diving for a few meters more, you now see two strange rooms.")
      second_room = choose_place("Which room would you get in?", "1 or 2")
      narrate_sleep("After going in the room...|You saw an item.|You picked it up then...")

      return second_room
    else:
      narrate_sleep("You selected to dive through the left corridor.|At the end of the corridor, you now see a hole in the floor and a casket.")
      opened_casket = choose_place("Do you want to go in the hole or do you want to open the casket?", "1 to go in the hole or 2 to open the casket")

      if opened_casket:
        narrate_sleep("You open the casket...|Something is inside...")
      else:
        narrate_sleep("After going in the hole...|You saw an item.|You picked it up then...")

      return opened_casket

def narrate_sleep(messages, secs = 1, split_by = "|"):
  for message in messages.split(split_by):
    print(message)
    time.sleep(secs)

def get_outcomes():
  # All negative outcomes
  first_outcome = "You got sucked in by an unknown force and died.|Game Over..."
  second_outcome = "The casket is a home of a sea vampire and he bit you.|You then runned out of blood and died.|Game Over..."
  third_outcome = "You realize the room you went into contains bombs from world war 2 ready to explode.|Booooom!!!|Game Over..."
  fourth_outcome = "You realize the room you went into is the home of an ancient sea dragon.|He gobbles you down in one bite.|Game Over..."
  fifth_outcome = "The door suddenly closed causing you to be locked up until you die...|Game Over..."
  sixth_outcome = "A giant octupus came and stripped you out causing you to drown.|Game Over..."
  seventh_outcome = "You opened the treasure chest...|There are interesting items inside...|A venomous snake then bit you causing you to die.|Game Over..."
  eighth_outcome = "A shark suddenly came and ate you.|Game Over..."

  # The lone positive outcome
  positive_outcome = "You just found a historical item worth billions.|You then returned home happily.|Game Over..."

  nodes = [[[first_outcome,second_outcome],[third_outcome,fourth_outcome]],[[fifth_outcome,sixth_outcome],[seventh_outcome,eighth_outcome]]]
  nodes[random.randint(0,1)][random.randint(0,1)][random.randint(0,1)] = positive_outcome

  return nodes

def choose_place(question, num_choice):
  while True:
    place = raw_input("{0} ({1}): ".format(question,num_choice))
    if place == '1' or place == '2': break
  return (int(place) - 1)

def main():
  while True:
#    display_intro()
    start_game()
    if(not raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]): break

if __name__ == "__main__": main()
