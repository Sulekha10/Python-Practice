# python program to check whether email is valid or not using string functions

email = input("Enter you Email : ")
k,j,d = 0,0,0
if len(email) >= 6:  #1
    if email[0].isalpha(): #2
        if("@" in email) and (email.count("@") == 1):#3
            if(email[-4]==".") ^ (email[-3] == "."):#4
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): #5
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else: #5
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("Right email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")
        