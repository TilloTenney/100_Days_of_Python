# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

first = t+r+u+e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

second = l+o+v+e

score = str(first)+str(second)

if int(score) < 10 or int(score) >90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) <50:
    print(f"Your score is {score}, you are alright together.")
else:
   print(f"Your score is {score}.") 
