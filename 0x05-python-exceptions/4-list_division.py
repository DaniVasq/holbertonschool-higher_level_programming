#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("{:s}".format("division by 0"))
            value = 0
        except TypeError:
            print("{:s}".format("wrong type"))
            value = 0
        except IndexError:
            print("{:d}".format("out of range"))
            value = 0
        finally:
            newList.append(value)
    return newList
