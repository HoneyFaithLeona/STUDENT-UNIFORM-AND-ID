print("HELLO STUDENTS!")
print("What shift are you?")
print("A. Shift A")
print("B. Shift B")
print("C. Shift C")
a=input("Shift ")
if a=="A":
    print("""
    What day is today?
    A. Monday
    B. Tuesday
    C. Wednesday
    D. Thursday
    E. Friday
    F. Saturday
    G. Sunday""")
    b=input("=")
    if b=="A" or  b=="B":
        print("DID YOU WEAR YOUR SCHOOL UNIFORM AND ID? Type 1 if YES and Type 2 if NO.")
        c=int(input("="))
        if c==1:
            print("You may now enter the school campus.")
        else:
            print("You ARE NOT ALLOWED to enter the school campus.")
    elif b=="C":
        print("DID YOU WEAR YOUR WASHING DAY OUTFIT AND ID? Type 1 if YES and Type 2 if NO.") 
        c=int(input("="))
        if c==1:
            print("You may now enter the school campus.")
        else:
            print("You ARE NOT ALLOWED to enter the school campus.")
    else:
        print("You are not allowed to enter the school.")
            
elif a=="B":
    print("""
What day is today?
A. Monday
B. Tuesday
C. Wednesday
D. Thursday
E. Friday
F. Saturday
G. Sunday
""")
    b=input("=")
    if b=="D" or b=="E"or b=="F":
        print("DID YOU WEAR YOUR SCHOOL UNIFORM AND ID? ")
        print("Type 1 if YES and Type 2 if NO")
        c=int(input("="))
        if c==1:
            print("You may now enter the School Campus.")
        else:
           print("You ARE NOT ALLOWED to enter the School Campus.")
    else:
        print("You are not allowed to enter the School")
            
elif a=="C":
    print("""
    What day is today?
    A. Monday
    B. Tuesday
    C. Wednesday
    D. Thursday
    E. Friday
    F. Saturday
    G. Sunday""")
    b=input("=")
    if b=="G":
        print("DID YOU WEAR YOUR WASHING DAY OUTFIT AND ID? Type 1 if YES and Type 2 if NO.") 
        c=int(input("="))
        if c==1:
            print("You may now enter the school campus.")
        else:
            print("You ARE NOT ALLOWED to enter the school campus.")
    elif b=="A" or  b=="B":
        print("DID YOU WEAR YOUR SCHOOL UNIFORM AND ID? Type 1 if YES and Type 2 if NO.")
        c=int(input("="))
        if c==1:
            print("You may now enter the school campus.")
        else:
            print("You ARE NOT ALLOWED to enter the school campus.")
    else:
        print("You are not allowed to enter the School.")
else:
    print("Not Valid.")

  
    
                
            
            
            
        
    