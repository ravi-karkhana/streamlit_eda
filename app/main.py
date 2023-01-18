import streamlit as st
import pandas as pd
import graph
import seaborn as sns
import matplotlib.pyplot as plt

file = st.file_uploader("upload a file",type=["xlsx","csv"])



if file is not None:
    if "xlsx" in file.name:
        df = pd.read_excel(file)
        column_list = list(df.select_dtypes(include='number').columns)
    elif "csv" in file.name:
        df = pd.read_csv(file)
        column_list = list(df.select_dtypes(include='number').columns)
    
    c1,c2 = st.columns(2)
    with c1:
        column = st.selectbox("Pick one column",column_list)
        bin = st.selectbox("Select quartile bin size",(5,7,10))
    with c2:
        list_ = range(50,101,bin)
        start, end = st.select_slider(
            'Select a range of Quartile',
            options=list_,
            value=(list_[0], list_[-1]))

    parameter = range(start, end,bin)
    
    hori_cell, verti_cell = graph.optimumum_grid(len(parameter))
    fig, axes = plt.subplots(hori_cell, verti_cell, figsize=(18, 10),constrained_layout = True)
    i = 0
    for j in range(hori_cell):
        for k in range(verti_cell):
            if i < len(parameter):
                dfg = graph.outlier_treat(df, column, parameter[i]/100)
                sns.histplot(ax=axes[j, k], x = dfg[column],
                             kde=True).set(title = "Hist plot with {} outlier".format(parameter[i]/100))
                i+=1
    st.pyplot(fig)
    st.dataframe(df)
