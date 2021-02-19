#A program to validate password
password = input("\nEnter password containing atleast one digit, one special character, one uppercase, and one lowercase letter with length between 8 and 16 characters:")

count_up =0
count_low =0
count_num =0
count_spec =0

special_chars = ['!', '@','#','$','%','^','&', 
                '*','(',')','-','_','.'] 
                
if (len(password)>7 and len(password)<17):  
    for i in password:
        if i == ' ':
            print("Password should not contain white spaces.")
            break
        
        elif i.isupper(): #checking atleast one uppercase
            count_up = 1
       
        elif i.islower(): #checking atleast one lowercase
            count_low = 1
        
        elif i.isdigit(): #checking atleast one digit
            count_num = 1
  
        elif i in special_chars: 
            count_spec = 1
        
else:
    print("Password length should be between 8 to 16 characters.")
    
if (count_up==1 and count_low==1 and count_num ==1 and count_spec==1):
    print("Password validated.")
    
else:
    print("Invalid password.")
