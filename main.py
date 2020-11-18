# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
newWeight = float(weight) #change string to float
newHeight = float(height)
#BMI formula
BMI = newWeight/(newHeight**2)
print("Your BMI is :" + str(BMI) + ". The more you know...")









