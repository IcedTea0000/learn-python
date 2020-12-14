def make_histogram(s):
    """

    :param s: text
    :return: dictionary of histogram letter : appearance
    """
    historgram = {}
    for letter in s:
        historgram[letter] = historgram.get(letter, 0) + 1
    return historgram



if __name__ == '__main__':
    pass