# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("I am Greet function")
    print("Bye")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"I am in greet_with_name function {name}")
    print(f"Bye {name}")

greet_with_name("Angela")

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Angela", "London")  ### Positional Argument (Default way)
# Function with keyword arguments
greet_with(location = "London", name = "Angela")
