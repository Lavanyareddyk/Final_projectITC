import re
def validation(email,passwd):
    x=email+passwd
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    pat = re.compile(reg)
    mat = re.search(pat, passwd)
    if(re.fullmatch(regex, email) and mat):
        file = open('project_','a')
        file.writelines(["\n"+x])
        file.close()
        print("valid email-id and password")
    else:
        print("please enter email id and password in correct format")
#################################################################################################################################
print("Enter 0 for Registration ")
print("Enter 1 for Login")
print("Enter 2 for Forgotpassword")
process=int(input("Enter your process "))
if process == 0:
    print("email id should be unique")
    print("please enter email id in this format")
    print("YOURNAME@ORGNAME.com")
    print("please enter password in the given format")
    print("Password should contain atlest one number, one uppercase letter,one lowercase letter,one special charater")
    print("length of your password should greater than 5 and lesser than 16")
    email=input("enter your email-id -> ")
    passwd=input("enter your password -> ")
    validation(email,passwd)
elif process == 1:
    print("please enter your email id and password")
    Email=input("enter your email id -> ")
    Password=input("enter your pasword -> ")
    file = open('project_','r')
    for i in file:
        if i in Email+Password :
            print("sucessfully logined")
            break
elif process == 2:
    print("forgot password")
    Email=input("enter your email id -> ")
    file = open('project_','r')
    for i in file:
        if Email in i:
            c=len(Email)
            print(i[c:])
            print("your password")
            break