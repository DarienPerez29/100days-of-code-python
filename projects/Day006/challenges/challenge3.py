# This code must be executed at:
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    for i in range(3): turn_left()
    
def jump_hurdle():
    turn_left()
    while not right_is_clear(): move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front(): move()
    turn_left()

while not at_goal():
    if wall_in_front(): jump_hurdle()
    else: move()