i = 0
while (i < 2):
    hungry = input("Are you hungry?")
    if hungry == "yes":
        print("Eat kabob")
        print("Eat chocolate cake")
    elif hungry == "i am fasting":
        print("Same")
    else:
        thirsty=input("are you thirsty?")
        if thirsty=="yes":
            print("drink water")
        print("Go to sleep")
    i+=1
