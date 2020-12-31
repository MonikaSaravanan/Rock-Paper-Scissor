import random
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.title("ROCK PAPER SCISSOR")

user_score=0
comp_score=0
user_choice=""
comp_choice=""

def choice_to_number(choice):
 rps={"rock":0 , "paper":1 , "scissor":2}
 return rps[choice]

def number_to_choice(number):
 rps={0:"rock",1:"paper",2:"scissor"}
 return rps[number]

def random_computer_choice():
 return random.choice(["rock","paper","scissor"])

def result(human_choice,comp_choice):
 global user_score
 global comp_score
 user = choice_to_number(human_choice)
 comp = choice_to_number(comp_choice)
 if(user == comp):
    print("tie")
 elif((user-comp)%3==1):
    print("You won")
    user_score += 1
 else:
    print("Computer Won")
    comp_score += 1
 text_area=tk.Text(master=window,width=30,height=33,bg="white")
 text_area.grid(row=6,column=4)
 answer="Your choice:{uc} \nComputer choice:{cc} \nyour Score:{u} \ncomp Score:{c}".format(uc=user_choice,cc=comp_choice,u=user_score,c=comp_score)
 text_area.insert(tk.END,answer)

def rock():
 global user_choice
 global comp_choice
 user_choice="rock"
 comp_choice=random_computer_choice()
 result(user_choice,comp_choice)

def paper():
 global user_choice
 global comp_choice
 user_choice="paper"
 comp_choice=random_computer_choice()
 result(user_choice,comp_choice)

def scissor():
 global user_choice
 global comp_choice
 user_choice="scissor"
 comp_choice=random_computer_choice()
 result(user_choice,comp_choice)

btn1 = tk.Button(text="ROCK",width=8,height=2,bg="hotpink",command=rock)
btn1.grid(row=1,column=4,padx=3,pady=3)
btn2 = tk.Button(text="PAPER",width=8,height=2,bg="hotpink",command=paper)
btn2.grid(row=2,column=4,padx=3,pady=3)
btn3 = tk.Button(text="SCISSOR",width=8,height=2,bg="hotpink",command=scissor)
btn3.grid(row=3,column=4,padx=3,pady=3)

window.mainloop()
