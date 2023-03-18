# Towers-of-Hanoi

Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.

The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

The game follows three rules:

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
No disk may be placed on top of a smaller disk.

```
#Start of Program
print("\nLet's play Towers of Hanoi!!")

#Creating the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Setting Up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

#Get User Input Method
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))

    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
          
#Playing the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.get_size == 0:
      print("\n\nInvalid Move. Try Again")
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
```

Output Example:

```
Let's play Towers of Hanoi!!

How many disks do you want to play with?
3

The fastest you can solve this game is in 7 moves

...Current Stacks...
Left Stack: [3, 2, 1]
Middle Stack: []
Right Stack: []


###Game Moves Made###


Which stack do you want to move from?

Enter L for Left
Enter M for Middle
Enter R for Right
L

Which stack do you want to move to?

Enter L for Left
Enter M for Middle
Enter R for Right
R


You completed the game in 7 moves, and the optimal number of moves is 7
```
