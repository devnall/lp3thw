from sys import argv

script, max_num, incr_amt = argv
max_num = int(max_num)
incr_amt = int(incr_amt)

numbers = []

def ex33(num, increment):
    i = 0
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom is {i}")

ex33(max_num, incr_amt)

print("The numbers: ")

for numb in numbers:
    print(numb)
