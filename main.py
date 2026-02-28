import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

menu = st.sidebar.selectbox("Menu", ["Home", "About"])

if "expression" not in st.session_state:
    st.session_state.expression = ""

def press(key):
    st.session_state.expression += str(key)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

if menu == "Home":
    st.title("Calculator with Buttons")

    st.text_input("Display", st.session_state.expression, disabled=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button("7", on_click=press, args=("7",))
        st.button("4", on_click=press, args=("4",))
        st.button("1", on_click=press, args=("1",))
        st.button("0", on_click=press, args=("0",))

    with col2:
        st.button("8", on_click=press, args=("8",))
        st.button("5", on_click=press, args=("5",))
        st.button("2", on_click=press, args=("2",))
        st.button(".", on_click=press, args=(".",))

    with col3:
        st.button("9", on_click=press, args=("9",))
        st.button("6", on_click=press, args=("6",))
        st.button("3", on_click=press, args=("3",))
        st.button("=", on_click=calculate)

    with col4:
        st.button("+", on_click=press, args=("+",))
        st.button("-", on_click=press, args=("-",))
        st.button("*", on_click=press, args=("*",))
        st.button("/", on_click=press, args=("/",))

    st.button("C", on_click=clear)

elif menu == "About":
    st.title("About")
    st.write("""
    This is a button-based calculator built using Streamlit.

    Features:
    - Button input
    - Basic arithmetic operations
    - Sidebar navigation (Home & About)

    Created using Python and Streamlit.
    """)