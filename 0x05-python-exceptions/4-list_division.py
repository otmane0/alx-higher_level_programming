def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            #Attempt to perform the division
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            #Handle division by zero
            print("division by 0")
            value = 0
        except (TypeError, ValueError):
            #Handle wrong type
            print("wrong type")
            value = 0
        except IndexError:
            #Handle out of range
            print("out of range")
            value = 0
        finally:
            #Append the result to the new list
            result.append(value)

    return result