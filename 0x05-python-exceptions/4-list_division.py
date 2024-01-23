#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output = []

    for i in range(list_length):
        try:
            array = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            array = 0
        except (TypeError, ValueError):
            print("wrong type")
            array = 0
        except IndexError:
            print("out of range")
            array = 0
        finally:
            output.append(array)

    return output