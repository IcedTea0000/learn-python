# counter module
from collections import Counter


def counter_test(input):
    return Counter(input)


# print(counter_test([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
# print(counter_test('asaaasdfasdfasv'))
# print(
#     counter_test('this is a sentence for a testing purpose that i am not sure what i am writing about'.lower().split()))
#
# print(Counter('asfdassdvbxczvzvasfafadf').most_common(5))

# defaultdict module
from collections import defaultdict

d = {'a': 1}
d = defaultdict(lambda: 0)
# print(d['wrong_key'])
# print(d['a'])

# namedtuple module
from collections import namedtuple

Customer = namedtuple('Customer', ['name', 'age', 'address'])
martin = Customer(name='Martin', age=27, address='Here')
# print(type(martin))
# print(martin)
# print('\n')

import os

# print(os.getcwd())
# print(os.listdir())

import shutil

# file_path = 'C:\\workspace\\learn-python'
# for folder, sub_folders, files in os.walk(file_path):
#     print('folder: {}'.format(folder))
#     print('sub_folders: {}'.format(sub_folders))
#     print('files: {}'.format(files))
#     print('\n')


import datetime

# mytime = datetime.time(13, 20, 1, 20)
# print(mytime)
# print('{}.{}.{}.{}'.format(mytime.hour, mytime.minute, mytime.second, mytime.microsecond))

# today = datetime.date.today()
# print(today)
# print(today.ctime())

# from datetime import date
# date1 = date(2021, 2, 3)
# date2 = date(2020, 11, 3)
# print(date1 - date2)

# import datetime
datetime1 = datetime(2020,11,2,15,23)
datetime2 = datetime(2019,3,15,7,1)
print(datetime1-datetime2)

