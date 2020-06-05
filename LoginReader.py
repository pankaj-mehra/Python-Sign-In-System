Username = input("What is the Username?\n")
file = open(f"{Username}.txt", "r")
print(file.read())