# Dashboard application

# Imports
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore


# Load your dataset
data = pd.read_csv("data/fatalities.csv")

# Create a Streamlit app
st.title("Incident Data Analysis Dashboard")

# Sidebar for data upload
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])


# If a file is uploaded, use it as the dataset
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)


    # displaying important information within sidebar
    # Number of events
    num_events = len(data)
    st.sidebar.write('NO of Events',num_events)
    # Types of weapons used
    weapons_used = data['ammunition'].value_counts()
    # Display the ammunition list
    st.subheader("Ammunition List")
    st.sidebar.write(weapons_used)



    col1, col2 = st.sidebar.columns(2)
    col3, col4 = st.sidebar.columns(2)

    citizenship_counts = data['citizenship'].value_counts()
    event_location_region_counts = data['event_location_region'].value_counts()
    hostilities_counts = data[data['took_part_in_the_hostilities'] == 'Yes']['citizenship'].value_counts()
    no_hostilities_counts = data[data['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()

    with col1:
        st.subheader("Citizenship")
        st.write(citizenship_counts)

    with col2:
        st.subheader("Event Location Region")
        st.write(event_location_region_counts)

    with col3:
        st.subheader("hostilities")
        st.write(hostilities_counts)
    with col4:
        st.subheader('no hostilities')
        st.write(no_hostilities_counts)
