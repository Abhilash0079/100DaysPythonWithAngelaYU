'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

'''
#### Instruction ########
'''
1. Go to the above link.
2. There you can try the code for different robot.
3. Already added 3 different problem in which robot will end in infinite loop.
3. The below code will work only for all three problems in the Resources folder.
4. turn_left(), wall_on_right(), front_is_clear(), at_goal()  ----------- these are the built-in functions on this paltform. There are many others function are on this platform.
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()