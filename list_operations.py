def multiply_list_element(numbers_list):
    """"
    @args:list()
    @disc:multiply the list element and returns the output
    @return: number
    """
    if type(numbers_list) == list:
        print("valid Data : ", type(numbers_list))
        num = 1
        for element in numbers_list:
            num = num * element
        return num
    else:
        print("It's not a valid Data type: ", type(numbers_list))
        return None


def square_list_elements(number_list):
    """"
    @args:list()
    @disc:square root the list elements
    @return:list()
    """
    if type(number_list) == list:
        print("valid data:", type(number_list))
        res = []
        for elements in number_list:
            res.append(elements ** 2)
        return res
    else:
        print("It's not a valid Data type:", type(number_list))
        return None
