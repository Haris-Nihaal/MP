import streamlit as st

def main():
    st.title("Text Input with Two Run Buttons")

    # Text input box
    input_text = st.text_area("Enter text here")

    # Run buttons
    col1, col2 = st.columns(2)
    if col1.button("Run on Left"):
        run_analysis(input_text)

    if col2.button("Run on Right"):
        run_analysis(input_text)

def run_analysis(text):
    # Add your analysis code here
    # For example, you can print the input text
    st.write("Analysis for input text:")
    st.write(text)

if __name__ == "__main__":
    main()
