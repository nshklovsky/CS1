import random

print("Hello world! welcome the all knowledgeable magic 8-ball")

while True:
    question = str.lower(input("What would you like to ask the 8-ball? "))

    if question == "stop":
        print("bye")
        break
    elif '?' in question:
        print(random.choice(["It is certain", "It is decidedly so","Very doubtful","Outlook not so good","Don't count on it","My reply is no","My sources say no","Without a doubt","Yes definitely","Concentrate and ask again","Cannot predict now","Ask again later","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again"]))
    else:
        print("Please ask as a question")




