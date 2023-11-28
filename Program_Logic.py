from Stack_Class import *

# Function to display the current state of the stacks
def display_stacks():
  print("\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()

# Function to get user input for stack selection
def get_input():
  # Create a list of the first characters of stack names
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    # Display stack options for user input
    for i, stack in enumerate(stacks):
      name = stack.get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))

    user_input = input("")

    try:
      if user_input in choices:
        return stacks[choices.index(user_input)]
      else:
        raise IndexError("Invalid stack selection.")
    except IndexError as e:
      print(f"Error: {e}. Please enter a valid option.")

if __name__ == "__main__":
  # Introduction to the Towers of Hanoi game
  print("\nLet's play Towers of Hanoi!!")

  # Creating the stacks
  stacks = [Stack("Left"), Stack("Middle"), Stack("Right")]

  # Getting the number of disks from the user with input validation
  num_disks = 0
  while num_disks < 3:
    try:
      num_disks = int(input("\nHow many disks do you want to play with?\n"))
    except ValueError:
      print("Please enter a valid integer.")

  # Initializing the left stack with the selected number of disks
  for disk in range(num_disks):
    stacks[0].push(disk)

  # Calculating the optimal number of moves
  num_optimal_moves = (2 ** num_disks) - 1
  print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

  # Initializing the user moves counter
  num_user_moves = 0

  try:
    # Main game loop until all disks are on the right stack
    while stacks[2].get_size() != num_disks:
      display_stacks()

      # Inner loop for getting valid user moves
      while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        # Validating the move
        if from_stack.get_size() == 0:
          print("\n\nInvalid Move. Try Again")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
          disk = from_stack.pop()
          to_stack.push(disk)
          num_user_moves += 1
          break
        else:
          print("\n\nInvalid Move. Try Again")

    # Game completion message
    print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))

  except KeyboardInterrupt:
    # Handling keyboard interrupt (e.g., Ctrl+C)
    print("\n\nGame aborted. Thanks for playing!")
