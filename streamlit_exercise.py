from random import choices
from nbformat import write
import plotly.io as pio
pio.renderers.default = "vscode"

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as py
from plotly.figure_factory import create_table

#Importing streamlit
import streamlit as st
import pandas as pd

st.image("https://i0.wp.com/gbsn.org/wp-content/uploads/2020/07/AUB-logo.png?ssl=1")

st.title("MSBA 325 Assignment #2")
st.header("My First Web Application using Streamlit")
st.markdown("""
Done by: Wassim Radwan
""")

#First Dataset
#Attributes
attribute = st.sidebar.radio('Which Attribute Would You Like To Select?',
                 ('Covid-19 Dataset','Covid_Grouped Dataset','Covid-19 in the United States'))

if attribute == 'Covid-19 Dataset':  
    st.balloons()           
    with st.expander("Click for more information on the dataset:"): 
        st.write("This dataset contains Country/Region, Continent,  Population, TotalCases, NewCases, TotalDeaths, NewDeaths,  TotalRecovered, NewRecovered, ActiveCases, Serious, Critical, Tot Cases/1M pop, Deaths/1M pop, TotalTests, Tests/1M pop, WHO Region, iso_alpha.")
        
# Importing Dataset1
    dataset1 = pd.read_csv("covid.csv") 
    if st.button('To see a small sample of the dataset'):
        st.subheader("A Glimpse of the Dataset")
        st.write(dataset1.head(10))

# Returns tuple of shape (Rows, columns)
    shape = st.checkbox("Click to see the shape of the dataset") 
    if shape:
        st.write(dataset1.shape)
  
    # Returns size of dataframe
    size = st.checkbox("Click to see the size of the dataset") 
    if size:
        st.write(dataset1.size)

#Interactive Widgets
    st.text("Please Click to View the Bar Graph Showing the Number of Total Cases of Covid-19 Across Countries/Regions of the WHO")
    if st.button("Check the Graph"):
        st.subheader("A Bar Graph Showing the Number of Total Cases of Covid-19 Across Countries/Regions of the WHO")
        st.write(px.bar(dataset1.head(10), x = 'Country/Region', 
        y = 'TotalCases',color = 'TotalCases', 
        height = 500,hover_data = ['Country/Region', 'Continent']))

#Checkbox
    h1 = st.checkbox("Click to see the the graph of total number of test tests by country/region")

    if h1:
        st.write(px.bar(dataset1.head(10), title= "Horizontal Bar Graph of Total Number of Tests by Country/Region", x = 'TotalTests', y = 'Country/Region',
	    color = 'TotalTests',orientation ='h', height = 500,
	    hover_data = ['Country/Region', 'Continent']))

#Radio
    knowledge = st.radio(
        "Test your Knowledge: Which country/region had the highest number of tests",
        ('USA', 'Russia', 'India'))

    if knowledge == 'USA':
        st.success('Correct!!!')
    else:
         st.error('That is Incorrect')

#2nd Dataset
if attribute =='Covid_Grouped Dataset':
    st.balloons()
    with st.expander("Click for more information on the dataset:"): 
        st.write("This dataset contains Date(from 20-01-22 to 20-07-27), Country/Region, Confirmed, Deaths, Recovered, Active, New cases, New deaths, New recovered, WHO Region, iso_alpha.")


#Importing Dataset2
    dataset2 = pd.read_csv("C:/Users/PC/Desktop/covid_grouped.csv")
    if st.button('To see a small sample of the dataset'):
        st.subheader("A Glimpse of the Dataset")
        st.write(dataset2.head(10))
   
    # Returns tuple of shape (Rows, columns)
    shape = st.checkbox("Click to see the shape of the dataset") 
    if shape:
        st.write(dataset2.shape)
  
    # Returns size of dataframe
    size = st.checkbox("Click to see the size of the dataset") 
    if size:
        st.write(dataset2.size)

    Mychoice = st.radio('What type of Animation would you like to see?', ('Interactive Map', 'Bar Graph Animation'))
    if Mychoice == 'Interactive Map':
            st.write(px.choropleth(dataset2,title = "Interactive Map showing the growth of Covid-19 (from Jan to July 2020) across the world.",
                locations="iso_alpha",
                color="Confirmed",
                hover_name="Country/Region", 
                color_continuous_scale="Reds",
                animation_frame="Date"))
    elif Mychoice == 'Bar Graph Animation':
        st.write(px.bar(dataset2, title = "Bar Graph Animation showing the growth of confirmed Covid-19 cases across the WHO region",x="WHO Region", y="Confirmed", color="WHO Region",
	    animation_frame="Date", hover_name="Country/Region"))

    st.text("Please Click to View the 3-D Scatter Plot")
    if st.button("Check the Plot"):
        st.subheader("3-D Scatter Plot")
        st.write(px.scatter_3d(dataset2, title= "3-D Scatter Plot showing the number of Recoveries and New Cases across Countries/Regions affiliated with the WHO as a function of Time",x='Date', y='New cases', z='Recovered',
              color='Country/Region'))

if attribute == 'Covid-19 in the United States':
    st.balloons()
    dataset2 = pd.read_csv("C:/Users/PC/Desktop/covid_grouped.csv")
    df_US= dataset2.loc[dataset2["Country/Region"]=="US"]
    st.text("Since Covid-19 affected the United States of America the most, we decided to explore it even further")
    st.write(df_US.head())

    select_subject = st.selectbox("What would you like to observe?", ('Confirmed Cases', 'Recoveries','New Cases'))
    if select_subject == 'Confirmed Cases':
        st.write(px.bar(df_US, title = "The Number of Confirmed Cases of Cases of Covid-19 in the U.S. as a function of Time",  x="Date", y="Confirmed", color="Confirmed", height=500))
    elif select_subject == 'Recoveries':
        st.write(px.line(df_US,title = "The Number of Recoveries from Covid-19 in the U.S. as a function of Time",x="Date", y="Recovered", height=500))
    elif select_subject == 'New Cases':
        st.write(px.bar(df_US,title = "The Number of New Cases of Cases of Covid-19 in the U.S. as a function of Time",x="Date", y="New cases", height=500))
