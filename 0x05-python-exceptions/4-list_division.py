#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            division_result = 0
            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                if divisor != 0:
                    division_result = dividend / divisor
                else:
                    print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(division_result)
    return result
