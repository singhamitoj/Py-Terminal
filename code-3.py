import time

def login():
    print("Logging in...")
    time.sleep(1.5)
    print("done!")
    time.sleep(0.4)

usrnme = input("Enter your username: ")

if usrnme != "Home":
    print("Sorry, unrecognised username.")
    exit()

psswd = input("Enter your password: ")
if usrnme == "Home" and psswd == "Iamathome":
    login()
    history = open("data-home.txt", "a+")
    while True:
        hmeshl = str(input("Home@Computer-89$ "))
        history.write(hmeshl + "\n")
        if hmeshl == "exit":
            exit()
        elif hmeshl == "hello":
            print("Hello, World!")
        elif hmeshl == "input":
            inpt = input("Enter text: ")
            txt = open("txtfiledat.txt", "a+")
            txt.write(inpt + "\n")
            print("Type 'input' again to add a new line.")
else:
    print("Sorry, incorrect password.")
    exit()
