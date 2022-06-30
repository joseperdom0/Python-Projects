this_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(this_list):
    del this_list[3]
    this_list[3] = 'ram'


print(my_list(this_list))
print(this_list)