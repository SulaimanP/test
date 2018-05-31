i = 0
while (i < 2):
    hungry = input("Are you hungry?")
    if hungry == "yes":
        print("Eat kabob")
    elif hungry == "i am fasting":
        print("Same")
    else:
        print("Go to sleep")
    i+=1
