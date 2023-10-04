my_list = ['one', 'two', 'three']

# Простой ассерт с выводом текста ошибки
assert 'five' in my_list, 'There are only three numbers in the list'

# Ассерт с обработкой ошибки, описанием что делает в случае AssertionError
try:
    assert 'two' in my_list
    print('Good')
except AssertionError:
    print('Please choose a number in range (1-3)')
