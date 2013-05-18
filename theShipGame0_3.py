"""
    Author Name: Aldrin Jerome Almacin
    Last Modified by: Aldrin Jerome Almacin
    Date last Modified:
    Program description: A game that asks the user to select paths that would lead to finding a treasure. There are 7 negative outcomes and one positive outcome. The player can then play the game again if desired.
    Revision History: 0.3
"""
import random
import time

"""
    Function: Display Intro
    Purpose: Displays the intro using narrate sleep.
    Input: None
    Output: The Narrated Introduction
    Params: None
    Returns: None
"""
def display_intro():
  narrate_sleep(\
    "You are a scuba diver searching for a lost vessel that sunk in the Pacific Ocean.|"\
    + "There's an abundance of tropical fish and sea creatures swimming beside you.|"\
    + "Your exploration reveals nothing significant until...|"\
    + "You discover a ship that matches what you are looking for.|"\
    + "You are now swimming beside this massive ship.|"\
    + "But you wanna know more about it."
  , 2)

"""
    Function: Start Game
    Purpose: Method to be called to start the game. In this method, the three choices are gathered from the user and the outcome based on those choices are narrated.
    Input: The choices the user selected.
    Output: The Narrated outcome
    Params: None
    Returns: None
"""
def start_game():
  NONVALID_VALUE = 2
  outcomes = get_outcomes()

  # Set all choices to nonvalid value. Can be used to determine whether the user wants to go back to first node.
  first_choice = NONVALID_VALUE
  second_choice = NONVALID_VALUE
  third_choice = NONVALID_VALUE

  # As long as the third choice is not yet set into a valid index, ask the user where he/she is going to go base on where he/she is.
  while third_choice == NONVALID_VALUE:
    # If no first choice selected yet ask the user
    if first_choice == NONVALID_VALUE:
      first_choice = get_first_choice()
    # If no second choice selected yet ask the user
    if second_choice == NONVALID_VALUE:
      second_choice = get_second_choice(first_choice)
      # If the user selected 3, then unset the first choice and narrate that the user is swimming back
      if second_choice == NONVALID_VALUE:
        first_choice = NONVALID_VALUE
        narrate_sleep("Swimming back outside the ship...")
    # If the first choice and the second choice is already set, then get the third choice.
    if first_choice != NONVALID_VALUE and second_choice != NONVALID_VALUE:
      third_choice = get_third_choice(first_choice, second_choice)

  # Show the outcome
  narrate_sleep(outcomes[first_choice][second_choice][third_choice])

"""
    Function: Get first choice
    Purpose: Method used to get where the user wants to go in the first node.
    Input: The users decision. Back or front of the ship
    Output: The prompt on whether to go to the front or the back of the ship
    Params: None
    Returns: The first decision
"""
def get_first_choice():
  return choose_place("Do you want to investigate the front or back of the ship?", "1 for front or 2 for back")

"""
    Function: Get second choice
    Purpose: Method used to get where the user wants to go in the second node. The story is based on the first decision.
    Input: The users second decision.
    Output: The prompt on which place the user wants to go to base on the first node decision
    Params:
      back_of_the_ship = boolean value used to determine whether the user selected the back of the ship on the first decision node
    Returns: The second decision
"""
def get_second_choice(back_of_the_ship):
  # The number selected by the user is also used as a boolean. 0 to false, 1 to true
  # The first  decision is used to determine what story should be shown to the user.
  # The decision is then returned by the function
  if back_of_the_ship:
    narrate_sleep("You see a round window at the back of the ship, you managed to squeeze in.|The room you got into appears to be an officer's quarters.")
    return choose_place("Do you want to investigate the room further?", "1 for yes or 2 for no or 3 to swim back")
  else:
    narrate_sleep("You see a rusty hole in front of the ship, in which your scuba barely fits in the crack.|But were able to get in.|Now you see two corridors.")
    return choose_place("Which way would you go?", "1 for left or 2 for right or 3 to swim back")

"""
    Function: Get third choice
    Purpose: Method used to get where the user wants to go in the third node. The decision is based on the first two decisions.
    Input: The users third decision.
    Output: The prompt on which place the user wants to go to base on the first and second node decision.
    Params:
      back_of_the_ship = boolean value used to determine whether the user selected the back of the ship on the first decision node
      picked_two = boolean value used to determine whether the user selected the second option on the second decision node
    Returns: The third decision
"""
def get_third_choice(back_of_the_ship, picked_two):
  # The number selected by the user is also used as a boolean. 0 to false, 1 to true
  # The first and second decision is used to determine what story should be shown to the user.
  # The decision is then returned by the function
  # Additional story narrations are added
  if back_of_the_ship:
    if picked_two:
      narrate_sleep("After you left the room...|You saw an item that looks like a chest.")
      chest_left = choose_place("Do you want to open the chest?","1 to open or 2 to leave it alone or 3 to swim back")
      if chest_left:
        narrate_sleep("After leaving the chest alone...|You saw an item.|You picked it up then...")

      return chest_left
    else:
      narrate_sleep("You decided to investigate the room further.|You then discovered that the room have a secret basement.")
      left_secret_basement = choose_place("Do you want to enter?","1 for yes or 2 for no or 3 to swim back")
      if left_secret_basement:
        narrate_sleep("After leaving the secret basement alone...|You saw an item.|You picked it up then...")
      else:
        narrate_sleep("After getting in the secret basement...|You saw an item.|You picked it up then...")

      return left_secret_basement
  else:
    if picked_two:
      narrate_sleep("You selected to dive through the right corridor.|After diving for a few meters more, you now see two strange rooms.")
      second_room = choose_place("Which room would you get in?", "1 or 2 or 3 to swim back")
      narrate_sleep("After going in the room...|You saw an item.|You picked it up then...")

      return second_room
    else:
      narrate_sleep("You selected to dive through the left corridor.|At the end of the corridor, you now see a hole in the floor and a casket.")
      opened_casket = choose_place("Do you want to go in the hole or do you want to open the casket?", "1 to go in the hole or 2 to open the casket or 3 to swim back")

      if opened_casket:
        narrate_sleep("You open the casket...|Something is inside...")
      else:
        narrate_sleep("After going in the hole...|You saw an item.|You picked it up then...")

      return opened_casket

"""
    Function: Narrate Sleep
    Purpose: Method used to show the user messages from a string with separators. The program the sleeps for 1 or any number of seconds specified.
    Input: None
    Output: The messages sent by the user
    Params:
      messages: String with a separator which separates sentences or set of words.
      secs: The amount of time the program sleeps
      split_by: The separator used to separate the string
    Returns: None
"""
def narrate_sleep(messages, secs = 1, split_by = "|"):
  for message in messages.split(split_by):
    print(message)
    time.sleep(secs)

"""
    Function: Get Outcomes
    Purpose: Method used to get the outcomes stored in a 3d array
    Input: None
    Output: None
    Params: None
    Returns: 3d array which contains all the outcomes.
"""
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

  # Set the positive outcome randomly
  nodes[random.randint(0,1)][random.randint(0,1)][random.randint(0,1)] = positive_outcome

  return nodes

"""
    Function: Choose place
    Purpose: Method used to ask the user on where he wants to go.
    Input: The decision of the user
    Output: The prompt that shows the question
    Params:
      question: The question to be shown to the user
      num_choice: The message that contains the number choices
    Returns: The decision of the user in integer subtracted by one. Substracted in order to become a valid index.
"""
def choose_place(question, num_choice):
  while True:
    place = raw_input("{0} ({1}): ".format(question,num_choice))
    if place == '1' or place == '2' or place == '3': break
  return (int(place) - 1)

"""
    Function: Main
    Purpose: The main function run by the program
    Input: The decision on whether to play again
    Output: The prompt that asks whether the user wants to play again.
    Params: None
    Returns: None
"""
def main():
  while True:
    display_intro()
    start_game()
    if(not raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]): break

# Calls the main function
if __name__ == "__main__": main()
