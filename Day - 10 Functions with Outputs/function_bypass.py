# Here, we can see a function with a return statement, that suggests the program that it is the end of the function and terminates 
# the function after it encounters the return statement. 

def name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}."

print(name(input("What is your first name ?\n"), input("What is your last name ?\n")))
