def frequency_dict(input_list=[]):
    """

    :param input_list: any list
    :return: dictionary with K=list member, V = number of appear
    """
    result_dict = dict()
    for member in input_list:
        if member not in result_dict:
            result_dict.update({member: 1})
        else:
            result_dict[member] += 1
    return result_dict


def inverse_frequency_dict(input_dict={}):
    """

    :param input_dict: frequency dictionary
    :return: dictionary with K=number of appearance, V = list of member
    """
    result_dict = dict()
    appearance_set = set(input_dict.values())
    for appearance in appearance_set:
        result_dict.update({appearance: []})
        for member in input_dict:
            if input_dict[member] == appearance:
                result_dict[appearance].append(member)
    return result_dict


if __name__ == '__main__':
    test_list = ['a', 'b', 'c', 'a', 'b']
    print(inverse_frequency_dict(frequency_dict(test_list)))
