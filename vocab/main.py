import random
from display import table

# All you have to do is change what is in 'Latin_Words.txt' by pasting in the stuff from the google docs.

with open("get_list.py") as file:
    file = file.read()
    exec(file)

terms = new_file
    
correct = [0, 0] # correct then wrong

c = -1
ack = -1
stop = False
while c == -1:
    exc = ""
    if len(terms) == 1:
        exc = terms[0][0][0] + "? "
    else:
        for i in range(len(terms)):
            if i != (len(terms) - 1):
                exc += terms[i][0][0] + ", "
            else:
                exc += "and " + terms[i][0][0] + "? "
    exc += "or display? "
    choice = input(exc)
    for i in range(int(len(terms))):
        if choice.lower() == terms[i][0][0].lower():
            c = i
            break
        if choice.lower() == "display":
            table(terms)
            c = i
            stop = True
            break
    print("")
for i in range(len(terms[c])-1):
    if stop:
        break
    answer = ""
    cont = 0
    cont2 = False
    time = 0
    for e in range(len(terms[c][i+1])):
        answer = answer+terms[c][i+1][e]
        if e != (len(terms[c][i+1]) - 1):
            answer = answer+", "
    while not cont:
        
        for b in range(len(terms[c][i+1])):
            if terms[c][i+1][b] == "f" or terms[c][i+1][b] == "m" or terms[c][i+1][b] == "n" or terms[c][i+1][b] == "m/f" or terms[c][i+1][b] == "f/m" or terms[c][i+1][b] == "none":
                ack = b
        while True:
            numb = random.randint(0,len(terms[c][i+1])-1)
            if numb != ack:
                break
        cont = terms[c][i+1][numb]
        if cont != "f" and cont != "m" and cont != "n" and cont != "m/f" and cont != "f/m" and cont != "none":
            print("")
            print(cont)
            print("")
            cont = True
    while not cont2:
        if input("").lower() == answer.lower():
            print("Correct!")
            if time == 0:
                correct[0] += 1
                time = 1
            cont2 = True
        else:
            print("Incorrect!")
            if time == 0:
                correct[1] += 1
                time = 1
            print("")
if not stop:
    print("")
    print("You got "+str(correct[0])+" right out of "+str((correct[0]+correct[1]))+".")