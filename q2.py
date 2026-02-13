import random

animal = random.choice(["dog", "cat", "turtle", "rabbit", "snake", "hamster", "lizard", "spider", "rock", "fish"])
if animal == "dog" or animal == "cat" or animal == "lizard" or animal == "fish":
    age = random.randrange(10, 200, 5)/10
elif animal == "rabbit":
    age = random.randrange(10, 120, 5)/10
elif animal == "snake" or animal == "spider":
    age = random.randrange(10, 300, 5)/10
elif animal == "hamster":
    age = random.randrange(10, 30, 5)/10
elif animal == "turtle":
    age = random.randrange(10, 500, 5)/10
elif animal == "rock":
    age = random.randint(100, 4000)
if animal == "dog" or animal == "rabbit" or animal == "hamster":
    color = random.choice(["golden", "white", "black", "brown", "grey"])
elif animal == "cat":
    color = random.choice(["black", "white", "creme", "tabby", "tuxedo", "tortie", "calico", "orange", "grey"])
elif animal == "turtle":
    color = random.choice(["brown", "grey", "yellow", "black", "green"])
elif animal == "snake" or animal == "lizard" or animal == "fish":
    color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown", "grey"])
elif animal == "spider":
    color = random.choice(["brown", "black", "white", "grey"])
elif animal == "rock":
    color = None
if animal == "dog":
    weight = random.randint(10, 100)
elif animal == "cat":
    weight = random.randint(8, 20)
elif animal == "turtle" or animal == "rabbit":
    weight = random.randrange(20, 100, 5)/10
elif animal == "snake":
    weight = random.randint(2, 30)
elif animal == "hamster":
    weight = random.randrange(25, 50, 5)/100
elif animal == "lizard":
    weight = random.randrange(5, 80, 5)/10
elif animal == "spider":
    weight_1 = random.randrange(5, 100, 5)/1000
    weight_2 = random.randrange(10, 40, 5)/100
    weight = random.choice([f"{weight_1}", f"{weight_2}"])
elif animal == "fish":
    weight_1 = random.randrange(10, 100, 5)/1000
    weight_2 = random.randrange(10, 100, 5)/100
    weight_3 = random.randrange(10, 200, 5)/10
    weight = random.choice([f"{weight_1}", f"{weight_2}", f"{weight_3}"])
elif animal == "rock":
    weight = random.randint(2, 1000)

if weight != "1":
    s_variable = "s"
else:
    s_variable = ""

print(f"Your pet is a {age} year old {color} {animal} that weighs {weight} pound{s_variable}.")