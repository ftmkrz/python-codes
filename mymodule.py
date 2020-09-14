def my_func():
    print("Hey I am in mymodule.py")
# my_func()
test = 'Test String'
def find_index(to_search, target):
    '''Find the index of a value in a sequence
    args:
        to_search:list of integers...
        target:string, integer
    '''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
if __name__ == '__main__':
    print('Imported my_module...')
    my_func()