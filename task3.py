import random
#Function to check the email and gives true if its right false if not.
def valid_email(email):
    if  (email.count("@") == 1) and (len(email.split('@')[0])>=3) and  (email.split('@')[1]== "pop.ac.uk"):
        return True
    else:
        return False
    
#Function to check the network.
def err_in_network(name):
    if random.choice([i for i in range(10)]) == 1:
        print("Unexpected, Error in Network",name,"Please try again later.")
        exit()

#Function to return answers from Chat bot.
def ans(name,quest):
    if "call" in quest.lower():
        print("who do you want to call? come again")
    elif "message" in quest.lower():
        print("who do you want to message? come again")
    elif "calender" in quest.lower():
        print("You have ",random.randint(1,6)," main events today.")
    elif "what's today" in quest.lower():
        print("You have to meet your",random.choice(["Nice.", "Got it.", "yeah", "is that true", "Yes.", "is that true?"])," today at sharp",random.randint(7,18),)
    elif "write note" in quest.lower():
        note = input("What you want to write today")
        print("Note Saved!")
    elif "resturant" in quest.lower():
        print("Resturant near you is ",random.randint(45,1000),"meter away.")
    elif any(char in quest.lower() for char in ["bye", "exit", "goodbye", "help"]):
        print("Thanks!",name," It was Great talking you!")
        exit()
    else:
        print(random.choice(["Nice.", "Got it.", "yeah", "is that true", "Yes.", "is that true?"]))

print("Welcome to Pop Chat ! \nThere is always one of our Operator is 24/7 online there to your service")

em = input("Enter your email address : ")

if valid_email(em) == False:
    exit("Email Address is Invalid!")

fname = em.split('@')[0].capitalize()  #seperate name from email
moderator = random.choice(['Eddie','Sham','Zed','Jarvis','Sophia','Alexyia'])

print(f"Hi, {fname}! Welcome! \nThis is {moderator}, from PopChat! I Heartily welcome You. You are free to ask anything in your mind. Lighten your heart with all sharing all your grief with me.")
while True:
    err_in_network(fname)
    ques = input("Give your question for the answer:")
    ans(fname,ques)
