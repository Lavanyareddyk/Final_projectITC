food = ["burger","Drink","Fries","Apple pie"]
prices =[10,18,50,60]

myorderFood=[]
myorderCost=[]
counter=0
total=0

print ("welcome to mcgodbolds")



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



