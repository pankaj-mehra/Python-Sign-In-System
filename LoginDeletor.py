import os
delete = input("What user to delete?\n")
os.remove(delete + ".txt")
os.remove(delete + "Password.txt")