# Here, we have an example of modifying a global scope. 

enemies = 1 

def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)
increase_enemies()

# The variable enemies = 1, declared outside the function increase_enemies() is assigned a value of 1, and the value is increased by 1 inside the increase_enemies() function. 
# Thus, in order to use a global variable, inside of a function, we need to define it explicitly using the global statement. 