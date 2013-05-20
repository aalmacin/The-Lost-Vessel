"""
    Author Name: Aldrin Jerome Almacin
    Last Modified by: Aldrin Jerome Almacin
    Date last Modified: 05/20/2013
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
  narrate_sleep(
    "You are a scuba diver searching for a lost vessel that sunk in the Pacific Ocean.|"
    + "There's an abundance of tropical fish and sea creatures swimming beside you.|"
    + "Your exploration reveals nothing significant until...|"
    + "You discover a ship that matches the kind of vessel you are looking for.|"
    + "You're now approaching the ship...|"
    + "...|"
    + "...|"
    + "You are now beside this massive ship.|"
    + "You're investigation will then begin.", 2.5)

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
    # Make sure that the first choice is a valid value though
    if second_choice == NONVALID_VALUE and first_choice != NONVALID_VALUE:
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
  return choose_place("Do you want to investigate the front or back of the ship?", "1 - Investigate the front of the ship.|2 - Investigate the back of the ship.")

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
    narrate_sleep(
      "You see a round window at the back of the ship...|"
      + "You decided to go further inside the ship.|"
      + "You squeezed in.|"
      + "Looking around...|"
      + "The room you got into appears to be an officer's quarters."
    )
    return choose_place("Do you want to investigate the room further?", "1 - Investigate further.|2 - Leave the room.|3 - Swim back outside the ship.", "|", True)
  else:
    narrate_sleep(
      "You see a rusty hole in front of the ship...|"
      + "You wanted to go further inside the ship.|"
      + "Your scuba will barely fit in the crack.|"
      + "You tried to get in.|"
      + "And...|"
      + "You were able to get in.|"
      + "After getting in...|"
      + "You now see a corridor and a staircase."
    )
    return choose_place("Which way would you go?", "1 - Go through the corridor.|2 - Swim up the staircase.|3 - Swim back outside the ship.", "|", True)

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
      narrate_sleep(
        "After leaving the officers quarters...|"
        + "You are now in the corridor.|"
        + "When...|"
        + "A very hungry shark suddenly came to devour you...|"
        + "Swim...|"
        + "Swim...|"
        + "Swim...|"
        + "You found a giant wardrobe..."
      )
      left_wardrobe_alone = choose_place("Do you want to get in?","1 - Get in.|2 - Leave it alone.")
      if left_wardrobe_alone == 1:
        narrate_sleep(
          "After leaving the wardrobe alone...|"
          + "You found a place which looks safer.|"
          + "It looks like you lost the shark...|"
          + "You are now in a room filled with books.|"
          + "When...|"
          + "Your eye caught an interesting item.|"
          + "You picked it up then..."
        )
      else:
        narrate_sleep(
          "After getting inside the wardrobe...|"
          + "The shark tried to sneak in but his head got smashed after you closed the wardrobe door.|"
          + "Poor shark...|"
          + "He's now dead...|"
          + "You then went outside the wardrobe.|"
          + "You noticed that your feet touched something interesting.|"
          + "It looks like a very rare mineral.|"
          + "You picked it up then..."
        )

      return left_wardrobe_alone
    else:
      narrate_sleep(
        "You decided to investigate the officers quarters further.|"
        + "There are interesting items inside the officers quarters.|"
        + "You see a brass candleholder.|"
        + "You tried to get it.|"
        + "But it accidentally slipped off your hands.|"
        + "You tried to quickly pick it up...|"
        + "But...|"
        + "It fell on something deeper...|"
        + "You discovered that the room have a secret basement..."
      )
      left_secret_basement_alone = choose_place("Do you want to enter the secret basement?","1 - Enter the secret basement.|2 - Continue investigating inside the officers quarters.")
      if left_secret_basement_alone == 1:
        narrate_sleep(
          "There are very old items in the quarters...|"
          + "You looked to the left and you see...|"
          + "Medals...|"
          + "Thropies...|"
          + "And there is also a very old picture...|"
          + "You looked to the right and you see...|"
          + "Cups...|"
          + "Something shiny...|"
          + "Wait...|"
          + "What is that?|"
          + "You approached it...|"
          + "You picked it up then..."
        )
      else:
        narrate_sleep(
          "It is very dark inside the secret basement...|"
          + "You pulled your flashlight out...|"
          + "But it's still so dark...|"
          + "You heard a roar...|"
          + "Then a screeching sound...|"
          + "You realized it is not a good idea you went inside...|"
          + "You are now doing your best to get out...|"
          + "When you suddenly dropped your flashlight...|"
          + "Causing you to swim on the wrong direction...|"
          + "You continued swimming...|"
          + "Then...|"
          + "You bumped into something...|"
          + "It spoke and it said that he's an ancient sea dragon...|"
          + "He held you inside his left claw...|"
          + "And swam you back up to the officer's quarters...|"
          + "He released you...|"
          + "Then opened up his other claw...|"
          + "You saw something shiny...|"
          + "He asked you to take it...|"
          + "That's what you did.|"
          + "Then..."
        )

      return left_secret_basement_alone
  else:
    if picked_two:
      narrate_sleep(
        "You selected to swim up the staircase.|"
        + "There is a door at the end of the staircase.|"
        + "There is a label that says...|"
        + "Engine Room.|"
        + "You are now in the engine room.|"
        + "The engine is massive.|"
        + "You are amazed on how this engine can make the vessel run.|"
        + "You went around the room.|"
        + "You then saw a lever.|"
        + "You are now very curious on what this lever does."
      )
      examine_lever = choose_place("What are you going to do with the lever?", "1 - Pull the lever.|2 - Examine where it's connected.")
      if examine_lever == 1:
        narrate_sleep(
          "The lever is rusty...|"
          + "It is connected to a separate room.|"
          + "You went inside that room.|"
          + "Nothing interesting in the room except it's filled with filth.|"
          + "You decided to go outside the room.|"
          + "But you went out the wrong door.|"
          + "Interesting...|"
          + "Now you are in a room filled tools and mechanical parts.|"
          + "You are examining these items.|"
          + "When...|"
          + "You saw a very interesting item...|"
          + "You picked it up then..."
        )
      else:
        narrate_sleep(
          "After pulling the lever...|"
          + "Nothing happened.|"
          + "You decided to just leave the engine room.|"
          + "You are about to go outside the engine room.|"
          + "When...|"
          + "You saw an old clock in the corner of the room.|"
          + "The clock looks interesting.|"
          + "It looks like it's made of gold.|"
          + "You got really excited.|"
          + "You picked it up then..."
        )

      return examine_lever
    else:
      narrate_sleep(
        "You decided to go through the corridor...|"
        + "The corridor is filled with holes...|"
        + "Small holes...|"
        + "There are rooms in which the doors are open...|"
        + "They look like regular bedrooms...|"
        + "You continued swimming until...|"
        + "You reached the end of the corridor...|"
        + "At the end of the corridor...|"
        + "There is a room in the right...|"
        + "You decided to go in that room...|"
        + "Inside the room...|"
        + "There is a big hole in the floor..."
      )
      ignore_hole = choose_place("Go in the hole or just ignore it?", "1 - Go in the hole.|2 - Ignore the hole.")

      if ignore_hole == 1:
        narrate_sleep(
          "You just ignored the big hole...|"
          + "You look around the room...|"
          + "You saw a chest...|"
          + "You tried to open it...|"
          + "But it's locked...|"
          + "You saw the key in a keyholder...|"
          + "You swim to get it...|"
          + "You now hold the key.|"
          + "You used it to open the chest...|"
          + "Inside the chest...|"
          + "There is an interesting item...|"
          + "You picked it up then..."
        )
      else:
        narrate_sleep(
          "You went inside the hole...|"
          + "It is dark inside the hole...|"
          + "You used your flashlight to see what's inside...|"
          + "Something's shining at the end of the hole...|"
          + "You continued swimming...|"
          + "Now you are at the bottom of the hole...|"
          + "The shining item is within your grasp...|"
          + "You picked it up.|"
          + "It looks like a very valuable item...|"
          + "You are very happy on what you picked up...|"
          + "Then..."
        )

      return ignore_hole

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
def narrate_sleep(messages, secs = 2, split_by = "|"):
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
  first_outcome = "You suddenly felt that the water around you is moving weird.|Then you suddenly got sucked in by an unknown force and died.|Game Over..."
  second_outcome = "Boooom!!!|It turned out that the item you picked up is a bomb from World War 2.|Game Over..."
  third_outcome = "The engine exploded...|You shouldn't have pulled the lever..|Tsk tsk...|Game Over..."
  fourth_outcome = "The ocean suddenly shakes...|There is an earthquake...|One big mechanical part fell onto you...|You got crushed...|Game Over..."
  fifth_outcome = "You just found a historical item worth billions...|But the dragon gobbles you down in one bite...|Game Over..."
  sixth_outcome = "It's huge body appeared.|Uh oh...|The thing you are holding is a giant octopus's tentacle.|He stripped you down and devoured you...|Game Over..."
  seventh_outcome = "The shark's friends came to avenge his death...|You tried to swim away...|But there're sharks everywhere.|They came all at once...|And you got shredded to pieces.|Game Over..."
  eighth_outcome = "The shark caught up...|You tried to lose him again...|But...|He's more determined this time...|He opened his jaws...|And...|You became his dinner...|Game Over..."

  # The lone positive outcome
  positive_outcome = "You realized that...|You just found a historical item worth billions.|You then returned home happily.|Game Over..."

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
def choose_place(question, num_choice, split_by = "|", exempted = False):
  while True:
    # SHow the question
    print(question)
    # Show each option
    for choice in num_choice.split(split_by):
      print(choice)
    # Take the choice
    place = raw_input(">>> ")
    # Exit the loop if 3 is entered and is exempted.
    if place == '3' and exempted: break
    if place == '1' or place == '2': break
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
