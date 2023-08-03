import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("THEME GENERATOR")

    # Empty box (placeholder)
    input_text = st.text_area("Enter text here", value="")

    # Run button
    if st.button("Run"):
        # Perform some action here when the button is clicked

        labels = ['teamless', 'impact-driven', 'productivity', 'misscommunication','cross level marketing']
        sizes = [13.9,20.8,16.7,26.4,22.2]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

        
if _name_ == "_main_":
    main()
