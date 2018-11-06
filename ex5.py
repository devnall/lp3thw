name = 'Drew Nall'
age = 39 # not a lie
height = 73 # inches
weight = 250 # lbs
eyes = 'Hazel'
teeth = 'Yellow'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"{height} inches works out to about {round(height * 2.54)} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's pretty heavy.")
print(f"{weight} pounds works out to", weight * .45, "kilograms. That sounds a bit better...")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
