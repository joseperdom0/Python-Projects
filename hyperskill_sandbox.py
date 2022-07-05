def do_the_mess(parameter):
    global variable
    variable += parameter[0]
    return variable


the_list = [x for x in range(2,3)]
print(the_list)
variable = 0
do_the_mess(the_list)
print(variable)