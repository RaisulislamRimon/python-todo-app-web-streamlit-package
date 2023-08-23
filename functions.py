# def get_todos(filepath):
# def get_todos(filepath):   # TypeError: get_todos() missing 1 required positional argument: 'filepath'

# constant variable
FILEPATH = 'todos.txt'


# def get_todos(filepath='todos.txt'):
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items. """
    # filepath = 'todos.txt'
    # with open('todos.txt', 'r') as file_local:
    with open(filepath, 'r') as file_local:
        # return filepath
        todos_local = file_local.readlines()
    return todos_local


# document the code #doc-strings
# print(help(get_todos))
# this is the result
# Help on function get_todos in module __main__:
#
# get_todos(filepath='todos.txt')
#     Read a text file and return the list of
#     to-do items.
#
# None


# def write_todos(filepath, todos_arg):
# def write_todos(filepath='todos.txt', todos_arg):
# def write_todos(todos_arg, filepath='todos.txt'):
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(help(write_todos))

# text = """
# lorem ipsum     \
# generated text  \
# hello world     \
# """

# text = """
# lorem ipsum     \n\
# generated text \
# hello world \
# """

text = """
lorem ipsum
generated text
hello world
"""

# print(text)


# print(__name__)

if __name__ == '__main__':
    print("Hello __main__")
    print(get_todos())
else:
    print('__name__', __name__)
