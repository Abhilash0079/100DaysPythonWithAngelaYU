'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

'''
#### Instruction ########
'''
1. Go to the above link.
2. There you can try the code for different robot.
3. The below code will work only for Hurdle1, Hurdle2 and Hurdle3.
4. turn_left(), wall_on_right(), front_is_clear(), at_goal()  ----------- these are the built-in functions on this paltform. There are many others function are on this platform.
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()