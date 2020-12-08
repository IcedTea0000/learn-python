import sys


def rotation(text, number_to_rotate):
    converted_list = []
    output_text = ''
    for character in text:
        converted_list.append(ord(character) - number_to_rotate)
    for number in converted_list:
        output_text += chr(number)
    return output_text


def check_word_longer_than(path, word_length):
    with open(path, mode='r') as text_file:
        for line in text_file:
            if len(line) > word_length:
                print('text : {} | size : {} bytes'.format(line,sys.getsizeof(line)))


if __name__ == '__main__':
    # print(rotation('abc', 1))
    path = 'C:\\workspace\\learn-python\\Practices\\text.txt'
    check_word_longer_than(path, 20)
