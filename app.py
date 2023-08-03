import streamlit as st

def square_number(number):
    return number ** 2

def main():
    st.title("Simple Square Number App")
    st.write("Enter a number below and click on the button to calculate its square.")

    # Input box for the user to enter the number
    user_input = st.number_input(label="Enter a number", step=1)

    if st.button("Calculate"):
        result = square_number(user_input)
        st.write(f"The square of {user_input} is {result}.")

if __name__ == "__main__":
    main()
