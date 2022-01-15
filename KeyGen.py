from threading import Timer
import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Extras = ['!', '"', '£', '$', '%', '^', '&', '*', '*', '#', '~']
def print_values():
    value = random.choice(Letters)
    print(value)
    
def print_numbers():
    numbPRINT = random.choice(Numbs)
    print(numbPRINT)
def print_extras():
    Extra = random.choice(Extras)
    print(Extra)

def print_names():
    print("Attempting to print Keys")
prnt_nam = Timer(1, print_names)
prnt_nam.start()

def print_all():
    for x in range(30):
        print_values(), print_numbers(), print_extras()
    print(".exe")
prnt_all = Timer(3, print_all)
prnt_all.start()

def prompt():
    print("Do you wish to exit?")
    AnsPromt = input()
    if AnsPromt == "Yes":
        exit()
    elif AnsPromt == "No":
            print("Do you want to print another key?")
            AnsPrompMore = input()
            if AnsPrompMore == "Yes":
                print_all()
            elif AnsPrompMore == "No":
                exit()
prnt_prompt = Timer(5, prompt)
prnt_prompt.start()
