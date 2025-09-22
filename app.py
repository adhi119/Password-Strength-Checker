import tkinter as tk
import string

def check_password_strength():
    password=password_entry.get()

#The longer the Password, Stronger it is!!!

    upper_case=any([1 if i in string.ascii_uppercase else 0 for i in password ])
    lower_case=any([1 if i in string.ascii_lowercase else 0 for i in password ])
    special_char=any([1 if i in string.punctuation else 0 for i in password])
    numeric=any([1 if i in string.digits else 0 for i in password])

    characters=[upper_case,lower_case,special_char,numeric]

    # with open("common.txt","r") as s:
    #     common=s.read().splitlines()
    # if password in common:
    #     print("the password found in common list so change password ")
    #     exit()
        
    length=len(password)

    score=0
    print(f"the length og the string is :{str(length)}")
    #defining the number of charactrers in the password
    if sum(characters)>1:
        score+=1
    if sum(characters)>2:  
        score+=1
    if sum(characters)>3:
        score+=1
    if sum(characters)==4:
        score+=1
    print(f"password having the {str(sum(characters))} different type of chsracters & adding {str(score)} points")

    #definig the strength and score of the password
    if length<=6:
        score+=1
        print(f"your password is weak! & score is:{str(score)}/5")
    elif length>10 :
        score+=1
        print(f"your password is Average & score is:{str(score)}/5 ")
    elif length>13:
        score+=1
        print(f"your password is good & score is:{str(score)}/5")
    elif length>=20: #or length>20:
        score+=1
        print(f"your password is Excellent! & score is:{str(score)}/5")

     
    if score <= 2:
        strength_label.config(text="Strength: Weak", bg="orange", fg="black")
    elif score == 3:
        strength_label.config(text="Strength: Fair", bg="yellow", fg="black")
    elif score == 4:
        strength_label.config(text="Strength: Good", bg="lightgreen", fg="black")
    else:  # score == 5
        strength_label.config(text="Strength: Excellent", bg="darkgreen", fg="white") 


#create main window
root=tk.Tk()
root.title("password strength checker")
root.geometry("400x300")

password_label=tk.Label(root, text="Enter the Password:")
password_label.pack(pady=10)

password_entry=tk.Entry(root,show='*')
password_entry.pack(pady=5)

strength_label=tk.Label(root, text="strength:", font=("Airal",12))
strength_label.pack(pady=10)
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

root.mainloop()