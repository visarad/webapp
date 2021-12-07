import streamlit as st

import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns


import joblib


def main():
    st.title('This is streamlit')
    activity = ['EDA','Prediction','Metrics']
    choice = st.sidebar.selectbox("Choose An Activity",activity)
    st.set_option('deprecation.showPyplotGlobalUse', False)    
    #Load File
    data = st.file_uploader("upload File in csv Format")
    

    if data == None:
        pass
    else:
        df = pd.read_csv(data)
        if choice == 'EDA':
            st.subheader('EDA Section')
            st.text("Exploratory Data Analysis")

            #Preview Data
            if st.checkbox("Preview Data"):
                number = st.number_input("Number of Rows to Show",step=1,min_value=0,max_value=df.shape[0])
                if int(number) > 0:
                    st.dataframe(df.head(number))

            #Show columns/Rows
            if st.checkbox('Column Names'):
                st.write(df.columns)
            
            #Show Description
            if st.checkbox('Show Description'):
                st.write(df.describe())
            
            #Selection of columns

            if st.checkbox("Select Columns to Show"):
                all_columns = df.columns
                selected_columns = st.multiselect("Select Columns",all_columns)
                if selected_columns:
                    st.dataframe(df[selected_columns].head(5))

            #Show Corr plot

            if st.checkbox("Show Correlation Plot[MatplotLib]"):
                plt.matshow(df.iloc[:,1:45].corr())
                st.pyplot()
                


if __name__ == '__main__':
    main()

