import string
import zxcvbn

password="Adhinsbaksb12@"

#The longer the Password, Stronger it is!!!

upper_case=any([1 if i in string.ascii_uppercase else 0 for i in password ])
lower_case=any([1 if i in string.ascii_lowercase else 0 for i in password ])
special_char=any([1 if i in string.punctuation else 0 for i in password])
numeric=any([1 if i in string.digits else 0 for i in password])

characters=[upper_case,lower_case,special_char,numeric]

with open("common.txt","r") as s:
     common=s.read().splitlines()
if password in common:
    print("the password found in common list so change password ")
    exit()
    
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

