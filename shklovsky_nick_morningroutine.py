print ("Alarm!")


while True:
    snooze = str.lower(input("snooze?"))

    if snooze == "yes":
       print("Go back to sleep for 10 minutes")
    elif snooze == "no":
        print("Wake up!")
        break
    else:
        print ("Invalid response")
        
while True:
    shower = str.lower(input("shower?"))

    if shower == "no":
        print("Gross!")
        break
    elif shower == "yes":
        print("You're fresh")
        break
    else:
        print ("Invalid response")

while True:
    Get_dressed = input("time to get dressed")
    
    Color = str.lower(input("Blue or White shirt?"))

    if Color == "blue":
        print("It's ok...")
    elif Color == "white":
        print("Cool Color!")
        break
    else:
        print ("Invalid response")




while True:
    Eat = input("time to eat breakfast")
    
    Food = str.lower(input("Waffles or Pancakes?"))

    if Food == "waffles":
        print("mmm.. waffles")
        break
    elif Food == "pancakes":
        print("oh pancakes :<")
        break
    else:
        print ("Invalid response")

while True:
    Leave = input("time to leave for school")
    
    v = str.lower(input("will you walk,take the bus, or take a car"))

    if v == "walk":
        print("time - 11:23  you are late for school, better luck tomorrow")
        break
    elif v == "bus":
        print("time - 7:45  you are early to school, enjoy breakfest")
        break
    elif v == "car":
        print("time - 8:20  you get to school on time, enjoy your day")
        
        break
    else:
        print ("Invalid response")
      
      
