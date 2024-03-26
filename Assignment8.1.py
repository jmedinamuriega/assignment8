# 1.
farenheit=[]
while True:
    try:    
        temperatures=int(input("Please put the temperatures that you want :D: "))
        farenheit.append(temperatures)
        print(farenheit)
        leave=input("Do you want to add more temperatures? y/n: ")
        if leave=="n":
            break        
    except ValueError:
        print("Please put numbers :D")
        
print("Here is the list of temperatures in farenheit!: ") 
for i in farenheit:
    print(f"{i}f")       
        
greetings="Thanks for ussing the wheather application"
celsius_list=[]
def far_cel(celsius_list):
    try:
        celsius_list=[]
        for temps in farenheit:
            celsius=(temps-32)*5/9
            celsius_list.append(celsius)   
    except ZeroDivisionError:
        print("I can't divide by zero")  
    except OverflowError:
        print("Too much numbers")
    else:
        print(f"here is a complete list of the temperatures in celsius {["%.1f" % elem for elem in celsius_list]}")
    finally:
        print(greetings)
        



far_cel(celsius_list)

# Task 1: 
try:
    servings=int(input("How much dishes you want to prepare? "))
    original_servings=int(input("And for how many was the original recipe? "))
    adjusment=servings/original_servings
    if servings=="0":
        raise ValueError("You can't have 0 dishes")
    else:
        print(f"Here is the ammount of ingredients that you are going to need!: {["%.1f"%adjusment]}")
except ValueError:
    print("Please put just numbers! :D")
except ZeroDivisionError:
    print("I think that you can't have 0 dishes")
finally:
    print("I hope that you never stop of cooking, your dishes are going to be the greatest!")



