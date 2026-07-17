# FUNCTIONS WITH OUTPUT;-

def format_name(f_name,l_name):

    if f_name=="" and l_name=="":
        return "Invalid O/P"

    f_name = f_name[0].upper() + f_name[1:]
    l_name = l_name[0].upper() + l_name[1:]

    # --------OR---------
    # return f_name.title() + l_name.title()

    return f_name + " " + l_name



fi_name=input("Enter first name: ")
la_name=input("Enter last name: ")

print(format_name(fi_name,la_name))



# DOCSTRINGS:-

""" This is called a Doctrings
    and it is multiline"""