

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    my_list.clear()
    for n in new_list:
            my_list.append(n)

    return my_list



