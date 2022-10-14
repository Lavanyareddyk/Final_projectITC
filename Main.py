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


food = ["burger","Drink","Fries","Apple pie"]
prices =[10,18,50,60]

myorderFood=[]
myorderCost=[]
counter=0
total=0

print ("welcome to Fooditems")



order = input(" can i take your order ?")

Foodorder = input("please enter item")
if Foodorder =="Burger":
   myorderFood.append(food[0])
   myorderCost.append(prices[0])
   counter=counter+1
   total=total+(prices[0])
elif Foodorder=="Drink":
   myorderFood.append(food[1])
   myorderCost.append(prices[1])
   counter=counter+1
   total=total+(prices[1])
elif Foodorder=="Fries":
   myorderFood.append(food[2])
   myorderCost.append(prices[2])
   counter=counter+1
   total=total+(prices[2])
elif Foodorder=="Apple pie":
   myorderFood.append(food[3])
   myorderCost.append(prices[3])
   counter=counter+1
   total=total+(prices[3])
else:
   print("Not on menu")
finished = input("Have you finished ordering Y/N")
if finished =="N":
   nextorder = True
else:
   nextorder = False
   print(myorderFood)
   print(myorderCost)
   print(counter)


   class Customer_Details:
    attr1=int(input("enter customer id:"))
    attr2=input("lavanya")
    attr3=input("Ap")
    attr4=input("254678854")
    def get_details(self):
        print("C_id",self.attr1)
        print("customer_name:",self.attr2)
        print("customerer_address:",self.attr3)
        print("customer_contact:",self.attr4)

class Payment_details:
    P_id = int(input("enter payment id:"))
    Amount ="200"
    Acc_no =int(input("enter acc_no"))
    p_status =input("payment_success")
    def getpayment_details(self):
        print("p_id:",self.p_id)
        print("Amount is:",self.Amount)
        print("Account num is:",self.Acc_no)
        print("payment status is:",self.P_status)


class Delivery_details:
    c_id =int(input("enter customer_id:"))
    c_Name =input("ghdfekge")
    Delivery_address =input("Ap , chittoor")
    delivery_item = input("item received")
    def getDelivery_details(self):
        print("Contact_id:",self.c_id)
        print("Contact_Name:",self.C_Name)
        print("self.delivery_address")
        print("delivery item is:",self.delivery_item)
        


file = open("Food.txt","r")
print(file.read())


