import time

def login():
    print("Logging in...")
    time.sleep(1.5)
    print("done!")
    time.sleep(0.4)
    dat.close()

dat = open("data.txt", "a+")

usrnme = input("Enter your username: ")

if usrnme != "Work":
    print("Sorry, unrecognised username.")
    exit()

elif usrnme != "Home":
    print("Sorry, unrecognised username.")
    exit()

elif usrnme != "Play":
    print("Sorry, unrecognised username.")
    exit()


else:
    dat.write("Log-1: Username: " + usrnme + "; Password: ")

psswd = input("Enter your password: ")

if usrnme == "Work" and psswd == "Iamatwork":
    login()
    history = open("data-work.txt", "a+")
    while True:
        wrkshl = str(input("Work@Computer-89$ "))
        history.write(wrkshl + "\n")
elif usrnme == "Home" and psswd == "Iamathome":
    login()
    history = open("data-home.txt" "a+")
    while True:
        hmeshl = str(input("Home@Computer-89$ "))
        history.write(hmeshl + "\n")
elif usrnme == "Play" and psswd == "Iamatplay":
    login()
    history = open("data-play.txt", "a+")
    while True:
        plyshl = str(input("Play@Computer-89$ "))
        history.write(plyshl + "\n")


        


