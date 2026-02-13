import random

def spin_twister_spinner():
  colors = ["red", "green", "yellow", "blue"]
  sides = ["left", "right"]
  body_part = ["hand", "foot"]
  output = f"{random.choice(sides)} {random.choice(body_part)} on {random.choice(colors)}"
  return output

# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  print(spin_twister_spinner())