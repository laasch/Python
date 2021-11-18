# Collect user input
try:
    age = int(input("What's your age: "))
except:
    print("I couldn't understand your age.")
    exit()
    
print ("In 50 years, you will be",age+50)