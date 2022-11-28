name, char = input("enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
# print(f"character count : {name.lower().count(char.lower())}") #case sensitive
print(f"character count : {name.strip().lower().count(char.strip().lower())}")
# Harshit - harshit
# H - h
# "  Harshit  " ------>"Harshit" ------> "harshit"
# "  H  "  ------> "H" -------> "h"
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()