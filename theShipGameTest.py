"""
    Author Name: Aldrin Jerome Almacin
    Last Modified by: Aldrin Jerome Almacin
    Date last Modified: 05/20/2013
    Program description: Tests how many times the user will win in 100 tries. The input is randomly selected. It is also used to test if the logic on setting nodes works. Each 100 tries is written in a csv file named test-data.csv. The 100 tries is used to determine the percentages of winning so it's fair to get it to be tested more than once.
    Revision History: 0.3
"""
import random
import time
import csv

"""
  Purpose: Starts the test.
"""
def start_game():
  # Get the outcomes array. The array in which the positive outcome is set.
  outcomes = get_outcomes()

  # Set the first, second, and third choice to random
  first_choice = random.randint(0,1)
  second_choice = random.randint(0,1)
  third_choice = random.randint(0,1)

  return outcomes[first_choice][second_choice][third_choice]

"""
  Purpose: Get the possible outcomes. There is only one positive outcome.
"""
def get_outcomes():
  # Set all outcomes to negative
  nodes = [[[0,0],[0,0]],[[0,0],[0,0]]]

  # Set the positive outcome randomly
  nodes[random.randint(0,1)][random.randint(0,1)][random.randint(0,1)] = 1
  return nodes

"""
  Purpose: Main function used to call the methods to start the game.
"""
def main():
  set_count = 0
  with open('test-data.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(["Win", "Lose"])
    while set_count < 100:
      test_count = 0
      win = 0
      lose = 0
      while test_count < 100:
        if start_game():
          win += 1
        else:
          lose += 1
        test_count += 1

      print("Win: " + str(win))
      print("Lose: " + str(lose))

      csvwriter.writerow([win, lose])
      set_count += 1

# Calls the main function
if __name__ == "__main__": main()
