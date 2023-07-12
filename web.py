import streamlit as st
import functions
import base64
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w")as file:
        pass

st.set_page_config(layout="wide", page_icon="random", page_title="plikka work")
todos = functions.readfile()
#completed = functions.readfile(txt="completed.txt")

def add_todo():
    todo = st.session_state["new_todo"]
    duplicate = [item.strip("\n") for item in todos]
    
    if todo not in duplicate:
        todos.append(todo + "\n")
        functions.writefile(todos)
        
    else:
        st.sidebar.warning(f'"{todo}" is already in the list')
    st.session_state["new_todo"]= ""


#def edit():
    

st.sidebar.title("To-Do")
st.sidebar.write(f"you have {len(todos)} tasks to finish")

for index, todo in enumerate(todos):
    checkbox = st.sidebar.checkbox(todo, key=todo)
    if checkbox:
        #completed.append(todo)
        #functions.writefile(completed, txt ="completed.txt")
        todos.pop(index)
        functions.writefile(todos)
        del st.session_state[todo]
        st.experimental_rerun()

def pdf_view(uploaded):
    if uploaded is not None:
        file_data = uploaded.read()
        base64_pdf = base64.b64encode(file_data).decode('utf-8')
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

        st.markdown(pdf_display, unsafe_allow_html=True)


st.sidebar.text_input(label="", placeholder="Add a new todo...", key="new_todo",on_change=add_todo)

st.title("Plikka")
st.write("Anything particular on your mind?")
with st.sidebar:
    st.text_area("your notes", height= 300 )

uploaded = st.file_uploader("Upload your pdf", type="pdf")

pdf_view(uploaded)