import random


def all_principal_parts(VERBS) -> None:
    
    score = {
        "correct": 0,
        "incorrect": 0
    }
    
    while True:
        
        word = random.choice(VERBS)
        rword = word.get_random_form()
        
        print(f"\n{rword[0]}. (type \"quit\" to quit) (first, second, third, fourth)")
        
        k = input("")
        
        if k == "quit":
            print("")
            break
        
        if [i.strip().lower() for i in k.split(",")] == list(word):
            print("Correct")
            score["correct"] += 1
        else:
            print("Incorrect. " + str(word))
            score["incorrect"] += 1
        
    print(f"Correct: {score.get('correct')}")
    print(f"Incorrect: {score.get('incorrect')}")
    

def first_principal_part(VERBS) -> None:
    
    score = {
        "correct": 0,
        "incorrect": 0
    }
    
    while True:
        
        word = random.choice(VERBS)
        rword = word.get_random_form()
        
        print(f"\n{rword[0]}. (type \"quit\" to quit) (first)")
        
        k = input("")
        
        if k == "quit":
            print("")
            break
        
        if k.strip().lower() == word.first:
            print("Correct")
            score["correct"] += 1
        else:
            print("Incorrect. " + word.first)
            score["incorrect"] += 1
        
    print(f"Correct: {score.get('correct')}")
    print(f"Incorrect: {score.get('incorrect')}")
    

def any_principal_parts(VERBS) -> None:
    
    score = {
        "correct": 0,
        "incorrect": 0
    }
    
    while True:
        
        word = random.choice(VERBS)
        rword = word.get_random_form()
        
        print(f"\n{rword[0]}. (type \"quit\" to quit) (first or second or third or fourth)")
        
        k = input("")
        
        if k == "quit":
            print("")
            break
        
        if set(list(word)) - set([i.strip().lower() for i in k.split(",")]) != set(word):
            print("Correct")
            score["correct"] += 1
        else:
            print("Incorrect. " + str(word))
            score["incorrect"] += 1
        
    print(f"Correct: {score.get('correct')}")
    print(f"Incorrect: {score.get('incorrect')}")


def composition(VERBS) -> None:
    
    score = {
        "correct": 0,
        "incorrect": 0
    }
    
    while True:
        
        word = random.choice(VERBS)
        rword = word.get_random_form()
        
        print(f"\n{rword[0]}. (type \"quit\" to quit) (person, number, tense, voice)")
        
        k = input("")
        
        if k == "quit":
            print("")
            break
        
        if [i.strip().lower() for i in k.split(",")] == rword[1]:
            print("Correct")
            score["correct"] += 1
        else:
            print("Incorrect. " + ", ".join(rword[1]))
            score["incorrect"] += 1
        
    print(f"Correct: {score.get('correct')}")
    print(f"Incorrect: {score.get('incorrect')}")


def conjugated_verb(VERBS) -> None:
    
    score = {
        "correct": 0,
        "incorrect": 0
    }
    
    while True:
        
        word = random.choice(VERBS)
        rword = word.get_random_form()
        
        print(f"\n{str(word)[17:]}")
        print(f"{', '.join(rword[1])}. (type \"quit\" to quit) (word)")
        
        k = input("")
        
        if k == "quit":
            print("")
            break
        
        if k.strip().lower() == rword[0]:
            print("Correct")
            score["correct"] += 1
        else:
            print("Incorrect. " + rword[0])
            score["incorrect"] += 1
        
    print(f"Correct: {score.get('correct')}")
    print(f"Incorrect: {score.get('incorrect')}")


def conjugation(VERBS) -> None:
    
    score = {
        "correct": 0,
        "incorrect": 0
    }
    
    while True:
        
        word = random.choice(VERBS)

        print(f"\n{str(word)[17:]}. (type \"quit\" to quit) (conjugation)")
        
        k = input("")
        
        if k == "quit":
            print("")
            break
        
        if k.strip().lower() == str(word.conj):
            print("Correct")
            score["correct"] += 1
        else:
            print("Incorrect. " + str(word.conj))
            score["incorrect"] += 1
        
    print(f"Correct: {score.get('correct')}")
    print(f"Incorrect: {score.get('incorrect')}")