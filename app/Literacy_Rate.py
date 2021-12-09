import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Literacy Rate")

people = st.sidebar.selectbox("Select the Age Group!",("Youth (15-24)", "Adult (Above 15)"))

def data(people):
    if people == "Youth (15-24)":
        youth_data = pd.read_csv("https://github.com/sakshisingh12/Literacy-Rate/blob/main/app/youth_data.csv")
        st.write("""
            ## Youth 
            ### Age Group 15-24 Years
        """
        )
        st.dataframe(youth_data, width=1200, height=500)

        male_literacy = px.scatter(youth_data,
                x='Country',
                y='Male',
                hover_name='Male',
                title=f'Countries vs Literacy Rate of Male')

        female_literacy = px.scatter(youth_data,
                x='Country',
                y='Female ',
                hover_name='Female ',
                title=f'Countries vs Literacy Rate of Female')

        st.markdown("""
          ## Literacy Rate of Males
        """)
        st.plotly_chart(male_literacy)

        st.markdown("""
          ## Literacy Rate of Females
        """)
        st.plotly_chart(female_literacy)


    elif people == "Adult (Above 15)":
        adult_data = pd.read_csv("https://github.com/sakshisingh12/Literacy-Rate/blob/main/app/adults_data.csv", encoding='latin-1')
        st.write("""
            ## Adults
            ### Age Group Above 15 Years
        """
        )

        st.dataframe(adult_data, width=1200, height=500)

        male_literacy = px.scatter(adult_data,
                x='Country',
                y='Male',
                hover_name='Male',
                title=f'Countries vs Literacy Rate of Male')

        female_literacy = px.scatter(adult_data,
                x='Country',
                y='Female ',
                hover_name='Female ',
                title=f'Countries vs Literacy Rate of Female')

        st.markdown("""
          ## Literacy Rate of Males
        """)
        st.plotly_chart(male_literacy)

        st.markdown("""
          ## Literacy Rate of Females
        """)
        st.plotly_chart(female_literacy)

data(people)
    
