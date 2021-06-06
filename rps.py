from tkinter import *
import random

root = Tk()
root.geometry("600x500")
root.title("Rock Paper Scissors Game")

user_score = 0
comp_score = 0
user_choice = ''
comp_choice = ''


def choice_to_num(choice):
    rps = {'rock': 0, 'paper': 1, 'scissors': 2}
    return rps[choice]


def random_comp_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def result(user_choice, comp_choice):
    global user_score
    global comp_score
    user = choice_to_num(user_choice)
    comp = choice_to_num(comp_choice)
    if user == comp:
        print("Tie")
    elif((user-comp)%3==1):
        print("You Won!")
        user_score+=1
    else:
        print("Computer Won")
        comp_score+=1
    text_area = Text(master=root, height=12, width=30, bg="#FFFF99")
    text_area.grid(column=0, row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(
        uc=user_choice, cc=comp_choice, u=user_score, c=comp_score)
    text_area.insert(END, answer)

def rock():
    global user_choice
    global comp_choice
    user_choice = 'rock'
    comp_choice = random_comp_choice()
    result(user_choice, comp_choice)
def paper():
    global user_choice
    global comp_choice
    user_choice = 'paper'
    comp_choice = random_comp_choice()
    result(user_choice, comp_choice)
def scissors():
    global user_choice
    global comp_choice
    user_choice = 'scissors'
    comp_choice = random_comp_choice()
    result(user_choice, comp_choice)


button1 = Button(root, text="       Rock       ", bg="skyblue", command=rock)
button1.grid(column=0, row=1)
button2 = Button(root, text="       Paper      ", bg="pink", command=paper)
button2.grid(column=0, row=2)
button3 = Button(root, text="      Scissor     ", bg="lightgreen", command=scissors)
button3.grid(column=0, row=3)

root.mainloop()

