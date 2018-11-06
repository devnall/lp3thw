formatter = "{} {} {} {}"

my_var1 = "I"
my_var2 = "II"
my_var3 = "III"
my_var4 = "IV"
my_var5 = "V"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(my_var1, my_var2, my_var3, my_var5))
print(formatter.format(
    "Try your",
    "\nOwn text here",
    "\nMaybe a poem",
    "\nOr a song about fear"
    ))
