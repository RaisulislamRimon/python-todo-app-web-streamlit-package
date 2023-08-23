import streamlit as st
# import streamlit as st
import functions
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

# function call for get_todos
todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)
    # print(todo)


st.title('My Todo Web App')
st.subheader('This is my todo web app')
st.write('This app is to increase your productivity')
st.checkbox('Buy grocery')
st.checkbox('Throw the trash')
# take input from the user
st.text_input(label='Enter a todo: ', placeholder='Add new todo...', on_change=add_todo, key='new_todo')
st.write('If any task is complete, put a tik mark to delete that task.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# st.text_input('')
# st.text_input(label='')
# st.text_input(label='Enter a todo: ')
# st.text_input(label='Enter a todo: ', placeholder='Add new todo...', on_change=add_todo, key='new_todo')

# print('hello')
# st.session_state
