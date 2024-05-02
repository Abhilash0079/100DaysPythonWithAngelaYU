import random
import mymodule

random_integer = random.randint(1,10)
print(random_integer)
ran_float = random.random()  ####----gives value b/w 0.0000 ----- 0.9999.....
print(ran_float)

ran_between_float = random.random() * 5
print(ran_between_float)

print(mymodule.pi)

###############  List  ##################
states_of_india = ["Maharashtra","Gujrat","Karnataka","Tamil Nadu","Kerala","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Haryana","Himachal"]
print(states_of_india[0])
print(states_of_india[-1])
states_of_india[0] = "Maharashtra"
print(states_of_india)
states_of_india.append("Rajasthan")
print(states_of_india)
states_of_india.extend(["West Bengal","Jharkhand","Bihar","Uttar Pradesh","Madhya Pradesh"])


############# Nested List ##############
fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches", "Cherries", "Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)