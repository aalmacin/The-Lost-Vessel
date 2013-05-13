import random
import time

def display_intro():
  print("You just arrived to dragon land.")
  print("You're sent in this land to search for a treasure stolen by a dragon.")
  print("You must choose the safest path so you don't run out of life or energy.\n")

def show_options():
  print("With you is a backpack which can hold special items.")
  print("To begin, you have a sword in which you can use to kill a dragon.")
  raw_input("Hit Return key to return to main menu: ")

def main_menu():
  game_running = True
  while game_running:
    print("1) Start Game.")
    print("2) Show options.")
    print("Hit Return key to exit.")

    option_num = raw_input(">>> ")
    if option_num == "1":
      start_game()
    elif option_num == "2":
      show_options()
    else:
      game_running = False

def start_game():
  play_again = True
  while play_again:
    display_intro()
    play_again = raw_input("Do you want to play again? (yes or no): ").lower() in ["yes","y"]

def main():
  main_menu()

if __name__ == "__main__": main()
