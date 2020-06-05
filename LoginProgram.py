import linecache
Sign_In = open("Sign-In.txt", "r")
a = linecache.getline("Sign-In.txt",2)
if "True" in Sign_In.read():
    L = input("Do you want to sign out? Please type yes or no.\n")
    if L == "yes":
        Sign_Out = open("Sign-In.txt", "w")
        Sign_Out.write("")
        print("Bye, "+ linecache.getline("Sign-In.txt", 2))
    elif L == "no":
        print(f"Hello {a}\nAccess Granted")
    else:
        print("Hi, nothing will happen now!")
else:
    Edit = open("Sign-In.txt", "a")
    Username = input("What is the username?\n")
    Password = input("What is the password?\n")
    FileName = Username
    file = open(f"{FileName}.txt", "r")
    file1 = open(f"{FileName}Password.txt", "r")
    Correct = False
    if "Username = " + Username in file.read():# and :
        Correct = False
    if "Password = " + Password >= file1.read():
        Correct = True
    else:
        print("Access Denied")
    if Correct == True:
        print(f"Welcome {Username}.\nAccess Granted")
        Edit.write(f"True\n{Username}.")
    file.close()
Sign_In.close()
